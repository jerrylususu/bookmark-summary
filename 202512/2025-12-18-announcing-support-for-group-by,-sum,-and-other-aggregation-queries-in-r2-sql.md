# Announcing support for GROUP BY, SUM, and other aggregation queries in R2 SQL
- URL: https://blog.cloudflare.com/r2-sql-aggregations/
- Added At: 2025-12-18 14:42:44
- Tags: #read #db
- [Link To Text](2025-12-18-announcing-support-for-group-by,-sum,-and-other-aggregation-queries-in-r2-sql_raw.md)

## TL;DR
Cloudflare R2 SQL 新增支持的聚合查询功能包含GROUP BY、SUM等，利用Scatter-Gather和Shuffling两种分布式策略处理数据，帮助用户快速获取大数据摘要并支持报告生成和异常检测。该功能已上线，适用于R2存储的Parquet文件。

## Summary
Cloudflare 宣布在 R2 SQL 中新增支持 GROUP BY、SUM 等聚合查询功能，旨在帮助用户从海量数据中快速获取摘要信息，以生成报告、发现趋势或检测异常。

聚合查询可以对数据进行分组并计算汇总值，典型示例如下：
- 按部门统计销售总额：`SELECT department, sum(value) FROM sales GROUP BY department`
- 结合 ORDER BY 和 LIMIT 获取前几名：`SELECT department, sum(value) FROM sales GROUP BY department ORDER BY sum(value) DESC LIMIT 10`
- 使用 HAVING 过滤分组结果：`SELECT department, sum(value), count(*) FROM sales GROUP BY department HAVING count(*) > 5`

R2 SQL 采用两种分布式执行策略来处理聚合查询：
1. **Scatter-Gather 策略**  
   适用于不含 HAVING 或 ORDER BY 的聚合查询。查询协调节点将任务分发到多个工作节点，各节点计算“预聚合”中间结果后返回协调节点进行合并。这种方式高效处理简单聚合，但无法应对需要全局排序或过滤的场景。

2. **Shuffling 策略**  
   当查询涉及基于聚合结果的排序或过滤时，采用数据混洗机制。工作节点通过哈希分区将相同分组的数据路由到同一节点，确保全局计算准确。随后各节点本地完成聚合、过滤和排序，协调节点仅需进行流式合并即可返回结果，有效避免单点瓶颈。

R2 SQL 基于 Cloudflare 的无服务器分布式架构，支持对 R2 Data Catalog 中存储的 Parquet 文件执行查询，无需用户管理复杂 OLAP 基础设施。聚合功能现已上线，用户可参考官方文档和开发者社区进一步使用。
