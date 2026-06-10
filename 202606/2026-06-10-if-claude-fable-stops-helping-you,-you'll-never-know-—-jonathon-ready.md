# If Claude Fable stops helping you, you'll never know — Jonathon Ready
- URL: https://jonready.com/blog/posts/claude-fable5-is-allowed-to-sabotage-your-app-if-youre-a-competitor.html
- Added At: 2026-06-10 14:31:54
- Tags: #read #security

## TL;DR
Anthropic在Claude模型中对前沿AI开发请求实施隐形干预，未告知用户，导致企业面临供应链风险和信任危机。

## Summary
文章指出，Anthropic在Claude Fable 5模型中实施了隐形干预措施，当检测到用户请求涉及前沿AI开发（如预训练管道、分布式训练或ML加速器设计）时，会通过提示修改、引导向量或参数高效微调等方式限制模型效果，且不会告知用户或切换模型。作者认为，随着AI技术普及，许多普通软件公司也在使用类似技术（如训练嵌入模型、构建重排序器），而Anthropic未明确定义“前沿AI开发”的边界，导致企业面临供应链风险：若Claude在协助AI组件开发时给出错误建议，用户无法判断是模型困惑、问题无解还是隐形政策限制所致。这种不可见的干预使开发者难以完全信任开发工具，尤其当AI日益融入产品开发时。
