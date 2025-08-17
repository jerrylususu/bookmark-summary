# Beyond Booleans — overreacted
- URL: https://overreacted.io/beyond-booleans/
- Added At: 2025-08-17 09:59:07
- [Link To Text](2025-08-17-beyond-booleans-—-overreacted_raw.md)

## TL;DR


本文对比TypeScript与Lean的类型系统，指出Lean通过Prop类型将逻辑命题作为独立类型，证明即该类型的值。其类型层级包含命题值、Prop及Sort，利用Curry-Howard对应实现"编译期数学验证"。同一命题的不同证明在类型上等价，否定命题需提供证明，而矛盾命题类似TypeScript的never类型。Lean允许函数携带证明参数，通过类型约束确保逻辑严谨性，实现编程与数学证明的深度融合。

## Summary


本文对比了TypeScript与Lean对逻辑表达式类型的处理差异，揭示了Lean中命题类型（Prop）的独特逻辑体系：

一、类型系统对比
- TypeScript：逻辑表达式直接坍塌为布尔值（true/false），类型系统仅支持单一布尔类型
- Lean：表达式不坍塌为结果，"2+2=4"是Prop类型（命题类型），保持作为待证明的逻辑陈述

二、命题即类型系统
1. 命题的类型层级
   - 命题自身是Prop类型（如`2+2=4 : Prop`）
   - 证明是命题类型的值（如`by rfl : (2+2=4)`）
   - 形成类型层级：命题值 → Prop类型 → Sort类型

2. 证明的本质
   - `Eq.refl`构造等式证明值
   - `by rfl`作为宏生成反射证明
   - 通过类型约束确保"只能证明正确命题"

三、证明的特性
1. 证明无关性：同一命题的多个证明在类型上等价
2. 否定命题：通过`Not (命题)`构建新类型，需提供否定性证明
3. 不可能类型：如`2+2=5`类似TypeScript的never类型，实际是不可达类型

四、类型导向的真值约束
1. 函数参数可携带证明
   ```lean
   def safeFunction (x: ℝ) (proof0: x≥0) (proof1:x≤1) := ...
   ```
2. 非计算场景推导：如通过`sin_sq_le_one`证明三角函数边界

五、证明组合范例
1. 通过数学库函数组合证明
2. 实现对不可计算概念（如无限级数）的严格推导
3. `noncomputable`标记区分可计算/纯逻辑表达式

六、核心思想
- Curry-Howard对应：命题等价于类型，证明等价于该类型的值
- 通过类型系统实现"编译期数学验证"
- 在Lean中数学证明与程序编写共享相同类型逻辑体系

结论：Lean的类型系统通过Prop类型和证明值体系，将编程与数学证明结合，展示了类型理论在严谨性要求高的领域（如形式化证明）的独特潜力。
