# Mission Impossible: Managing AI Agents in the Real World
- URL: https://levelup.gitconnected.com/mission-impossible-managing-ai-agents-in-the-real-world-f8e7834833af
- Added At: 2025-05-11 05:58:10
- [Link To Text](2025-05-11-mission-impossible-managing-ai-agents-in-the-real-world_raw.md)

## TL;DR


文章强调规划为核心，90%精力用于需求拆解与迭代优化，结合高质量输入（文档、代码）及工具技巧（如@mention引用规则）约束AI；分步执行并人工验证，避免模糊需求生成低质代码；建立规则文件与架构文档控制AI行为，及时重构技术债务，平衡效率与成本，始终以人工干预为主导，规避模型局限性。

## Summary


- **规划为核心**：  
  90%的工作应集中在规划而非直接执行，多数AI错误源于不良计划或代码，而非模型缺陷。需通过规划将需求分解为可执行的模块化步骤，并频繁迭代调整。

- **重视输入材料与技巧**：  
  工具本身变化迅速，关键在于输入（代码、数据、提示词）的质量。优秀工具可自动补全代码片段或引用架构，但需开发者精通工具文档。工具如Cursor允许通过`@mention`代码文件或规则文档提升预测准确性。

- **避免“氛围编码”（Vibe Coding）**：  
  直接给出模糊需求让AI即兴生成代码会制造技术债务，仅适合生成原型。需明确需求边界，将不可行方案回退至规划阶段改进。

- **制定可执行的计划文档**：  
  在代码库中创建`/plans`目录，用Markdown编写详尽计划，包含代码示例、注释及步骤说明。计划文件需经常更新，且每次执行步骤后提交代码并标注进展，形成可追溯的记录。

- **逐步执行与验证**：  
  计划分步骤执行，人工测试每一步结果，避免AI未经验证直接修改代码。复杂任务需先模拟执行流程，确保步骤顺序与逻辑无误。

- **应对模型的预测偏差**：  
  AI可能忽视代码的复杂性，倾向于选择训练集中的常规方案。自定义架构需开发者主动干预，明确禁止违规操作，并通过具体案例（如错误省略号处理）验证输出。

- **利用文档约束生成行为**：  
  在提示中引用技术规范、架构图或文档片段，辅助AI生成符合需求的代码。文档需存于代码库并持续维护。

- **规则与上下文协议（MCP）**：  
  建立规则文件控制AI的行为，如禁用继承、规定代码风格或依赖库。规则需定期更新以匹配代码库变化，避免模型受训练数据干扰偏离正确路径。

- **技术债务暴露与重构**：  
  通过与AI协作，会发现隐藏的技术债务。需及时重构代码，使架构更清晰，便于后续AI辅助开发。例如，分离JSON元数据以解决社交分享问题。

- **成本与效率平衡**：  
  免费工具可能难以生成高质量代码，付费工具更稳定。需选择适合的模型，避免因过度追求低价导致频繁返工。

- **模型局限性认知**：  
  AI模型不理解代码语义，仅通过上下文预测结果，无法保证方案的完全正确性。需人工验证执行结果，例如直接测试功能而非依赖模型口述。

- **持续迭代流程**：  
  每个计划尝试2-3次修订后执行，单步执行后提交代码，逐步构建可靠解决方案。关键在开发者与AI的协作中形成长期优化反馈循环，保持对项目的控制力。

- **工具依赖陷阱警告**：  
  工具界面与功能频繁变化，依赖特定工具按键会导致僵化。开发流程应围绕代码库和计划文档展开，而非特定工具的功能设计。

- **架构优化要求**：  
  AI难以处理混乱的架构，需开发者先清理代码，并书面化说明架构设计逻辑。将架构问题的描述单独规划为步骤，逐步解决优先于直接生成功能代码。

- **文档与代码共生**：  
  生成的计划文件既是代码指南也是执行工具。通过`@mention`调用计划文件，实现代码与文档的双向映射，减少叙述性遗漏。

- **心理预期管理**：  
  AI的“高完成度”输出可能包含逻辑漏洞或不符合目标的方案（如省略号的硬编码逻辑），开发者需保持警惕，而非被表面进展麻痹。

- **技术伦理考量**：  
  若未明确约束路径，AI可能采用危险或有缺陷的解决方案（如自动驾驶模型忽略安全规则）。需通过规则文档和计划步骤强制实现所需约束。

- **迭代式规划语言**：  
  使用伪代码结合自然语言构建可扩展的规划语言，例如Cursor的Markdown计划模板，为AI提供结构化指令而非开放式问题。

- **人工干预优先级**：  
  复杂问题需开发者主导路径设计，AI仅负责填充实例代码。例如，先确定元数据分离架构，再让AI生成具体JSON模板。

- **错误诊断最佳实践**：  
  当AI输出失败时，将问题转化为具体需求工单，提供截图、日志和架构文档辅助其定位。避免直接修补代码，优先重新规划问题解决路径。

- **长期代码质量提升**：  
  通过AI生成的失败案例反推技术债务成因，推动代码优化。例如，省略号问题揭示了现有CSS布局的不足，需手动修复后更新文档。

- **工具的双向赋能**：  
  高质量提示设计能力提升代码质量，同时执行AI生成代码的过程倒逼开发者加深对自身系统的理解，形成技术能力增强的“付费机制”。
