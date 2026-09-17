# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-09-17) [Migrating the GitHub Copilot runtime to Rust, using Copilot](202609/2026-09-17-migrating-the-github-copilot-runtime-to-rust%2C-using-copilot.md)
  - GitHub 将 Copilot agent runtime 从 TypeScript/Node.js 重写为 Rust，产出超 80 万行代码，多由 AI 编写，分 128 个增量 PR 原子替换完成。一人数月完成原需团队一两年的工程，性能提升数个数量级，并通过 C ABI 与 napi 双入口支撑六个语言 SDK。
  - Tags: #read #deepdive #engineering

- (2026-09-16) [How to get a DOI for your blog posts](202609/2026-09-16-how-to-get-a-doi-for-your-blog-posts.md)
  - 作者介绍为博客文章申请DOI的原因、方法与风险：用Rogue Scholar自动分配，但面临失控、追踪和删除等问题；结论是虽显自恋，却便于学术引用，值得尝试。
  - Tags: #read

- (2026-09-16) [Jev means structured output is interesting again](202609/2026-09-16-jev-means-structured-output-is-interesting-again.md)
  - Jev 是仅输出结构化结果的低延迟系统1模型，可用于实时决策，或成智能计算原语；但其技术门槛不高，普通大模型单令牌推理也能接近，智能上限有限，“免疫幻觉”存疑，价值仍待验证。
  - Tags: #read #llm

- (2026-09-15) [Your Recursion Is Lying to You](202609/2026-09-15-your-recursion-is-lying-to-you.md)
  - 递归没问题，错在假设 JS 运行时支持尾调用优化。尾递归不等于栈安全，深度可能增长时应改用迭代、显式栈或 trampoline，别在生产中依赖 TCO。
  - Tags: #read #js

- (2026-09-15) [We are all Product Engineers now | Seldo.com](202609/2026-09-15-we-are-all-product-engineers-now-seldo.com.md)
  - 文章认为，AI将吃掉编码、审查、维护、部署和运维，软件成本崩塌；真正值钱的是挖掘需求、定义“好”并做得愉悦，即产品工程。初级梯子断裂，我们终将成为产品工程师，喜不喜欢都一样。
  - Tags: #read

- (2026-09-15) [置身 Agent 时代：当软件开始不再需要软件工程师](202609/2026-09-15-%E7%BD%AE%E8%BA%AB-agent-%E6%97%B6%E4%BB%A3%EF%BC%9A%E5%BD%93%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%A7%8B%E4%B8%8D%E5%86%8D%E9%9C%80%E8%A6%81%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md)
  - 文章借两个复杂项目观察：智能体正接管编码、评审、测试与故障排查，人转向产品、成本、体验和责任等关键决策，注意力成瓶颈，经验变风险控制。核心追问：复杂软件还需同样多工程师吗？未来有经验者从何而来？
  - Tags: #read

- (2026-09-13) [Agent harness security and Git](202609/2026-09-13-agent-harness-security-and-git.md)
  - Git 支持仓库内嵌裸仓库，编码代理对只读 Git 命令免审批，攻击者可在不可信仓库埋恶意 config 触发代码执行。多家代理已修复，根本防御是沙箱化代理。
  - Tags: #read #security

- (2026-09-13) [AI is breaking our proxies for expertise](202609/2026-09-13-ai-is-breaking-our-proxies-for-expertise.md)
  - 文章指出，数学与软件等领域的声望依赖代理指标，AI令这些指标廉价可伪造，冲击激励机制。数学需区分解谜与生成想法，未来或形成人机分域；软件工程也须重建评价文化。
  - Tags: #read

- (2026-09-04) [How we make AI coding more cost efficient without sacrificing task quality](202609/2026-09-04-how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality.md)
  - GitHub Copilot通过四项优化降低编码代理成本：选择性压缩噪声、移除行号、精简提示词、直接返回后台任务结果。强调从整体任务完成衡量，局部省token可能引发更多恢复操作。改动均经离线与在线实验验证，核心是移除模型不必要工作。
  - Tags: #read #agent

- (2026-09-04) [What Makes LLM Tokenization Slow?](202609/2026-09-04-what-makes-llm-tokenization-slow.md)
  - 文章通过优化GPT-2分词器发现，性能瓶颈在于海量微小操作而非单步复杂度。采用直接处理字节、利用token ID与排名关系及边界向量后，BPE合并开销大幅下降，正则匹配成为新瓶颈。流式分词与并行化收益有限。
  - Tags: #read #llm

## Monthly Archive

- [2026-09](202609/monthly-index.md) (13 entries)
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
