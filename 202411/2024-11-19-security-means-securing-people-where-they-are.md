# Security means securing people where they are
- URL: https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are
- Added At: 2024-11-19 17:10:05
- [Link To Text](2024-11-19-security-means-securing-people-where-they-are_raw.md)

## TL;DR
文章讨论了PyPI实施PEP 740和Trusted Publishing引发的争议，强调了大规模安全的重要性，即在用户所在的地方保障他们。文章分析了用户对GitHub认证的担忧，如不公平社会压力和供应商偏见，并解释了多供应商支持和开放标准的实施。最终，文章主张实用主义，建议首先支持能最大程度受益的服务，同时不排除对其他服务的支持。

## Summary
1. **引言**：
   - **背景**：作者受Seth Larson的鼓励，针对PEP 740及其在PyPI上的实施引发的广泛讨论，撰写此文。
   - **核心观点**：大规模安全意味着在用户所在的地方保障他们，即决定如何分配有限的工程资源，使最大用户群体受益。

2. **用户反馈**：
   - **担忧类型**：
     - **不公平社会压力**：来自大型IdP（如GitHub）的认证会导致在自有基础设施上做得好的项目受到不公平压力。
     - **供应商偏见**：先支持GitHub认证被视为加深对GitHub依赖的策略。
     - **认证的负面看法**：有人认为认证是坏的，应继续容忍长期使用的PGP签名密钥。
     - **阴谋论**：认为PyPI被微软/NSA/Unit 8200控制，开发认证是为了完成今年的邪恶计划。

3. **事实基础**：
   - **多供应商支持**：Trusted Publishing最初仅支持GitHub，但后来增加了GitLab、Google Cloud、ActiveState等。
   - **开放标准**：Trusted Publishing和PEP 740基于OpenID Connect，允许独立服务通过公钥加密进行联邦。
   - **新供应商的复杂性**：添加新Trusted Publisher需要审查，确保IdP能区分用户，防止用户间冒充。
   - **不适用所有场景**：OIDC受益于规模，不适合每个维护者都运行自己的OIDC IdP。
   - **信任未增加**：Trusted Publishing和PEP 740减少了对CI/CD提供商的不必要信任，强制其公开可审计和验证的声明。

4. **策略选择**：
   - **GitHub优先**：GitHub用户群体最大，首先支持GitHub是为了最大化立即受益的用户。
   - **非阴谋论**：选择GitHub并非阴谋，而是基于实际用户分布的战略决策。

5. **用户安全意识**：
   - **用户不需成为安全专家**：大多数开源维护者不是安全专家，他们希望在不成为安全专家的情况下实现目标。
   - **安全是过渡性问题**：安全是一个在实现实际目标时需要克服的障碍。

6. **缓解策略**：
   - **将安全功能转化为可用性功能**：如Trusted Publishing的设计，消除用户在PyPI和CI/CD之间的切换，同时提高安全性。
   - **委托安全责任**：大型服务有资源和动机维持强大的默认安全姿态，并跟上最新的安全变化。

7. **GitHub的主导地位**：
   - **当前聚集地**：GitHub是当前开源项目的主要聚集地，绝大多数项目集中在GitHub上。
   - **数据支持**：84.7%的Python包在元数据中列出了GitHub URL。

8. **结论**：
   - **实用主义**：新功能应首先与能最大程度立即受益的服务（如GitHub）交互。
   - **不排除其他服务**：PyPI应继续增加对其他服务的支持，如独立GitLab主机或Codeberg实例。

9. **未来工作**：
   - **支持更多认证来源**：如支持电子邮件身份认证，继续增加Trusted Publishing提供商。
   - **解决社会压力**：通过扩大支持范围，解决因认证特性导致的社会压力问题。
