# Software engineering with LLMs in 2025: reality check
- URL: https://newsletter.pragmaticengineer.com/p/software-engineering-with-llms-in-2025
- Added At: 2025-07-02 14:28:52
- [Link To Text](2025-07-02-software-engineering-with-llms-in-2025-reality-check_raw.md)

## TL;DR


2025年AI工具对软件工程的影响引发两极观点。高管乐观预测AI主导代码生成，但开发者指出其不可靠性，需人工修正，部分案例甚至引发损失。科技公司如微软、谷歌推进工具整合，但亚马逊等注重风险控制；Windsurf等初创公司AI生成超95%代码，生物技术公司却因低效转向传统工具。资深工程师态度分化，有人验证AI效率突破，也有人警告过度依赖风险。当前挑战包括代码质量参差、安全漏洞及领域适配，需平衡技术信任与协作流程革新。

## Summary


文章讨论了2025年AI工具对软件工程的实际影响，结合多个案例和专家观点分析其现状与挑战。主要内容包括：

### 一、AI工具使用现状的双极观点  
1. **高管的激进预测**  
   - 多家AI公司高管（如Anthropic、微软、谷歌）宣称LLM将主导代码生成（如微软称30%代码由AI编写，Anthropic赌注“一年内所有代码AI化”）。  
   - 这些言论被视作促销手段，引发开发者对技术泡沫的担忧。  

2. **开发者的现实反馈**  
   - 案例：GitHub Copilot Agent在.NET代码审查中频繁失败，Devin工具生成错误代码导致$733损失。  
   - 开发者认为AI工具仍不可靠，需人工审核，对其生产力提升存疑。

---

### 二、AI工具公司的内部实践  
1. **Anthropic**  
   - 内部工具Claude Code使用率达90%，代码自动生成率持续提升（ launching Claude Sonnet 4后使用量增40%，用户增长160%）。  
   - 发明**MCP协议**（Model Context Protocol），被AWS、谷歌等广泛采用，构建跨系统AI协作基础。  

2. **Windsurf**  
   - 内部代码95%由AI生成（通过其工具Cascade），非技术人员（如市场人员）也能用工具开发系统。  

3. **Cursor**  
   - 工程团队用自身产品编写40-50%代码，但低于Claude Code的自用率。

---

### 三、大科技公司的整合策略  
1. **谷歌（Google）**  
   - 内部工具全面AI化：Cider（Gemini支持的IDE）、Critique（AI代码审查）、CodeSearch（AI集成）。  
   - 采用“谨慎策略”推动AI工具落地，避免过度依赖。  
   - 预计未来代码量将激增10倍，需加强代码审查、部署等流程。  

2. **亚马逊（Amazon）**  
   - 推广**Amazon Q**（ GitHub Copilot竞品），优化AWS相关任务，但受限于单文件处理、Java专精等问题。  
   - 发挥其**API优先**战略优势（始于2002年Jeff Bezos的API强制政策），将API转为MCP服务器，支持AI代理自动化操作。  

---

### 四、AI初创公司的实践差异  
1. **oncall管理公司incident.io**  
   - 广泛采用Claude Code、Cursor，结合MCP协议自动化工作流，内部分享AI工具使用技巧（如用Claude分析文档）。  

2. **生物技术AI公司**  
   - 对AI编码工具失望：AI代码审查评论仅10%有效，仍依赖传统工具（如ruff代码检查器、uv项目管理器）。  
   - 认为LLM在特定领域（如数值型ML流水线）不如优化传统工具显著。

---

### 五、资深工程师的反思与转变  
1. **Armin Ronacher（Flask创始人）**  
   - 曾怀疑AI工具，现依靠Claude Code代理功能实现“远程编程”，认为其代码质量提升和信任度跨越临界点。  

2. **Peter Steinberger（PSPDFKit创始人）**  
   - AI工具（如Cursor）重启编程热情，称代理工具使产出能力提升10-20倍，引发开发者“全职投身AI”的浪潮。  

3. **Birgitta Böckeler & Simon Willison**  
   - 视AI为“侧向工具”，突破传统抽象层级，开辟新可能性（如自然语言到汇编级的自由表达）。  

4. **Kent Beck & Martin Fowler**  
   - 强调AI需与开发者技能结合，警惕过度依赖；Fowler称AI可能重构工程协作模式。

---

### 六、开放问题  
1. **认知分歧**：高管比开发者更看好AI工具前景，实际落地效果存疑。  
2. **工具使用率**：仅少数公司达到代码生成超90%，多数场景仍在实验阶段。  
3. **生产力提升**：开发者评估AI节省时间差异大（如Claude Code用户称效率翻倍至10倍）。  
4. **安全与风险**：AI生成代码引入的漏洞、责任归属问题尚未解决。  
5. **领域适配性**：AI工具在特定技术领域（如生物计算）表现欠佳，需定制化优化。
