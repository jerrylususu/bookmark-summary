# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-11-17) [直播观察（二）：怎么把真人的注意力做成大生意](202611/2026-11-17-%E7%9B%B4%E6%92%AD%E8%A7%82%E5%AF%9F%EF%BC%88%E4%BA%8C%EF%BC%89%EF%BC%9A%E6%80%8E%E4%B9%88%E6%8A%8A%E7%9C%9F%E4%BA%BA%E7%9A%84%E6%B3%A8%E6%84%8F%E5%8A%9B%E5%81%9A%E6%88%90%E5%A4%A7%E7%94%9F%E6%84%8F.md)
  - 未获取到文章正文：解析 `live-streaming-2.html` 失败，返回数据为空，无法总结；请提供正文或可访问链接。
  - Tags: #read

- (2026-11-17) [直播观察（一）：平台怎么把打赏做成大生意](202611/2026-11-17-%E7%9B%B4%E6%92%AD%E8%A7%82%E5%AF%9F%EF%BC%88%E4%B8%80%EF%BC%89%EF%BC%9A%E5%B9%B3%E5%8F%B0%E6%80%8E%E4%B9%88%E6%8A%8A%E6%89%93%E8%B5%8F%E5%81%9A%E6%88%90%E5%A4%A7%E7%94%9F%E6%84%8F.md)
  - 该信息说明抓取失败：系统误将文件名当作域名解析，未获取文章正文；可能因链接不完整、失效、需登录或被反爬拦截。需提供完整URL或粘贴正文后再总结。
  - Tags: #read

- (2026-11-17) [使用形式化方法找出网络模型中的竞态问题](202611/2026-11-17-%E4%BD%BF%E7%94%A8%E5%BD%A2%E5%BC%8F%E5%8C%96%E6%96%B9%E6%B3%95%E6%89%BE%E5%87%BA%E7%BD%91%E7%BB%9C%E6%A8%A1%E5%9E%8B%E4%B8%AD%E7%9A%84%E7%AB%9E%E6%80%81%E9%97%AE%E9%A2%98.md)
  - 作者用Quint对DeskFleet异步竞态建模，以抽象拆分和最小基数验证，发现Promise缓存锁死与all提前reject竞态并修复；认为形式化可提前证伪异步设计死角，AI显著降低门槛。
  - Tags: #read #guide

- (2026-11-16) [Introducing the World's Strongest Sokoban Solver](202611/2026-11-16-introducing-the-world%27s-strongest-sokoban-solver.md)
  - 文章称AI代理14天造出Soksolv，在两大基准上解出最多且最快，含24个世界首次；技术靠推搜索、双向搜索、FESS、多车道等组合，方法论为代理爬山实验，但需人类强引导。
  - Tags: #read #agent #deepdive

- (2026-11-13) [AI 的知识诅咒与多 Agent 协作 | 虹线](202611/2026-11-13-ai-%E7%9A%84%E7%9F%A5%E8%AF%86%E8%AF%85%E5%92%92%E4%B8%8E%E5%A4%9A-agent-%E5%8D%8F%E4%BD%9C-%E8%99%B9%E7%BA%BF.md)
  - 文章区分收敛与发散任务：收敛任务单 Agent 更优；发散任务中，多 Agent 靠上下文隔离、独立记忆与各自目标制造持续分歧，逼出意外答案，并认为模仿人类组织是通往 AGI 的务实路径。
  - Tags: #read #agent

- (2026-11-03) [新型谷子：在光盘上烧刻肉眼可见的插画教程 - 少数派](202611/2026-11-03-%E6%96%B0%E5%9E%8B%E8%B0%B7%E5%AD%90%EF%BC%9A%E5%9C%A8%E5%85%89%E7%9B%98%E4%B8%8A%E7%83%A7%E5%88%BB%E8%82%89%E7%9C%BC%E5%8F%AF%E8%A7%81%E7%9A%84%E6%8F%92%E7%94%BB%E6%95%99%E7%A8%8B---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 文章介绍用普通刻录光驱和空白盘烧制可见插画的DIY，核心是Disc Image Studio图像编码，难点在盘片参数标定；教程给出选盘、粗调精调和常见问题，适合愿折腾者。
  - Tags: #read

- (2026-10-29) [You can just ask AI to do things](202610/2026-10-29-you-can-just-ask-ai-to-do-things.md)
  - 核心观点：使用AI的关键技能是“能动性”，主动让代理自动化开发、验证、监控等枯燥任务；但消息、设计决策和代码审查仍亲自负责。
  - Tags: #read #agent

- (2026-10-18) [How our vibe coded website looks like a designer made it](202610/2026-10-18-how-our-vibe-coded-website-looks-like-a-designer-made-it.md)
  - 作者用 AI 编码代理做网站，靠先定概念、按强度光谱多次生成并“放飞”、频繁 fork 对比、playground 调参和大量参考迭代，证明编码代理也能做出有个人品味的设计，关键是过程好玩。
  - Tags: #read #design

- (2026-10-18) [Inline rendering with document​.currentScript](202610/2026-10-18-inline-rendering-with-document%E2%80%8B.currentscript.md)
  - 该内容实为422接口报错信息，提示提交数据格式错误、域名“notes”无法解析，不包含文章正文，无法进行文章总结。
  - Tags: #read #frontend

- (2026-10-16) [How to Build Wealth as a Career Person](202610/2026-10-16-how-to-build-wealth-as-a-career-person.md)
  - 文章认为，九到五工作也能致富：先提升职业价值、创造可衡量结果以提高收入；再控制消费、避免生活方式膨胀，把盈余自动投资成资产。让工作资助自由，既做明星球员，也做所有者。
  - Tags: #read #career

## Monthly Archive

- [2026-11](202611/monthly-index.md) (6 entries)
- [2026-10](202610/monthly-index.md) (11 entries)
- [2026-09](202609/monthly-index.md) (18 entries)
- [2026-08](202608/monthly-index.md) (39 entries)
- [2026-07](202607/monthly-index.md) (30 entries)
- [2026-06](202606/monthly-index.md) (33 entries)
- [2026-05](202605/monthly-index.md) (70 entries)
- [2026-04](202604/monthly-index.md) (57 entries)
- [2026-03](202603/monthly-index.md) (70 entries)
- [2026-02](202602/monthly-index.md) (58 entries)
- [2026-01](202601/monthly-index.md) (67 entries)
- [2025-12](202512/monthly-index.md) (68 entries)
- [2025-11](202511/monthly-index.md) (78 entries)
- [2025-10](202510/monthly-index.md) (67 entries)
- [2025-09](202509/monthly-index.md) (40 entries)
- [2025-08](202508/monthly-index.md) (46 entries)
- [2025-07](202507/monthly-index.md) (77 entries)
- [2025-06](202506/monthly-index.md) (75 entries)
- [2025-05](202505/monthly-index.md) (65 entries)
- [2025-04](202504/monthly-index.md) (61 entries)
- [2025-03](202503/monthly-index.md) (49 entries)
- [2025-02](202502/monthly-index.md) (32 entries)
- [2025-01](202501/monthly-index.md) (41 entries)
- [2024-12](202412/monthly-index.md) (45 entries)
- [2024-11](202411/monthly-index.md) (57 entries)
- [2024-10](202410/monthly-index.md) (34 entries)
- [2024-09](202409/monthly-index.md) (46 entries)
- [2024-08](202408/monthly-index.md) (31 entries)
- [2024-07](202407/monthly-index.md) (12 entries)
