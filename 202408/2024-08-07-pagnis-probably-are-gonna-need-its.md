# PAGNIs: Probably Are Gonna Need Its
- URL: https://simonwillison.net/2021/Jul/1/pagnis/
- Added At: 2024-08-07 14:48:38

## TL;DR
文章讨论了YAGNI原则及其例外，介绍了PAGNIs概念，强调了移动应用kill-switch、自动化部署、持续集成与测试框架、API分页和详细日志的重要性，并推荐了Django SQL Dashboard等工具，指出这些实践虽初期成本高，但长远回报显著。

## Summary
1. **YAGNI原则**：YAGNI原则指出不应仅因为未来可能有用就添加功能，只有在解决直接问题时才应编写代码。

2. **YAGNI例外**：Luke Page列出了一些YAGNI的例外情况，如日志记录、API版本控制、created_at时间戳以及倾向于“为用户存储多个X”（多对多关系）。

3. **PAGNIs概念**：提出PAGNIs（Probably Are Gonna Need Its）概念，指那些虽然当前不需要但未来很可能需要的功能。

4. **移动应用的kill-switch**：
   - **定义**：确保移动应用有一个kill-switch机制，可以在应用启动时显示“必须升级才能继续使用”的屏幕。
   - **必要性**：在发现安全漏洞或需要停止维护旧版本API时，kill-switch是必要的。
   - **实现**：Firebase提供此功能给许多Android应用，iOS应用需要自行实现。

5. **自动化部署**：
   - **好处**：避免在六个月后回到项目时忘记如何部署。
   - **工具**：使用GitHub Actions和云服务提供商如Google Cloud Run、Vercel、Heroku和Netlify，设置自动化部署变得更容易。

6. **持续集成与测试框架**：
   - **好处**：GitHub Actions等工具使设置持续集成更简单。
   - **测试框架**：在项目初期引入测试框架容易，且能从第一天起就设定测试代码的先例。
   - **工具**：推荐使用pytest，并提供各种cookiecutter模板来配置新项目。

7. **API分页**：
   - **原则**：永远不要构建不分页的API端点。
   - **实现**：即使只返回单页结果，也应包含分页信息。

8. **详细API日志**：
   - **好处**：提供详细的日志记录，包括API的POST体，对调试和重放API流量非常有用。
   - **实现**：使用Django视图装饰器将日志直接记录到PostgreSQL表中。

9. **可书签化的只读SQL查询接口**：
   - **好处**：使用书签化的SQL查询来指导新功能的实现，极大地提高生产力。
   - **工具**：Django SQL Dashboard提供此功能给Django+PostgreSQL项目。

10. **降低实施成本**：
    - **经验积累**：随着经验的积累和工具的增多，实施这些功能的成本会显著降低。
    - **投资回报**：尽管初期实施可能看似昂贵，但长远来看，这些投资会多次回报。
