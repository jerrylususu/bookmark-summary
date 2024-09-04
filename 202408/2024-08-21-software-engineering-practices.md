# Software engineering practices
- URL: https://simonwillison.net/2022/Oct/1/software-engineering-practices/
- Added At: 2024-08-21 15:04:46
- [Link To Text](2024-08-21-software-engineering-practices_raw.md)

## TL;DR
文章讨论了软件工程实践中的一些推荐做法，包括代码与文档同库、创建测试数据的机制、可靠的数据库迁移、新项目和组件的模板、自动化代码格式化、新开发环境的测试自动化流程以及自动化预览环境。这些实践旨在提高生产力和审查质量，虽然需要前期投资，但长远来看将带来多次回报。

## Summary
1. **软件工程实践推荐**：
   - **日期**：2022年10月1日
   - **来源**：Gergely Orosz在Twitter上发起了一场关于开发团队推荐“软件工程实践”的对话。

2. **对“最佳实践”一词的看法**：
   - 作者不喜欢“最佳实践”这一术语，认为它具有规定性和误导性。

3. **详细推荐的软件工程实践**：
   - **代码与文档同库**：
     - 重要性在于信任，确保文档存在且更新及时。
     - 将文档放在代码仓库中，便于代码审查时强制更新文档。
     - 实现版本化文档，便于查阅不同版本的文档。
     - 将文档与自动化测试结合，确保文档的准确性。
   - **创建测试数据的机制**：
     - 提供工具导入生产数据到本地环境，但需注意隐私和安全问题。
     - 建立生成测试数据的系统，覆盖各种场景，便于工程师复现问题。
   - **可靠的数据库迁移**：
     - 投资于版本控制的数据库迁移机制，确保生产环境无停机时间。
     - 使用Django的迁移系统，或尽可能复制其方法。
     - 设计无停机时间的架构变更流程。
   - **新项目和组件的模板**：
     - 提供良好的模板，确保新项目和组件以正确的方式创建。
     - 使用工具如cookiecutter或GitHub模板仓库。
     - 定期维护和更新模板。
   - **自动化代码格式化**：
     - 选择适合语言的代码格式化工具，如Black或Prettier，并在CI流程中运行检查模式。
     - 避免代码格式化争议，提高个人和团队的效率。
   - **新开发环境的测试自动化流程**：
     - 解决初始开发环境设置的痛点，提供文档化或自动化流程。
     - 推荐使用云端开发环境，如Gitpod或Codespaces。
   - **自动化预览环境**：
     - 提供与PR直接链接的自动化预览环境，便于审查变更。
     - 使用平台如Vercel、Netlify、Render或Heroku的功能，或自建系统。

4. **总结**：
   - 这些实践需要前期投资，但通过提高生产力和审查质量，将带来多次回报。