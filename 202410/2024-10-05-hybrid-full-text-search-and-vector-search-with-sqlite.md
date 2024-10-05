# Hybrid full-text search and vector search with SQLite
- URL: https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html
- Added At: 2024-10-05 02:11:16
- [Link To Text](2024-10-05-hybrid-full-text-search-and-vector-search-with-sqlite_raw.md)

## TL;DR
文章讨论了全文搜索与向量搜索的结合，通过`sqlite-vec`扩展在SQLite中实现混合搜索。全文搜索和语义搜索各有优劣，结合使用能提高搜索效果。文章还提供了构建和查询示例，并探讨了不同混合搜索方法的应用场景和未来改进方向。

## Summary
1. **全文搜索与向量搜索的结合**：
   - `sqlite-vec`和其他向量搜索工具的主要用途是为文本数据提供“语义搜索”。
   - 全文搜索（关键词搜索）有时效果不佳，例如“气候变化”不会返回提到“全球变暖”的文档。
   - 语义搜索允许用户通过“感觉”查找结果，返回更有意义的结果。

2. **单一语义搜索的局限**：
   - 仅使用语义搜索可能对应用有害，例如在HBO Max上搜索“冒险时间”时，结果不准确。
   - 语义搜索可能返回与查询不完全匹配但相关的结果，而全文搜索则更直接。

3. **SQLite的全文搜索与向量搜索结合**：
   - SQLite已具备全文搜索功能，通过[FTS5扩展](https://www.sqlite.org/fts5.html)实现。
   - 结合`sqlite-vec`扩展，可以在命令行、移动设备、Raspberry Pis和Web浏览器（通过WASM）上实现混合搜索。

4. **示例：NBC新闻标题数据集**：
   - 使用从NBC新闻站点抓取的14,500+个标题，数据量为4.3MB。
   - 构建FTS5索引和向量索引，使用`fts5`和`vec0`虚拟表。

5. **构建全文搜索FTS5表**：
   - 通过SQL语句创建、填充和优化`fts_headlines`全文搜索虚拟表。
   - 示例查询返回包含“planned parenthood”的标题及其排名。

6. **构建向量搜索`sqlite-vec`表**：
   - `sqlite-vec`提供向量存储和比较，但不生成嵌入。
   - 使用`sqlite-lembed`扩展和`Snowflake Artic Embed 1.5模型`生成嵌入。
   - 将嵌入存储在`vec0`虚拟表中，并进行KNN查询。

7. **混合搜索方法**：
   - **方法1：关键词优先**：先返回全文搜索结果，然后用向量搜索补充。
   - **方法2：倒数排名融合（RRF）**：结合全文搜索和向量搜索结果，提高两者匹配的排名。
   - **方法3：按语义重新排序**：先进行全文搜索，然后根据向量距离重新排序结果。

8. **选择合适的混合搜索方法**：
   - 取决于应用场景，如电子邮件搜索、内部文档搜索或重复帖子检测。
   - SQLite使得实验和原型设计变得简单，数据存储在单个文件中，支持多种编程语言。

9. **未来改进**：
   - FTS5和`sqlite-vec`的结合在小型样本中表现良好，但仍需改进。
   - 例如，FTS5支持文档中的匹配高亮显示，而`sqlite-vec`目前不支持。
   - 支持分区、元数据过滤等功能正在开发中。

10. **总结**：
    - 尝试在项目中使用`sqlite-vec`进行混合搜索，并在Mozilla Discord的`#sqlite-vec`频道中提出问题。
