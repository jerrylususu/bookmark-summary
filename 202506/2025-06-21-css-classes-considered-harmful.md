# CSS Classes considered harmful
- URL: https://www.keithcirkel.co.uk/css-classes-considered-harmful/
- Added At: 2025-06-21 10:04:39
- [Link To Text](2025-06-21-css-classes-considered-harmful_raw.md)

## TL;DR


文章指出HTML的`class`属性存在历史局限，无法适应现代复杂交互需求。现有解决方案（如BEM、CSS Modules）存在状态管理缺失、样式膨胀等问题。建议采用HTML原生特性：1）用`data-*`属性参数化控制状态（如`data-size`）；2）通过自定义标签（如`<my-card>`）替代类名标识组件；3）借助`element-internals`定义CSS状态伪类，实现更可靠的状态管理和样式控制。此举可避免命名冲突、减少技术债务，并利用未来CSS标准（如`attr()`函数）优化实现。

## Summary


文章指出继续依赖HTML的`class`属性用于现代CSS设计存在根本性缺陷，并提出通过HTML原生特性（属性、自定义标签、自定义状态）替代方案的实现思路。

**核心观点**：
1. `class`属性的历史局限性源于早期Web设计约束，无法适应现今复杂交互需求
2. 基于类名的解决方案（BEM/Atomic/CSS Modules）均存在共性问题：
   - 状态控制缺失（如动态加载状态被错误设置）
   - 参数类型管理缺陷（如同时可能存在`.Card--size-big`和`.Card--size-small`）
   - 响应式设计导致的样式爆炸
   - 依赖开发人员自我约束或额外工具
   - 增加无效的HTML重复代码

**提出替代方案**：
- **属性系统**：
   - 使用`data-*`属性进行状态参数化（如`data-size="big"`）
   - 属性值唯一性避免类名冲突问题
   - 通过CSS属性函数`attr()`实现动态值转换（需当前值补丁或未来CSS Values 5支持）
   - 支持复合属性值（如`data-border-collapse="left right"`）

- **自定义标签（Custom Elements）**：
   - 用`<my-card>`替代类名作为组件标识
   - 避免`class`命名冲突，且保持浏览器原生语义支持
   - 允许通过`element-internals` API定义自有的CSS状态伪类（`:state(loading)`）

- **自定义状态**：
   - 通过JavaScript直接控制组件内部状态
   - CSS可直接监听元素内置状态变化提供优雅的样式切换

**技术优势**：
- HTML标签本身具备组件标识能力，属性系统提供可靠的参数管理
- Core DOM API安全封装状态逻辑，消除外部随意修改风险
- 避免类名系统的状态耦合性与样式剧烈膨胀问题
- 未来浏览器API（如attr()函数、:state伪类）将进一步增强能力

**现状分析**：
- 所有主流替代方案（含Tailwind等）本质都是在原生属性系统基础上的有限模拟
- Tooling依赖未解决根本问题，反而增加技术债务
- 标签+属性组合更适合现代设计系统需求

**总结建议**：
主动采用HTML5/Custom Element/Modern CSS特性替代过时的`class`系统，可通过当前的属性选择器实现基础控制，未来随着CSS标准发展（如CSS Values 5/Elements Module）实现更优雅解决方案。
