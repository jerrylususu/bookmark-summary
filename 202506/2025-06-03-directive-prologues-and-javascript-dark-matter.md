# Directive prologues and JavaScript dark matter
- URL: https://macwright.com/2025/04/29/directive-prologues-and-javascript-dark-matter
- Added At: 2025-06-03 14:33:17

## TL;DR


本文总结了TypeScript/JavaScript中三种特殊控制语法：JSX Pragmas通过C风格注释（如`/** @jsx h */`）配置转译规则，需置于文件起始；Directive Prologues如`"use strict"`和React的`"use client"`等指令需置于代码开头；Magic Comments以sourcemap注释形式（如`//# sourceMappingURL`）指导编译。三者中仅指令标准化，其余依赖非标准实现，但均在代码转译或执行中扮演关键角色。

## Summary


本文讨论TypeScript/JavaScript中影响代码解释或转译的特殊语法，包括Pragma指令、Magic Comments和Directive Prologues，并总结其用法、规则及标准化状态。

### JSX Pragmas  
用于控制TypeScript将JSX语法转换为特定函数调用（如`h()`）。示例：`/** @jsx h */`需使用C风格注释（非`//`），且必须置于文件最开始位置。TypeScript解析时会提取`pragmas`成员记录配置。该语法起源于2013年React早期开发，由Facebook/Instagram团队设计，后被Babel和TypeScript支持。

### Directive Prologues  
ECMAScript标准定义的指令前缀，如 `"use strict";`，通过放置在代码开头指定行为。React使用类似语法的`"use client"`和`"use server"`控制代码执行位置。其他提案包括隐藏函数源代码的`"hide source"`和已弃用的asm.js指令`"use asm"`。V8引入新编译提示`//# allFunctionsCalledOnLoad`，采用与sourcemap注释相同的语法（如`//# sourceMappingURL`），但早期sourcemap曾使用`//@`前缀。

### 三类控制语法的对比  
1. **指令（Directives）**：  
   - 标准化于ECMAScript，需以代码形式（如`"use strict";`）置于文件或函数开头。  
   - 直接参与代码逻辑，可能增加文件体积。  

2. **Pragma注释**：  
   - 以注释形式（如`/** @jsx */`）提供转译配置，未标准化。  
   - 规则严格，需特定注释格式和位置。  

3. **Magic Comments**：  
   - 如sourcemap注释`//# sourceMappingURL`或V8新语法，作用于映射或编译配置，未标准化。  

这些语法是JavaScript的“暗物质”，长期被开发者用于实现特定功能（如严格模式），但其名称和机制常被忽略。虽未被充分标准化，却在代码中扮演关键角色。
