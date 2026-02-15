# Two different tricks for fast LLM inference
- URL: https://www.seangoedecke.com/fast-llm-inference/
- Added At: 2026-02-15 03:29:05
- Tags: #read #llm

## TL;DR
文章对比了Anthropic与OpenAI的“快速模式”技术路径：Anthropic通过降低批处理大小提升单个用户速度，但成本增加；OpenAI则借助Cerebras硬件与模型蒸馏实现超低延迟。作者认为OpenAI方案更具突破性，但指出快速推理可能并非主流需求，因准确性常优先于速度。

## Summary
文章分析了Anthropic和OpenAI推出的“快速模式”在LLM推理加速上的两种不同技术路径。Anthropic的快速模式通过降低批处理大小（low-batch-size）来减少用户等待时间，从而提升单个用户的吞吐量，但其代价是整体GPU吞吐量下降和成本增加，且模型本身（Opus 4.6）保持不变。相比之下，OpenAI的快速模式基于与Cerebras的合作，使用其巨型芯片（Wafer Scale Engine）来实现超低延迟推理。Cerebras芯片拥有巨大的片内SRAM（44GB），足以容纳较小的模型，因此OpenAI发布了一个名为GPT-5.3-Codex-Spark的蒸馏模型，该模型参数更少、能力稍弱，但推理速度极快（提升15倍）。

作者认为，OpenAI的技术方案更具突破性，因为它涉及硬件创新和模型蒸馏；而Anthropic的方案更像是一种战术性应对，旨在快速响应市场竞争。文章进一步指出，快速推理可能并非AI实验室的首要目标，因为对于许多应用（如AI代理）而言，模型的准确性比速度更重要，速度提升往往以牺牲一定准确性为代价。目前，快速推理更可能作为底层组件，用于特定场景（如Claude Code中使用Haiku模型），而非成为主流需求。
