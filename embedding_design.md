# Bookmark Summary 项目嵌入/RAG 设计

## 1. 现状梳理
- `process_changes.py` 负责发现新书签、拉取原文、生成摘要与 TL;DR，并在 `YYYYMM/` 目录下写入摘要（结构化 Markdown）和原文文本，同时维护 `data.json`（仅存摘要元数据）。
- 生成的 Markdown 结构固定：头部元数据、`## TL;DR`、`## Summary`；原文以 `<date>-<slug>_raw.md` 形式存放。
- 现无嵌入/向量存储逻辑；现阶段计划通过独立的后台脚本补齐嵌入，用于语义检索与相关文章发现，而非在 Git 工作流内联生成。

## 2. RAG 目标与约束
- 目标：基于书签内容做语义检索（问答、聚合分类等）。需要兼顾“快速定位摘要”与“必要时回退到原文细节”，并支撑“相关文章推荐”这一后台能力。
- 约束：嵌入计算不与 Git 变更一并提交；在独立服务器上通过 cron job 每小时拉取最新仓库状态后运行；避免重复调用昂贵的 embedding API；结构需支持持续追加；无外部托管依赖；与现有目录结构兼容。

## 3. 嵌入范围方案对比

| 方案 | 内容范围 | 优点 | 风险/不足 | 适用 |
| --- | --- | --- | --- | --- |
| 仅摘要 | `## Summary` 或 TL;DR 文本 | 文本短、成本低；结构稳定 | 丢失原文细节，难回答细粒度问题 | 只做摘要检索 |
| 摘要 + 原文整体 | 摘要全文 + 原文拼接 | 信息完整 | 原文过长导致嵌入质量下降、费用高；更新即全量重算 | 原文极短场景 |
| **摘要 + 原文分块（推荐）** | 保留一份摘要向量 + 原文 chunk | 兼顾概览和细节，支持部分重算 | 需要分块/管理 chunk | 需要更完整的问答能力 |

> 推荐选项：同时存储摘要级嵌入（单条）与原文分块嵌入（结构化 chunk）。原文 chunk 可灵活选择是否启用或按需触发，以控制成本。

## 4. 推荐方案细节

### 4.1 语料结构
- 文档 ID：使用 `bookmark_identity()`（月、标题、timestamp）生成稳定键，作为 `document_id`。
- 元数据：保留 `url`、`tags`、`timestamp`、`month`，新增 `summary_hash`、`raw_hash`（基于文件内容 SHA256，避免重复计算）。
- Chunk 层级：
  - `summary`: 一个 chunk，来源于 `## Summary` 段落（可选附加 TL;DR 作为独立 chunk）。
  - `raw`: 使用 Markdown 解析（优先 `mistune`，fallback 正则）按层级切分；单个 section 再基于 token 长度（例如 700 token）做二次切片，窗口重叠 ~15%。Chunk 元数据包含 `section_heading`、`chunk_index`。

### 4.2 嵌入生成流程
1. 后台服务器通过 cron job（推荐每小时）执行：
   - `git pull` 获取仓库最新内容（仅用于读取；不回推）。
   - 运行独立 CLI：`python scripts/embedding_runner.py --repo-root /path/to/bookmark-summary`。
2. `embedding_runner.py` 读取 `YYYYMM/` 下的 Markdown 和原文，根据 manifest 计算 `summary_hash`/`raw_hash`，确定需增量处理的文档。
3. 哈希未变化 → 跳过对应 chunk；哈希变化或新增 → 调用嵌入 API（模型配置化，如 `text-embedding-3-small`）。
4. API 返回向量后，将数据写入后台向量存储（见 §5），并更新 manifest。脚本提供 `--tqdm` 进度条、`--force` 全量刷新、`--dry-run` 等参数，便于手动调试。
5. 嵌入及 manifest 文件不提交回 Git；如需调试，可本地导出快照（JSONL/Parquet）。

### 4.3 去重与重算控制
- Manifest 表：`documents(document_id PRIMARY KEY, summary_hash, raw_hash, embed_model, updated_at, meta...)`，其中 `embed_model` 记录嵌入模型或供应商版本（如 `openai/text-embedding-3-small@2024-07`），便于后续切换或并存多模型。
- Chunk 表：`chunks(id, document_id, chunk_type, chunk_index, heading, text_sha, embed_model, token_count, embedding, created_at)`，允许按 chunk 追踪具体模型，支持回填时混合多模型或分阶段迁移。
- 通过哈希比较即可避免每次 backfill 时重复请求嵌入；必要时提供 CLI `--force-embedding` 选项强制刷新。

## 5. 向量存储形态

### 推荐：SQLite + 自定义向量列
- 结构化：易于和现有 JSON 数据互通，文件型，追加友好。
- 方案：使用 `sqlite3` 保存元数据；嵌入向量保存为 `BLOB`（`array('f')` 或 `numpy.tobytes()`）。
- 检索：可在后台服务中用 `numpy`/`faiss` 做相似度查询；如需内嵌 SQL 相似度，可集成 `sqlite-vss`/`pgvector`（可选）。
- 文件位置：部署机本地目录（例如 `/var/lib/bookmark-summary/embeddings.sqlite`）。该文件及配套 manifest 存于服务器，不进入 Git；仓库中可保留 `.gitignore` 以避免误提交。

### 备选方案对比
- **JSONL/Parquet**：追加简单，但查询/更新不便；仍需加载至内存做向量检索。适合作为轻量导出格式。
- **专门向量库（Chroma、Qdrant 等）**：检索性能好，API 友好；但引入额外依赖/服务，不易在 GitHub Action 中无痛运行。
- **FAISS 索引文件 + JSON 元数据**：检索最快，但增量写复杂（需重建或使用 IVF 索引合并）。适合大规模离线批处理，目前用不上。

> 基于部署成本与可维护性，建议首选 SQLite，实现“单文件可提交”的向量仓库。未来若查询瓶颈明显，再考虑替换/导出。

## 6. 代码改动建议
- 保持 `process_changes.py` 聚焦“发现 → 摘要生成 → 写文件”；无需在该流程内触碰嵌入逻辑。
- 新脚本与模块：
  - `scripts/embedding_runner.py`：命令行入口，处理参数解析（`--repo-root`、`--force`、`--dry-run`、`--show-progress` 等）和 tqdm 进度展示。
  - `embedding_store.py`：封装 SQLite 连接、建表、插入/更新、查询操作。
  - `embedding_pipeline.py`：包含 chunking、哈希计算、调用 `requests` 获取嵌入 API 的逻辑；保持与主逻辑解耦，便于单元测试。
- `requirements.txt`: 视需要增加 `tiktoken`（token 计数）、`numpy`（向量处理）、可选 `mistune`（已存在）与 `langdetect`（附加语言标签）。
- 部署机设置 cron job，例如：`0 * * * * /usr/bin/env OPENAI_API_KEY=... /usr/bin/python /srv/bookmark-summary/scripts/embedding_runner.py --repo-root /srv/bookmark-summary >> /var/log/bookmark-embedding.log 2>&1`。无需在 GitHub Action 中执行。

## 7. 待确认问题与推荐答案
- **是否需要对全部历史原文立即补嵌入？**  
  推荐分批：先对摘要全量补嵌入，再按需/按月份批量跑原文分块，以控制成本。
- **Embedding 模型选择？**  
  默认可用 OpenAI `text-embedding-3-small`（便宜）+ TL;DR 场景，如果需要更高质量再切换到 `3-large`；设计时保持模型可配置。
- **是否需要多语言支持？**  
  原文多语言时，建议 chunk 中保留语言字段（可用 `langdetect`，可选）以便检索时过滤。
- **Git 历史膨胀问题？**  
  嵌入文件不再提交 Git，直接存放在服务器本地，避免仓库膨胀。必要时仅在备份/迁移时独立导出。

## 8. 后续迭代建议
- 为嵌入生成单元测试：mock API，验证 chunk 切分 & 去重逻辑。
- 在 `README.md` 或专门运维文档中说明 cron 部署方法、调试命令、如何查询。
- 预留导出接口，将 SQLite 中的嵌入导出到 `parquet`/`faiss` 以便外部分析。

## 9. 实施进度
- 2025-11-03：完成 `scripts/embedding_smoketest.py`，可加载 `.env` 中的 `SF_TOKEN` 并调用 SiliconFlow Embeddings API 验证连通性；依赖通过 `uv add requests python-dotenv` 管理。
- 2025-11-03：在 `.env` 中补充 `EMBED_MODEL`（当前为 `BAAI/bge-m3`）并通过 `uv add` 写入后续嵌入流程所需依赖（`mistune`、`numpy`、`tiktoken`），为 chunking 与向量存储实现铺平依赖基础。
- 2025-11-03：实现嵌入流水线（`embedding_pipeline.py`）、SQLite 向量仓储（`embedding_store.py`）及 CLI 入口（`scripts/embedding_runner.py`），支持基于 `.env` 的模型切换、增量哈希去重、干跑/强制刷新等参数；同日改造烟囱测试脚本以使用实际配置的 `EMBED_MODEL`，并在本地通过 `python3 -m venv` 初始化环境后以 `--max-docs 2` 真实调用 API，验证 manifest 先写入再插 chunk 的流程与 26 条向量入库正常。
- 2025-11-04：为 `scripts/embedding_runner.py` 默认启用 `tqdm` 进度条（无须 `--verbose`），同时补充依赖 `tqdm` 至 `requirements.txt` 并在 `.venv` 中更新安装。
- 2025-11-04：新增基于 SQLite 的检索脚本 `scripts/embed_search_db.py`，复用持久化向量进行命令行查询；完善 `embed_usage.md`，覆盖 runner、交互示例与数据库检索三类脚本的使用指引。
- 2025-11-04：编写 `scripts/embed_db_explorer.py`，汇总 `embeddings.sqlite` 中的文档/Chunk 数量并支持表格、JSON、CSV 三种导出；新增依赖 `rich` 以提升终端表格展示效果，并补充对应使用说明。
- 2025-11-04：优化 `scripts/embedding_runner.py` 进度展示逻辑，引入文档与 chunk 两级 `tqdm` 进度条，并为 `embedding_pipeline.embed_chunks` 加入回调以实时更新批量请求进度，避免长时间无反馈。
- 2025-11-04：在 `scripts/embedding_runner.py` 增加 `--rpm`/`--tpm` 限频参数，结合 `embedding_pipeline.RequestRateLimiter` 以分钟滑窗控制请求与 token 峰值，tiktoken 计数估算批次 tokens；通过 `.venv` 下 `--dry-run` + 限速组合自测验证配置与日志输出。
- 2025-11-04：排查 `--dry-run` 报错 `Encountered text corresponding to disallowed special token '<|fim_prefix|>'`，为 `TokenSplitter` 增加特殊 token 白名单并在命中未覆盖 token 时自动降级为普通文本处理；通过 `.venv` 执行 `python scripts/embedding_runner.py --dry-run --max-docs 200` 验证不再抛出异常，进度条完整跑完。
- 2025-11-04：强化限频可观测性，当 `RequestRateLimiter` 触发请求或 token 滑窗限制时，在 `scripts/embedding_runner.py` 默认日志中输出命中类型与预计恢复时间，并在窗口释放后追加恢复日志，避免误判为网络阻塞。
