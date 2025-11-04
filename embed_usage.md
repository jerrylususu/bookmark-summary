# 嵌入脚本使用说明

本文汇总仓库中与嵌入相关的脚本，包括批量生成嵌入、交互式示例搜索，以及基于 SQLite 的查询工具。所有命令均假设你位于仓库根目录，且使用预置的 `.venv` 虚拟环境。

## 1. 环境准备
- 确认 `.venv` 已安装依赖：`source .venv/bin/activate`（或在命令前加 `./.venv/bin/`）。
- 配置嵌入服务凭据：在仓库根目录创建或更新 `.env`，至少包含  
  `SF_TOKEN=<你的 API Key>`  
  `EMBED_MODEL=<嵌入模型名称>`。

## 2. 批量生成嵌入：`scripts/embedding_runner.py`
- 该脚本读取 `data.json`，并将摘要、TL;DR 与原文切分成多个 chunk 后写入 `embeddings.sqlite`。
- 默认情况下，即使不加 `--verbose` 也会显示基于 `tqdm` 的进度条，实时反映文档处理进度。
- 常用参数：
  - `--max-docs N`：仅处理前 N 篇文档；
  - `--dry-run`：仅展示计划嵌入的 chunk 数，不调用 API、不写入数据库；
  - `--skip-summary` / `--skip-raw`：跳过摘要或原文内容的嵌入；
  - `--force`：即使签名未变化也强制重新嵌入；
  - `--rpm N`：限制每分钟最多发起 N 次嵌入请求；
  - `--tpm N`：限制每分钟消耗的 token 数不超过 N（基于 `tiktoken` 的 `cl100k_base` 估算）。若同时提供 `--rpm` 与 `--tpm`，脚本会自动按照更严格的限速执行。

示例命令：
```bash
./.venv/bin/python scripts/embedding_runner.py --max-docs 20
```

## 3. 交互式示例搜索：`scripts/embed_search_example.py`
- 该脚本会现用现取文档 Markdown，构建一个临时向量索引，并进入交互式命令行。
- 默认仅索引前 10 篇文档，可通过 `--max-docs` 调整；使用 `--top-k` 控制每次查询展示结果数量。
- 启动后按照提示输入查询，按 `Ctrl-D`（或 Windows 下 `Ctrl-Z`+回车）退出。

示例命令：
```bash
./.venv/bin/python scripts/embed_search_example.py --max-docs 10 --top-k 6
```

## 4. SQLite 向量搜索：`scripts/embed_search_db.py`
- 已运行过 `embedding_runner.py` 后，可直接复用 `embeddings.sqlite` 中缓存的向量，避免重新读取 Markdown。
- 通过位置参数传入查询文本，例如 `"大语言模型"`；脚本会嵌入查询向量并输出相似度最高的 chunk。
- 常用参数：
  - `--top-k N`：显示前 N 条结果；
  - `--chunk-type summary --chunk-type tldr`：限制匹配的 chunk 类型，可重复指定；
  - `--database path/to/sqlite`：自定义数据库路径。

示例命令：
```bash
./.venv/bin/python scripts/embed_search_db.py "大语言模型" --top-k 5 --chunk-type summary
```

## 5. 数据统计导出：`scripts/embed_db_explorer.py`
- 读取 `embeddings.sqlite` 中的 `documents` 与 `chunks` 表，统计每篇文章的 summary/TL;DR/raw chunk 数量与总计。
- 默认使用 Rich 输出表格，可结合 `--limit` 截断展示行数；若未安装 `rich`，可切换 `--format json` 或 `--format csv`。
- `--embed-model` 可筛选特定模型，`--output` 用于将 JSON/CSV 写入文件；未指定时直接打印到终端。

示例命令：
```bash
./.venv/bin/python scripts/embed_db_explorer.py
./.venv/bin/python scripts/embed_db_explorer.py --format csv --output stats.csv
```

以上脚本共用 `.env` 中的模型配置。推荐先使用 `embedding_runner.py` 生成完整索引，再依据需要选择交互式查询、数据库搜索或统计导出脚本进行分析。
