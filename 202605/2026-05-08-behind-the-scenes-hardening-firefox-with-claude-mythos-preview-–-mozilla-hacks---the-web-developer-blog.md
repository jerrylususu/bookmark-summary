# Behind the Scenes Hardening Firefox with Claude Mythos Preview – Mozilla Hacks - the Web developer blog
- URL: https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/
- Added At: 2026-05-08 15:22:59
- Tags: #read #security #agent #llm

## TL;DR
Mozilla利用Claude Mythos Preview等AI模型构建智能代理测试框架，结合模糊测试动态生成可复现用例，在Firefox 150版本中发现271个漏洞（含180个高危），显著提升漏洞检测效率，为软件安全提供新策略。

## Summary
Mozilla利用Claude Mythos Preview等AI模型，通过构建智能代理测试框架，系统性地发现并修复了Firefox中的大量安全漏洞。该框架结合现有模糊测试基础设施，能动态生成可复现的测试用例，显著提升了漏洞检测的准确性和规模。在Firefox 150版本中，AI辅助发现了271个漏洞，其中180个为高危漏洞，涵盖沙箱逃逸、内存破坏等多类问题。Mozilla强调，这种AI驱动的安全加固方法不仅提高了Firefox的安全性，也为其他软件项目提供了可借鉴的防御策略。
