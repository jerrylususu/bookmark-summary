# Guest Post: How I Scanned all of GitHub’s “Oops Commits” for Leaked Secrets ◆ Truffle Security Co.
- URL: https://trufflesecurity.com/blog/guest-post-how-i-scanned-all-of-github-s-oops-commits-for-leaked-secrets
- Added At: 2026-01-31 14:59:45
- Tags: #read #deepdive #security

## TL;DR
本文介绍了如何扫描GitHub上因强制推送删除的提交（Oops Commits）以发现泄露的秘密。作者开发了开源工具Force Push Scanner，通过分析GitHub Archive数据，成功检测出价值约25,000美元的漏洞赏金秘密，强调秘密一旦提交就必须立即撤销，并呼吁开发者提高安全意识。

## Summary
本文探讨了如何扫描GitHub上因强制推送而被删除的提交（称为“Oops Commits”），以发现泄露的秘密。作者Sharon Brizinov与Truffle Security合作，开发了开源工具Force Push Scanner，通过分析GitHub Archive中的事件数据，识别并扫描这些隐藏提交，共发现价值约25,000美元的漏洞赏金秘密。

**技术背景**：GitHub不会真正删除提交，即使是强制推送后，提交仍可通过完整或部分哈希访问。GitHub Archive项目记录了所有公共事件，包括PushEvents，其中零提交的事件表示强制推送导致的删除。

**扫描方法**：利用GitHub Event API和GH Archive数据，筛选出零提交的PushEvents，提取“before”哈希值，然后使用TruffleHog工具扫描这些提交的内容，寻找活跃秘密。开源工具Force Push Scanner自动化了此过程，支持扫描特定组织或用户的提交。

**秘密发现**：扫描结果显示，大量秘密被泄露，常见类型包括MongoDB凭证、GitHub个人访问令牌（PAT）和AWS密钥。泄露文件以.env、index.js等配置文件和脚本为主。通过手动筛选和自动化工具，作者识别出高价值目标，其中企业邮箱相关的提交更易产生重大影响。

**案例研究**：具体示例中，一个泄露的GitHub PAT拥有对Istio项目所有仓库的管理员权限，可能导致大规模供应链攻击，但通过及时报告得以避免。

**结论**：研究强调，一旦秘密被提交到GitHub，即使删除也应视为已泄露，必须立即撤销。这呼吁开发者提高安全意识，并利用工具检查潜在风险。
