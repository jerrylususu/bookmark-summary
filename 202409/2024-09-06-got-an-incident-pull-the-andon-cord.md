# Got an incident? pull the Andon Cord
- URL: https://spike.sh/blog/pull-the-andon-cord/
- Added At: 2024-09-06 13:38:59
- [Link To Text](2024-09-06-got-an-incident?-pull-the-andon-cord_raw.md)

## TL;DR
Andon Cord是丰田引入的生产管理方法，通过在装配线上安装拉绳系统，员工发现缺陷时可立即停止生产线，与经理共同解决问题。这种方法不仅提高了生产质量，还降低了成本，并被亚马逊和Netflix等公司借鉴应用于客户服务和软件开发中。

## Summary
1. **背景介绍**：
   - **Andon Cord的引入**：Andon Cord是丰田在20世纪初引入的一种生产管理方法，由工业工程师Taiichi Ohno提出，旨在提高生产质量和效率。
   - **生产成本高昂**：在1984年，每分钟的停工成本高达15,000美元，相当于今天的42,758美元，任何生产问题都会导致巨大损失。

2. **问题描述**：
   - **生产缺陷**：在装配线上，如果员工发现缺陷，需要时间修复，这不仅影响生产效率，还可能导致低质量产品。
   - **临时解决方案**：员工可能采取临时措施（如monkeypatching），这会导致产品质量下降和生产成本增加。

3. **解决方案**：
   - **Andon Cord的实施**：在装配线上安装一根长绳，员工发现缺陷时拉绳，触发警报并停止整个生产线，经理与员工一起解决问题或进行进一步检查。
   - **简单有效**：每次员工发现问题时，只需拉绳，这种方法看似极端，但对丰田非常有效。

4. **成功因素**：
   - **鼓励拉绳**：每个员工都被鼓励拉绳，不拉绳意味着妥协质量和增加成本。
   - **文化塑造**：当员工拉绳时，经理会感谢员工，强调任何缺陷都不能忽视，并表示员工的努力受到CEO的赞赏，这种行为逐渐演变为“安全文化”。
   - **即时解决**：重点在于立即解决问题，无需繁琐的官僚程序，经理会问“我如何帮助你？”
   - **持续学习**：将失败视为学习机会，通过快速学习和改进，提高质量并降低生产成本。

5. **现代应用**：
   - **亚马逊**：引入客户服务Andon Cord，当发现客户多付费用时，系统会扫描并解决问题，视其为缺陷。
   - **Netflix**：鼓励失败并从中学习，使用混沌工程原则随机关闭生产服务器，开发者计划并防止错误。

6. **软件环境中的应用**：
   - **借鉴丰田原则**：在工程中引入事件管理，鼓励团队设置和接收警报，建立无责文化，立即解决问题，并从事件中学习。
   - **团队会议**：安排团队会议，鼓励团队设置警报，感谢同事创建事件或设置集成，立即解决问题，并记录解决方案以供未来参考。

7. **推荐阅读**：
   - **《The DevOps Handbook》**：作者Gene Kim, Jez Humble, Patrick Debios, 和 John Willis，推荐给工程团队的每个人阅读。