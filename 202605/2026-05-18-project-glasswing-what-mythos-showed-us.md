# Project Glasswing: what Mythos showed us
- URL: https://blog.cloudflare.com/cyber-frontier-models/
- Added At: 2026-05-18 14:48:55
- Tags: #read #agent #security

## TL;DR
Cloudflare在Project Glasswing中利用Anthropic的Mythos Preview模型进行安全漏洞研究，该模型能有效构建漏洞利用链并生成验证代码，但存在不一致拒绝行为。Cloudflare构建了多阶段自动化框架提升效率，并强调构建更安全系统架构以缩短漏洞修复时间，计划将这些原则应用于产品以增强客户安全防护。

## Summary
本文介绍了Cloudflare在Project Glasswing中使用Anthropic的Mythos Preview模型进行安全漏洞研究的实践与发现。Mythos Preview在漏洞利用链构建和证明生成方面表现出色，能够将多个低风险漏洞组合成可利用的攻击链，并自动生成验证代码。然而，模型存在不一致的拒绝行为，可能影响合法安全研究，因此需要额外的安全措施。

在漏洞发现过程中，Cloudflare构建了多阶段的自动化漏洞发现框架，包括侦察、狩猎、验证、填补、去重、追踪、反馈和报告等阶段。该框架通过并行化窄任务、对抗性审查和分离问题链等方式，提高了漏洞发现的效率和准确性。

文章指出，单纯追求更快的补丁速度并不足够，关键在于构建更安全的系统架构，使攻击者更难利用漏洞，同时减少漏洞披露与修复之间的时间差。Cloudflare计划将这些原则应用于其产品，为客户提供更强大的安全防护。
