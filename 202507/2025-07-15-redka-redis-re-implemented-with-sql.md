# Redka: Redis re-implemented with SQL
- URL: https://antonz.org/redka/
- Added At: 2025-07-15 14:51:02

## TL;DR


Redka是基于Go语言的SQL驱动型Redis替代方案，支持SQLite或PostgreSQL后端，兼具Redis易用性和关系数据库的稳定性。提供独立服务器及Go嵌入模块两种模式，支持主流数据类型，通过SQL表存储数据并支持视图查询。性能低于原生Redis，但适合中小型应用的测试环境或事务一致性需求较高的场景。

## Summary


Redka 是基于 SQL 的 Redis 重构方案，由 Go 语言编写，支持 SQLite 或 PostgreSQL 作为后端数据库。其核心目标是结合 Redis 的便捷 API 与关系型数据库的稳定性，提供键值存储能力。

### 关键特性
- **两种模式**  
  1. 独立 Redis 兼容服务器（通过 RESP 协议交互）。  
  2. Go 语言模块（嵌入应用程序直接使用）。  
- **支持数据类型**  
  字符串（Strings）、列表（Lists）、集合（Sets）、有序集合（Sorted Sets）、哈希（Hashes）。  
- **存储架构**  
  数据以结构化表存储于关系型数据库，提供 SQL 视图方便数据查询。  

### 典型应用场景
1. **嵌入式缓存**  
   Go 应用可直接集成，无需独立 Redis 服务，支持复杂数据结构和事务管理。  
2. **轻量级测试**  
   使用内存数据库快速搭建测试环境，替代复杂的容器化 Redis。  
3. **PostgreSQL 扩展**  
   利用现有 PostgreSQL 环境实现 Redis 类数据结构，保证事务一致性。  

### 实例演示
- **服务器模式**  
  ```bash
  ./redka -h localhost -p 6379
  ```  
  使用 redis-cli 执行基础命令（如 `SET`, `GET`）。  
- **Go 模块模式**  
  通过 API 直接操作数据库，示例代码展示键值设置与读取。  
- **SQL 验证**  
  通过视图 `vstring` 查询键值数据及其元信息（如过期时间）。  

### 性能表现
- **基准测试（百万次操作）**  
  Redis: `GET/SET` 每秒约 13-14 万次  
  Redka（SQLite）: `GET` 约 10 万次/秒，`SET` 约 2.6 万次/秒  
  Redka（PostgreSQL）: `GET` 约 2.5 万次/秒，`SET` 约 1.1 万次/秒  
  **结论**：性能低于原生 Redis，但能满足中小型应用需求。  

### 总结
Redka 适用于测试环境或对性能要求不苛刻的生产场景，特别适合希望统一使用 SQL 工具链的团队。其 GitHub 仓库提供详细文档与示例。
