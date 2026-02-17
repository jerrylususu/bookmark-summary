# LLM-generated skills work, if you generate them afterwards
- URL: https://www.seangoedecke.com/generate-skills-afterwards/
- Added At: 2026-02-17 14:10:12
- Tags: #read #llm

## TL;DR
本文探讨了LLM生成技能的有效性，指出任务前生成技能无益，而任务后生成技能能有效提炼解决问题过程中获得的知识，从而提升新任务表现。

## Summary
本文讨论了LLM生成技能（skills）的有效性。作者指出，近期研究显示，让LLM在任务开始前生成技能并无益处，因为这类似于“先制定计划”的策略，而当前的推理模型本身已具备任务前思考的能力。相反，作者主张应在LLM完成任务后再让其生成技能。这样，技能可以总结LLM在解决问题过程中迭代获得的知识，而非其训练数据中已有的知识。作者以自己使用Codex模型处理SAE（稀疏自编码器）任务为例，说明在成功解决问题后生成的技能能有效应用于新任务，而提前生成的技能则可能包含错误假设。因此，关键在于让LLM在解决实际问题后进行知识提炼，而非预先生成技能。
