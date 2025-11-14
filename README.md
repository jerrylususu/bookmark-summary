# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-11-14) [Needy Programs](202511/2025-11-14-needy-programs.md)
  - 文章批评现代软件从“用户主导”转向“需求化”，通过账户、更新、通知和新功能引导四个层面，揭示应用如何侵占用户注意力。作者主张程序应回归安静、可控的体验，像基础工具一样仅响应指令。
  - Tags: #read

- (2025-11-14) [Nano Banana can be prompt engineered for extremely nuanced AI image generation](202511/2025-11-14-nano-banana-can-be-prompt-engineered-for-extremely-nuanced-ai-image-generation.md)
  - Google推出的Nano Banana图像生成模型基于自回归技术，能精确遵循复杂提示并生成高质量图像，如处理荒诞请求和多指令编辑。模型优势包括强大的文本理解和免费使用，但存在风格转换弱、渲染文字出错及生成速度慢等局限。
  - Tags: #read #llm #guide

- (2025-11-13) [The Software Engineer’s Guidebook: a recap](202511/2025-11-13-the-software-engineer%E2%80%99s-guidebook-a-recap.md)
  - 《软件工程师指南》作者分享自出版经验：书籍基于Uber管理实践，因与传统出版社合作不顺转为自出版，通过多平台销售两年收入61万美元。自出版收益更高但需自主承担全流程，技术书籍需平衡时效性与普适性。该书成功推动行业交流，并激励技术人写作。
  - Tags: #read #deepdive

- (2025-11-13) [Scaling HNSWs - <antirez>](202511/2025-11-13-scaling-hnsws---antirez.md)
  - Redis 创始人 antirez 总结了在 Redis 中实现 HNSW 的经验，基于低延迟需求介绍了内存优化（如 8 位量化）、并发操作支持、删除节点处理、多进程扩展、快速加载、JSON 过滤等优化措施。通过优化，Redis 的 HNSW 实现了高吞吐和良好伸缩性，适用于大规模向量检索场景。
  - Tags: #read #deepdive

- (2025-11-13) [Vibe hacking a padding oracle](202511/2025-11-13-vibe-hacking-a-padding-oracle.md)
  - 这篇文章记录作者在CTF挑战中利用编码绕过、填充预言机和SQL注入等漏洞攻破一个加密粘贴板服务，成功获取四个Flag的过程。挑战暴露了错误信息泄露、加密实现缺陷及数据库安全问题，凸显了漏洞链的危害。
  - Tags: #read #security

- (2025-11-13) [Parsing integers in C](202511/2025-11-13-parsing-integers-in-c.md)
  - C语言标准库的整数解析函数如atoi和strtol存在错误处理不严、易溢出等问题。curl项目为增强安全性实现了自定义解析函数，严格处理溢出和输入格式，并已全面替换标准库函数。
  - Tags: #read #c

- (2025-11-13) [Agentic Pelican on a Bicycle](202511/2025-11-13-agentic-pelican-on-a-bicycle.md)
  - 通过智能体迭代测试六款多模态模型生成“鹈鹕骑自行车”SVG的能力，发现部分模型能自我改进细节，但整体构图变化有限。实验揭示了模型在视觉评估与创意任务中的能力差异，强调了迭代方法对测试自主改进潜力的价值。
  - Tags: #read #llm

- (2025-11-13) [A quote from Steve Krouse](202511/2025-11-13-a-quote-from-steve-krouse.md)
  - MCP协议利用LLM动态推理机制，实现快速迭代且无需担心兼容性问题，相比传统API具有更高灵活性和开发效率。
  - Tags: #read #llm

- (2025-11-12) [Giving your AI a Job Interview](202511/2025-11-12-giving-your-ai-a-job-interview.md)
  - 基准测试易失真且忽略软技能评价，建议个人用户结合直观任务测试，企业用户需通过专家设计的场景化"AI面试"进行能力评估。
  - Tags: #read #llm

- (2025-11-11) [Reflections on My Tech Career – Part 2](202511/2025-11-11-reflections-on-my-tech-career-%E2%80%93-part-2.md)
  - 作者回顾了在多家科技公司的职业生涯，强调技术贡献与职业选择。他参与多款游戏开发与优化，通过自学解决难题，但反思因忠诚或管理问题停留过久。建议持续学习、平衡生活，并利用跳槽提升薪酬。最终因个人原因退休，专注爱好。
  - Tags: #read #people #deepdive

## Monthly Archive

- [2025-11](202511/monthly-index.md) (40 entries)
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
