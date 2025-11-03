# New prompt injection papers: Agents Rule of Two and The Attacker Moves Second
- URL: https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/
- Added At: 2025-11-03 13:44:49
- Tags: #read #llm #security
- [Link To Text](2025-11-03-new-prompt-injection-papers-agents-rule-of-two-and-the-attacker-moves-second_raw.md)

## TL;DR
两篇AI安全论文指出提示注入仍是未解难题：Meta提出“规则二”限制AI代理权限组合以降低风险；多机构研究显示现有防御在自适应攻击下成功率超90%，验证了通过设计而非依赖防御的实用安全思路。

## Summary
这篇文章讨论了两篇关于LLM安全和提示注入攻击的新研究论文。

**第一篇论文：《Agents Rule of Two: A Practical Approach to AI Agent Security》**
- 由Meta AI于2025年10月31日发布，基于作者Simon Willison的“致命三方”概念和Google Chrome团队的“Rule of Two”。
- 提出“规则二”：为避免提示注入的高风险后果，AI代理在一个会话中最多只能同时满足以下三个属性中的两个：
  - [A] 处理不可信输入
  - [B] 访问敏感系统或私有数据
  - [C] 改变状态或外部通信
- 如果必须同时满足所有三个属性，则代理不应自主运行，而需人工监督或可靠验证。
- 作者认为该规则简洁实用，但指出其Venn图中“不可信输入+改变状态”的组合被标记为“安全”可能不准确，因为即使无敏感数据也可能造成危害。

**第二篇论文：《The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections》**
- 由来自OpenAI、Anthropic和Google DeepMind等机构的14位作者于2025年10月10日发表。
- 测试了12种针对提示注入和越狱的防御措施，采用自适应攻击（如梯度下降、强化学习和随机搜索）进行评估。
- 结果：所有防御措施在自适应攻击下成功率均超90%，而人类红队攻击成功率高达100%。静态攻击评估被证明无效。
- 论文强调自适应攻击评估的重要性，并呼吁提高防御标准，但作者对近期开发出可靠防御持悲观态度。

**总结与关联**
- 两篇论文均指出提示注入仍是未解难题，现有防御不可靠。
- 第二篇论文的强攻击结果支持了Meta的“规则二”作为当前构建安全AI代理的实用方案，即通过设计限制风险而非依赖防御。
