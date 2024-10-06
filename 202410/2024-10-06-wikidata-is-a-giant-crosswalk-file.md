# Wikidata is a Giant Crosswalk File
- URL: https://www.dbreunig.com/2024/10/04/wikidata-is-a-giant-crosswalk-file.html
- Added At: 2024-10-06 08:21:16
- [Link To Text](2024-10-06-wikidata-is-a-giant-crosswalk-file_raw.md)

## TL;DR
文章介绍了如何利用Wikidata的结构化数据构建跨平台数据表，通过DuckDB和Ruby脚本处理近140GB的JSON数据集，分割数据以避免性能问题，并探索了Wikidata的声明系统及其外部ID的应用。

## Summary
1. **Wikidata概述**：
   - Wikidata是Wikipedia的结构化数据版本，内容丰富且以结构化数据形式呈现。
   - 每个条目包含大量元数据和外部ID，这些ID可以用于跨平台数据抓取和应用开发。

2. **构建跨平台数据表**：
   - 使用DuckDB和Ruby脚本构建一个针对地点的跨平台数据表。
   - 需要下载近140GB的Wikidata JSON数据集。

3. **数据处理**：
   - 避免直接解压大文件，而是将其分割成小批次处理，以避免机器性能问题。
   - 使用命令行工具将数据流分割成100,000条记录的小文件，并压缩保存。

4. **数据探索**：
   - 使用DuckDB查询数据，统计实体数量。
   - 查看单个记录的结构，了解Wikidata的实体结构，包括基本信息、标签、描述、别名、站点链接和声明。

5. **声明系统**：
   - Wikidata的声明系统类似于OpenStreetMap的标签系统，支持灵活的数据元素和关系描述。
   - 声明可以描述外部ID，如AllTrails、Library of Congress等，支持多平台数据关联。

6. **外部ID示例**：
   - 以比利时为例，展示其外部ID的多样性，包括图书馆、新闻网站、视频游戏平台等。
   - 地理标识符如OpenStreetMap、Google Maps和Apple Maps也有相应的声明。

7. **数据准备**：
   - 使用Ruby脚本预处理数据，去除不需要的元数据，并将数据转换为更易处理的格式。
