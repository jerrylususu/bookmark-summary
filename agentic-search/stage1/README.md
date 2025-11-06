# Stage 1: Agentic Search 原型

## 概述

这是一个基于LLM的智能代理搜索原型，验证了LLM自主调用工具来解决复杂查询的能力。系统集成了向量搜索、关键词搜索和文本读取工具，通过LLM进行智能工具选择和答案生成。

## 核心特性

- 🤖 **LLM驱动的工具选择**：智能选择最适合的搜索工具
- 🔍 **多模态搜索**：结合语义搜索和关键词搜索
- 📚 **文本内容读取**：深入阅读文档内容
- 🎯 **智能答案生成**：基于搜索结果生成高质量回答
- ⚡ **失败暴露机制**：不隐藏错误，便于调试

## 项目结构

```
stage1/
├── prototype.py          # 原型入口程序
├── tools/                # 工具模块
│   ├── keyword_search.py # 关键词搜索
│   ├── vector_search.py  # 向量搜索（使用现有embedding基础设施）
│   └── text_reader.py    # 文本读取
├── core/
│   ├── agent.py          # 核心代理逻辑
│   └── llm_client.py     # LLM客户端
└── README.md            # 本文件
```

## 环境要求

### Python环境
- Python 3.8+
- 使用项目的虚拟环境：`source .venv/bin/activate`

### 依赖库
- `tiktoken` - Token计数（与embedding_pipeline.py保持一致）
- `numpy` - 向量计算
- `requests` - HTTP请求
- `sqlite3` - 数据库访问

### 外部服务
- **Embedding API**：SiliconFlow（用于向量搜索）
- **LLM API**：配置在.env文件中

## 配置文件

确保`.env`文件包含以下配置：

```bash
# Embedding配置（用于向量搜索）
SF_TOKEN=your_embedding_token
EMBED_MODEL=BAAI/bge-m3

# LLM配置（用于工具选择和答案生成）
LLM_TOKEN=your_llm_token
LLM_MODEL=gpt-5-nano
LLM_ENDPOINT=https://your-llm-api-endpoint/v1/chat/completions
```

## 使用方法

### 1. 激活虚拟环境并运行

```bash
cd /home/jerrylu/code/251028-bookmark-by-month/bookmark-summary
source .venv/bin/activate
cd agentic-search/stage1
```

### 2. 运行默认测试查询

```bash
python prototype.py
```

### 3. 运行所有硬编码测试查询

```bash
python prototype.py --test
```

### 4. 指定自定义查询

```bash
python prototype.py --query "什么是embedding"
python prototype.py --query "Find articles about LLM"
python prototype.py --query "2024年前端技术相关文章"
```

### 5. 详细输出模式（显示工具调用详情）

```bash
python prototype.py --query "LLM" --verbose
```

## 工具说明

### keyword_search
- **功能**：基于关键词搜索文件内容
- **使用场景**：查找特定术语、文件名或精确匹配
- **参数**：
  - `query`：搜索关键词
  - `max_results`：最大结果数（默认10）

### vector_search
- **功能**：基于语义相似度的智能搜索
- **使用场景**：概念性查询、主题性搜索、模糊匹配
- **参数**：
  - `query`：查询文本
  - `top_k`：返回结果数（最大10）
  - `chunk_types`：指定chunk类型（可选）
- **技术**：使用现有的embeddings.sqlite数据库

### text_reader
- **功能**：读取指定文件的行范围内容
- **使用场景**：深入查看文档详细内容
- **参数**：
  - `file_path`：文件路径
  - `start_line`：开始行号（默认1）
  - `end_line`：结束行号（默认200）

## 系统限制

- **最大工具调用次数**：10次
- **最大对话token数**：60,000 tokens
- **文本读取最大行数**：200行
- **向量搜索top_k**：≤ 10
- **严格失败模式**：LLM不可用或工具失败时直接报错，不回退

## 工作原理

1. **查询分析**：LLM分析用户查询意图
2. **工具选择**：智能选择最适合的搜索工具
3. **迭代搜索**：根据结果动态选择下一步操作
4. **结果整合**：收集所有有用的搜索结果
5. **答案生成**：LLM基于搜索结果生成结构化回答

## 示例查询

### 技术概念查询
```bash
python prototype.py --query "什么是embedding"
python prototype.py --query "向量搜索的原理"
python prototype.py --query "tokenization的作用"
```

### 文章检索查询
```bash
python prototype.py --query "Find all articles about LLM embeddings"
python prototype.py --query "前端性能优化相关文章"
```

### 时间范围查询
```bash
python prototype.py --query "2024年6月有哪些AI相关的文章？"
python prototype.py --query "最近关于RAG的技术文章"
```

### 混合查询
```bash
python prototype.py --query "embedding在机器学习中的应用案例"
python prototype.py --query "如何优化大模型的推理速度"
```

## 输出格式

### 成功查询输出
```
📋 最终答案
============================================================
[LLM生成的结构化答案]

📊 统计信息:
  - 工具调用次数: X
  - 置信度: high/medium/low
  - 处理时间: X.XX 秒
  - 来源文件 (X 个):
    • document_id_1
    • document_id_2
```

### 详细模式输出（--verbose）
```
🔧 工具调用详情:
  1. vector_search
     参数: {"query": "embedding", "top_k": 5}
     结果: 找到 X 条记录
  2. text_reader
     参数: {"file_path": "path/to/file", "start_line": 1, "end_line": 50}
     结果: 无匹配内容
```

## 错误处理

系统采用**严格失败模式**：
- ✅ LLM不可用：直接失败并显示具体错误
- ✅ 向量搜索失败：抛出异常，不回退到关键词搜索
- ✅ 工具调用失败：暴露错误信息，便于调试
- ✅ 配置错误：明确指出缺失的配置项

## 调试建议

1. **检查环境变量**：确认`.env`文件配置正确
2. **验证API连接**：单独测试embedding和LLM API
3. **查看详细日志**：使用`--verbose`模式查看完整工具调用过程
4. **检查数据库**：确认`embeddings.sqlite`存在且可访问

## 性能参考

基于实际测试：
- **典型查询时间**：30-90秒
- **平均工具调用**：5-10次
- **常见置信度**：high（多个相关结果时）
- **处理能力**：支持中英文混合查询

## 下一步开发

Stage 1验证了核心概念，后续可以扩展：
- Stage 2：添加HTTP服务器接口
- Stage 3：开发CLI界面
- Stage 4：构建Web前端

## 故障排除

### 常见问题

**Q: "LLM不可用，无法启动代理"**
A: 检查`.env`中的LLM_TOKEN、LLM_MODEL、LLM_ENDPOINT配置

**Q: "embedding modules not available"**
A: 确保在正确的虚拟环境中，且路径设置正确

**Q: 向量搜索返回空结果**
A: 检查embeddings.sqlite数据库是否存在且有数据

**Q: 工具调用次数过多**
A: 系统限制为10次，LLM会智能选择何时停止搜索