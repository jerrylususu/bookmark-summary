# Preferring throwaway code over design docs
- URL: https://softwaredoug.com/blog/2024/12/14/throwaway-prs-not-design-docs
- Added At: 2024-12-16 15:18:18
- [Link To Text](2024-12-16-preferring-throwaway-code-over-design-docs_raw.md)

## TL;DR
文章探讨了软件开发中设计与代码的关系，强调通过“编码狂欢”发现设计，而非依赖设计文档。提出使用草稿PR进行原型开发，尽早达成共识，并通过PR作为动态文档。设计文档在特定场景下有用，但容易过时，代码更具说服力。

## Summary
1. **引言**：
   - 描述了软件开发中理想化的流程：先写设计文档，然后通过小增量变化逐步实现功能，保持Git历史记录的整洁有序。
   - 指出这种理想化流程是一种错觉，实际开发中设计文档往往无法直接指导代码的实现。

2. **设计与代码的关系**：
   - 强调通过编码来发现设计，而不是依赖设计文档。
   - 提出通过“编码狂欢”（coding binges）来形成实际的设计方案，即先制造混乱，再从中整理出有效的方案。

3. **编码狂欢的方法论**：
   - **步骤1**：创建一个不打算合并的草稿PR，实现原型或概念验证。
   - **步骤2**：尽早让团队成员审查PR，获取对方案的共识。
   - **步骤3**：在草稿PR中记录设计思路，作为历史文档。
   - **步骤4**：准备好完全丢弃草稿PR，尽早进行。
   - **步骤5**：从草稿PR中逐步提取出可用于生产的PR，逐步完善测试和健壮性。
   - **步骤6**：在每个PR中逐步填补测试和健壮性方面的空白。

4. **成熟度要求**：
   - 强调开发者需要具备丢弃自己代码的成熟度，尤其是高级开发者应能舒适地编写2-3种不同的实现方式。
   - 价值交付不在于代码行数的产出，而在于组织知识的积累。

5. **早期共识的重要性**：
   - 强调在最重要的部分上尽早达成共识，以避免后续的原型工作浪费。
   - 提倡“早失败，早学习”，快速迭代并推进到下一个想法。

6. **代码库的熟悉度**：
   - 高级员工需要对代码库有足够的熟悉度，能够快速组合关键部分。
   - 这也可以是团队协作的结果。

7. **PR作为文档**：
   - PR是开发者最好的文档形式之一，易于发现，且反映了某个时间点的状态，是历史记录。
   - 相比之下，设计文档往往过时，除非频繁更新，否则它们反映的是过时的现实。

8. **“展示而非讲述”**：
   - 原型比设计文档更有说服力，推动变革通常通过代码而非文档。
   - 但需注意，在不自律的组织中，原型可能被误认为是最终答案，而非探索性的问题。

9. **设计文档的适用场景**：
   - **场景1**：用于组织和存档来自多个利益相关者、经理和外部团队的反馈。
   - **场景2**：当想法非常概念化且长期时，设计文档可以作为“北极星”文档。
   - **场景3**：当你在编写代码之前更有效地表达想法时，设计文档可以用于获取反馈。
   - **场景4**：如果你的公司没有丢弃首次解决方案的纪律，设计文档可以作为一种“软”工具，供初级员工更安全地质疑。

10. **设计文档的负面用途**：
    - **负面用途1**：用于“减缓”开发过程，尤其是对不自律或技术较差的开发者。
    - **负面用途2**：作为文档，设计文档通常很快过时。
    - **负面用途3**：试图回答所有设计问题，但实际上只有在编写代码时才能发现真正的问题。

11. **总结**：
    - 如果团队有纪律性，通过编码狂欢会比“设计”更高效。
    - 鼓励在组织中培养这种纪律性，因为代码比文字更有说服力。
