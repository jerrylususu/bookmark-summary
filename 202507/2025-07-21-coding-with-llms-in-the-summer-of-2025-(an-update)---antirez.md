# Coding with LLMs in the summer of 2025 (an update) - <antirez>
- URL: https://antirez.com/news/154
- Added At: 2025-07-21 13:34:51
- [Link To Text](2025-07-21-coding-with-llms-in-the-summer-of-2025-(an-update)---antirez_raw.md)

## TL;DR


2025年，前沿LLM（如Gemini 2.5 PRO、Claude Opus 4）成为程序员人机协作的核心工具。通过提供完整代码上下文与技术文档、直接调用顶尖模型优化核心功能，开发者可高效提升编码效率。其优势体现在代码审查、逻辑推理、快速验证及跨领域辅助，但需人类主导设计决策，动态切换模型填补知识缺口。最佳实践需平衡AI辅助与自主编写，规避过度依赖风险，在可控协作中突破技术边界。

## Summary


前沿LLM（如Gemini 2.5 PRO、Claude Opus 4）在2025年已成为程序员的重要工具，通过高效协作显著提升开发能力。关键创新点包括优化代码审查、快速验证方案可行性、人机混合设计、代码片段撰写、跨领域技术扩展。

核心观点：
- LLM当前无法独立完成复杂编码任务，需通过人机协作最大化价值。
- 人类需具备清晰表达问题与有效沟通的能力，才能精准引导LLM减少失误。
- 直接控制LLM的交互过程是当前高质量开发的必经路径。

关键实践：
1. 避免让LLM独立处理非简单任务。例如Vector Sets的Redis开发中，直接编写代码后再由LLM审查可快速修复漏洞。
2. 提供完整代码上下文与技术文档。包含设计思路、潜在错误点及目标要求，例如将Vector Sets的README加入上下文使LLM像专家般工作。
3. 必须使用大参数尖端模型直接交互。绕过代理或RAG系统，避免局部信息导致性能下降，通过手动切换模型（如Gemini+Claude）拓展设计视野。

推荐模型：
- Gemini 2.5 PRO：擅长深层逻辑分析及复杂问题解决，尤其在代码审查与推理方面更优。
- Claude Opus 4：在代码生成流畅度与辅助效果上表现突出，但需与Gemini互补使用。

实操风险：
- 盲目依赖LLM可能导致重复或低效；完全拒绝则会错失效率提升机遇。
- 需平衡LLM辅助与自主编写：当LLM建议不足时，需切换回手动编码，确保最终代码符合设计目标。

开发效率提升：
- 人类主导设计方向与质量把控，LLM负责加速实现或验证细节。例如用LLM快速生成试验代码评估方案，但最终决策权仍在开发者手中。
- 结合汇编等陌生领域编程，通过LLM补足专业知识缺口，实现技术边界突破。

未来展望：
- 虽然开发者期待AI独立完成任务，但现阶段必须保持主导地位。人机协作不仅能提升速度，还能通过批判性反馈持续学习，形成新的开发模式。
- 强调中道的实践哲学：既不过度沉迷AI代理幻觉，也不因抵触情绪阻碍技术进步，在控制与信任间找到最佳平衡点。
