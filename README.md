# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-10-09) [是的，而且……](202610/2026-10-09-%E6%98%AF%E7%9A%84%EF%BC%8C%E8%80%8C%E4%B8%94%E2%80%A6%E2%80%A6.md)
  - 作者结论：AI时代编程仍值得学，但必须亲手写代码以读懂代码、控制复杂度；AI可作助教，还要提升沟通、业务、架构能力。就业低潮是暂时的，可用私人关系求职。
  - Tags: #read

- (2026-10-08) [Anti-Patterns in Software Blogging](202610/2026-10-08-anti-patterns-in-software-blogging.md)
  - 文章归纳开发者写博客的常见反模式：开头冗长、高估读者背景、滥用链接、续集依赖、语气过度正式、移动端与字体对比度失误；建议直接给出阅读理由、少设知识门槛、保证独立可读、自然表达并做好排版。
  - Tags: #read #guide

- (2026-10-07) [How to read code](202610/2026-10-07-how-to-read-code.md)
  - 文章认为读代码不能像读书按序读，应借鉴数学论文多轮分层扫描：先追关键路径建流程，再细看并最后通读，聚焦目标；AI不能替代读代码，LLM输出也须审查。
  - Tags: #read #guide

- (2026-10-06) [What is Codemode](202610/2026-10-06-what-is-codemode.md)
  - Armin Ronacher 介绍 Pi 1.0 的 Codemode：让 LLM 在 harness 侧用代码编排工具调用，而非把工具输出塞进上下文，从而支持组合、并发与状态暂存。作者认为这是 MCP 的自然归宿。
  - Tags: #read #agent

- (2026-10-04) [Shipping is the foundation](202610/2026-10-04-shipping-is-the-foundation.md)
  - 文章认为，工程师的会议、设计、拆解、带队等技能都建立在能独立交付上线这一基础上。不能把事推到上线会导致协调成本增加与空转，人工智能也无法完全替代。
  - Tags: #read #career

- (2026-09-29) [Using multiple git remotes for true distributed version control](202609/2026-09-29-using-multiple-git-remotes-for-true-distributed-version-control.md)
  - 文章主张充分利用 Git 多远程，把代码同时托管到多个平台：为一个远程添加多个推送 URL，一次推送即可镜像到 GitHub、GitLab 等，提升可用性、协作者自由和无痛迁移，但需注意 CI 重复与强制推送风险。
  - Tags: #read #git

- (2026-09-28) [2026 in LLMs (so far)](202609/2026-09-28-2026-in-llms-%28so-far%29.md)
  - 文章回顾2026年前九月LLM进展：编码智能体跨过日常可用临界点，催生Claw与个人智能体、安全焦虑、开源追赶和Token成本反转，并重塑工程师职业，LLM写代码已不可否认。
  - Tags: #read #llm

- (2026-09-22) [Writing Rust code that's faster than state-of-the-art libraries by asking agents to make the code faster](202609/2026-09-22-writing-rust-code-that%27s-faster-than-state-of-the-art-libraries-by-asking-agents-to-make-the-code-faster.md)
  - 用AI智能体迭代优化Rust代码，核心是把模糊目标转为可量化基准与约束，配以防作弊、质量验证、多轮迭代等手段，可在多领域超越现有库，但结果仍需人工验证。
  - Tags: #read #agent #deepdive

- (2026-09-22) [Defensive Driving For Your Career](202609/2026-09-22-defensive-driving-for-your-career.md)
  - 职场回报不自动公平，个人需主动展示功劳、纠正歪曲、防嫉妒、保持筹码；领导应建公平评估制度，使员工无需防御。
  - Tags: #read #career

- (2026-09-17) [You can run git on object storage if you re-make packfiles | Tigris Object Storage](202609/2026-09-17-you-can-run-git-on-object-storage-if-you-re-make-packfiles-tigris-object-storage.md)
  - 作者在 Tigris 上实现 Git 服务器 objgit，重设面向对象存储的 packfile，用 bin/cue 索引支持精确 Range 读取，性能大增；但项目仍早期，缺认证授权。
  - Tags: #read #git #deepdive

## Monthly Archive

- [2026-10](202610/monthly-index.md) (5 entries)
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
