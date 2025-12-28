# Using Assisted-by commit footers instead of banning AI tools
- URL: https://xeiaso.net/notes/2025/assisted-by-footer/
- Added At: 2025-11-03 13:42:20
- Tags: #read #llm

## TL;DR
反对全面禁止AI投稿，建议要求贡献者用“Assisted-by”脚注公开使用的AI工具，便于审查与追踪，平衡创新与风险。

## Summary
本文反对完全禁止AI工具的做法，主张采用“辅助者”（Assisted-by）提交脚注作为中间方案。许多项目试图全面禁止AI投稿，但作者认为这不可行，因为用户很容易隐瞒使用情况。更好的方法是像Fedora的AI贡献政策那样，要求贡献者在提交信息中添加脚注，披露所使用的AI工具和模型，例如：
```
Assisted-by: GPT-OSS 120b via OpenAI Codex (locally hosted)
```
这种做法便于自动化检测AI使用，帮助审查者针对性审核，并能长期追踪哪些工具易引发问题，从而优化政策。作者还指出，可引导AI工具默认添加此脚注，提高合规性，避免因完全禁止导致低质量贡献泛滥。作者希望未来允许人们尝试新工具，但通过简单、机器可读的脚注降低风险。文末幽默提到，使用GNU Emacs等工具也可添加脚注，并以自身使用AI编辑文章为例说明。
