# Designing software that could possibly work
- URL: https://www.seangoedecke.com/planning-software/
- Added At: 2025-04-14 13:41:53
- [Link To Text](2025-04-14-designing-software-that-could-possibly-work_raw.md)

## TL;DR


文章指出软件设计常犯两大错误：早期规划停留过高层次或过早纠结技术细节。正确方法应围绕核心用户流程（如提交评论）端到端验证可行性：用伪代码级逻辑推演关键步骤，暴露问题并确定基础架构约束（如身份验证、数据存储），避免过早技术选型。最终通过简洁文档沟通方案，保持可迭代调整，确保基础功能先能运作。

## Summary


文章总结了设计可行软件的思路，指出许多工程师在早期规划阶段常犯的两大错误：  
1. **停留过高层次**：例如设计博客评论系统时仅提出“用关系型数据库存储评论”，未具体说明数据如何从前端传输到数据库；  
2. **过早纠结细节**：如直接争论使用React的RSC还是TSQ获取数据，却未验证基本功能是否可行。  

**正确方法**：  
- **追踪核心用户流程端到端**：选择最关键的操作路径（如用户提交并查看评论），用伪代码级别的逻辑细节推演实现过程，确保每一步“至少能运作”。例如：  
  - 用户填写表单 → 后端接收数据 → 存储评论 → 重定向并展示评论列表；  
  - 在此过程中暴露缺失环节（如身份验证、数据存储）、潜在问题（如性能瓶颈）及技术约束（如静态博客需转为动态服务）。  

**设计示例**：  
以评论系统为例，需解决：用户身份关联方式、数据持久化手段、展示时的性能优化（如缓存），以及边缘场景（如私有部署的存储问题）。这些思考需基于系统必须满足的基础逻辑，而非具体技术选型。  

**沟通与迭代**：  
- 草稿计划应留存在思维中，主要用于**估算工作量**和**提出关键问题**（如是否采用第三方评论服务）；  
- 记录计划时采用简洁的流程图或文字描述，后续团队可在此基础上探讨技术细节，但需保持开放态度，随时调整方案。  

核心观点：软件设计必须从“能运作”出发，优先验证基本流程可行性，而非过早陷入无关细节或不切实际的方案，避免因基础架构缺陷导致后续重构困难。
