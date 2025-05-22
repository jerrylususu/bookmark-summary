# How ChatGPT Remembers You: A Deep Dive into Its Memory and Chat History Features ·  Embrace The Red
- URL: https://embracethered.com/blog/posts/2025/chatgpt-how-does-chat-history-memory-preferences-work/
- Added At: 2025-05-22 13:46:04
- [Link To Text](2025-05-22-how-chatgpt-remembers-you-a-deep-dive-into-its-memory-and-chat-history-features-·-embrace-the-red_raw.md)

## TL;DR


ChatGPT通过六大系统模块整合用户数据实现记忆功能：手动保存的bio信息、对话偏好、历史主题、用户画像、近期对话及交互元数据，但存在系统幻觉、隐私风险及提示注入漏洞。新增功能依赖用户画像和短期记录实现个性化回复，却无法让用户直接查看或删除数据，可能引发结果偏差。研究建议增强透明度以符合隐私法规，并推动开发多档案安全机制。

## Summary


文章介绍了ChatGPT的两种记忆功能：参考保存的用户自定义记忆（bio工具）和新增的“聊天历史”特征。系统通过扩展的系统提示词（System Prompt）整合用户数据，分为六大模块影响回复：

1. **Model Set Context**：记录用户手动保存的生物（bio）信息及时间戳，但存在系统幻觉问题，可能将其他部分数据误作为记忆项。例如实验账户显示含3次“记忆清除事件”，但实际并不存在该功能。

2. **Assistant Response Preferences**：基于历史对话生成用户偏好模式，如要求结构化输出格式（XML/JSON）、技术安全研究倾向等。每个条目带有“Confidence=high”标记，推测会影响模型推理方向。

3. **Notable Past Conversation Topics**：存储早期重要对话主题，例如用户曾测试AI漏洞或频繁使用编程语言进行安全研究等，置信度始终最高。测试账户显示需持续对话才能积累此类条目。

4. **Helpful User Insights**：自动总结用户个人信息（姓名、地理位置、职业），包含用户未直接提供但被推断的信息。测试账户若使用较少，则显示“Nothing yet”。

5. **Recent Conversation Content**：保存约40条最近对话记录，包含对话起始时间、摘要及用户输入内容（不含模型回复）。具体如某次对话用户询问西雅图天气和波特兰情况，仅保留用户原始提问。系统提示词中明确只存储用户输入的原始消息。

6. **User Interaction Metadata**：追踪用户设备信息（屏幕尺寸、用户代理）、使用习惯（对话深度、活跃周期）、当前环境（时区、深色模式）等。其中显示ChatGPT使用意图标签（intent_tags）分类对话，如最近8条消息被标记为“摘要生成”。

新增功能未使用全文检索或RAG技术，而是通过构建用户画像和短期历史记录来实现个性化。用户无法直接查看或修改系统记录的数据，导致回复结果可能因个人历史不同产生差异。作者指出这一设计存在隐私风险，建议增加透明度及删除机制，以符合GDPR等法规要求。研究通过对比不同账户对话数据完成，但受限于模型幻觉特性，部分内容可能存在偏差。

系统中存在提示注入漏洞：可通过间接方式触发对特定记忆模块的访问，或利用metadata中“意图标签”控制回复方向。例如在“Recent Conversation Content”摘要部分插入恶意指令，或篡改用户代理字符串改变输出风格。这些安全问题可能推动OpenAI开发用户分层配置（如多档案或项目隔离功能）。
