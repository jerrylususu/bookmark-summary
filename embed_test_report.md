# 嵌入搜索示例测试记录

- 测试时间：2025-11-03
- 索引命令：`./.venv/bin/python scripts/embed_search_example.py --max-docs 10`
- 查询命令：脚本运行后依次输入  
  `AI 智能助手` → 回车  
  `隐私 安全` → 回车  
  `投资 策略` → 回车  
  最后按 `Ctrl-D` 结束交互。
- 索引说明：加载 `data.json` 中最新 10 篇书签摘要，使用默认 `top_k=5`。

## 查询：`AI 智能助手`
1. **Mapping the landscape of gen-AI product user experience**（202407，得分 0.554）  
   - 链接：https://interconnected.org/home/2024/07/19/ai-landscape  
   - 亮点：关于生成式 AI 产品体验的调研与设计模式讨论。
2. **How not to use box shadows**（202407，得分 0.447）  
   - 链接：https://dgerrells.com/blog/how-not-to-use-box-shadows  
   - 亮点：分享 UI 设计中 box shadow 的另类用法。
3. **How we improved availability through iterative simplification**（202407，得分 0.434）  
   - 链接：https://github.blog/engineering/engineering-principles/how-we-improved-availability-through-iterative-simplification/  
   - 亮点：GitHub 团队讨论迭代简化提升可用性的经验。
4. **We need visual programming. No, not like that.**（202407，得分 0.426）  
   - 链接：https://blog.sbensu.com/posts/demand-for-visual-programming/  
   - 亮点：探讨面向开发者的可视化编程需求。
5. **Mocking is an Anti-Pattern**（202407，得分 0.396）  
   - 链接：https://www.amazingcto.com/mocking-is-an-antipattern-how-to-test-without-mocking/  
   - 亮点：讨论在测试中过度使用 mocking 的风险。

## 查询：`隐私 安全`
1. **Anyone can Access Deleted and Private Repository Data on GitHub ◆ Truffle Security Co.**（202407，得分 0.509）  
   - 链接：https://trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github  
   - 亮点：曝光 GitHub 已删除或私有仓库仍可被访问的安全隐患。
2. **Python Practical Package Packing 2024**（202407，得分 0.467）  
   - 链接：https://matt.sh/python-project-structure-2024  
   - 亮点：Python 项目结构与打包实践。
3. **Mapping the landscape of gen-AI product user experience**（202407，得分 0.459）  
   - 链接：https://interconnected.org/home/2024/07/19/ai-landscape  
   - 亮点：生成式 AI 产品体验研究。
4. **How we improved availability through iterative simplification**（202407，得分 0.456）  
   - 链接：https://github.blog/engineering/engineering-principles/how-we-improved-availability-through-iterative-simplification/  
   - 亮点：面向高可用的工程实践。
5. **How not to use box shadows**（202407，得分 0.454）  
   - 链接：https://dgerrells.com/blog/how-not-to-use-box-shadows  
   - 亮点：UI 设计技巧。

## 查询：`投资 策略`
1. **Panic! at the Tech Job Market**（202407，得分 0.468）  
   - 链接：https://matt.sh/panic-at-the-job-market  
   - 亮点：以戏谑语气分析科技行业就业市场变化。
2. **We need visual programming. No, not like that.**（202407，得分 0.417）  
   - 链接：https://blog.sbensu.com/posts/demand-for-visual-programming/  
   - 亮点：关注开发者工具领域的可视化编程趋势。
3. **How we improved availability through iterative simplification**（202407，得分 0.411）  
   - 链接：https://github.blog/engineering/engineering-principles/how-we-improved-availability-through-iterative-simplification/  
   - 亮点：复杂系统的持续迭代方法。
4. **Python Practical Package Packing 2024**（202407，得分 0.400）  
   - 链接：https://matt.sh/python-project-structure-2024  
   - 亮点：Python 包发布最佳实践。
5. **Mocking is an Anti-Pattern**（202407，得分 0.395）  
   - 链接：https://www.amazingcto.com/mocking-is-an-antipattern-how-to-test-without-mocking/  
   - 亮点：测试策略讨论。

## 数据库与持久化说明

### 关于 `embed_search_example.py`

**重要提示**：`embed_search_example.py` 是一个**演示/原型脚本**，**不会持久化存储数据**。

- 每次运行都会实时调用嵌入 API 获取向量
- 所有索引存储在内存中，程序结束后立即释放
- 不会创建或使用 `embeddings.sqlite` 数据库
- 适用于快速测试和交互式搜索，不适合生产环境

### 持久化存储

若需持久化存储嵌入向量，请使用：

```bash
python scripts/embedding_runner.py --repo-root /path/to/bookmark-summary
```

该脚本会：
- 创建 `embeddings.sqlite` SQLite 数据库（位于当前工作目录）
- 基于 `summary_hash` 和 `raw_hash` 实现增量更新
- 支持多模型版本管理和向量修剪
- 适合生产环境的定时任务（如 cron job）

## 备注
- 三个查询都成功返回 5 条结果，API 请求稳定，未出现异常重试。
- 第二与第三个查询呈现大量工程与工具类文章，提示索引内容以开发实践为主。
- 如需更贴合投资主题，可扩大 `--max-docs` 或引入金融类书签以丰富嵌入语料。
