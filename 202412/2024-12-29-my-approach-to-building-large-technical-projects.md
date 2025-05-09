# My Approach to Building Large Technical Projects
- URL: https://mitchellh.com/writing/building-large-technical-projects
- Added At: 2024-12-29 08:36:48
- [Link To Text](2024-12-29-my-approach-to-building-large-technical-projects_raw.md)

## TL;DR
文章总结了启动和推进大型技术项目的策略，强调将大任务分解为小任务以保持动力，通过早期成果和自动化测试验证进展，并尽快达到演示阶段。作者建议在个人项目中优先构建所需功能，并尽早使用自己的软件，以发现和解决问题。整个过程注重实际成果和持续迭代，以保持动力和推进项目进展。

## Summary
1. **项目启动**：
   - **挑战**：启动大型技术项目时，确定如何开始是最困难的部分，可能会花费数小时甚至数天时间。
   - **策略**：将大型任务分解为可看到实际进展的小任务，以保持动力和兴奋感。
   - **示例**：在终端模拟器项目中，初始阶段选择了一些可以快速看到结果的子项目，如VT解析、空白窗口渲染和子进程启动。

2. **早期成果**：
   - **挑战**：早期工作往往不可见，难以看到实际成果。
   - **工具**：自动化测试（通常是单元测试）是克服这一阶段的最佳工具，可以运行代码并验证其工作。
   - **示例**：在终端模拟器项目中，选择从VT解析开始，因为它易于测试，并且可以通过测试的通过数量看到进展。

3. **冲刺到演示**：
   - **目标**：早期子项目的目标是构建一个“足够好”的子组件，以便继续前进到下一个任务，最终达到演示阶段。
   - **策略**：不要追求完美，不要让未来的改进阻碍当前进展，目标是尽快达到演示阶段。
   - **示例**：在终端模拟器项目中，通过构建一个CLI作为第一个“UI”，可以运行简单程序并看到解析器的工作情况，从而保持动力。

4. **为自己构建**：
   - **适用性**：这一部分更适用于个人项目，而不是工作分配的项目。
   - **策略**：只构建你需要的功能，并尽快采用自己的软件。
   - **示例**：在终端模拟器项目中，首先实现了加载shell配置和使用Neovim的功能，然后开始将其作为日常驱动程序使用，发现并修复了一些问题。

5. **打包总结**：
   - **步骤**：
     1. 将大问题分解为小问题，每个小问题都有明确的成果展示方式。
     2. 只解决小问题到足以推进大问题的演示阶段，然后继续下一个问题。
     3. 只解决足够多的小问题以开始构建可运行的演示，然后继续迭代更多功能。
     4. 优先考虑能够让你采用自己软件的功能（如果是个人项目或解决实际问题的项目）。
     5. 根据需要返回并迭代每个组件，重复此过程。

6. **结论**：
   - **个人过程**：这是一个非常个人化的过程，每个人都需要找到一种方法来以健康的方式增强动力。
   - **动机**：看到结果对作者有很强的激励作用，因此围绕这一点构建了工作风格，并且效果良好。
   - **未提及的内容**：作者没有讨论发布、工具（如Git工作流、CI等），因为这些对长期激励作用不大。
