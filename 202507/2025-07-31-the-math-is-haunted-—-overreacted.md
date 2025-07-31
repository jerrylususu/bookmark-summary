# The Math Is Haunted — overreacted
- URL: https://overreacted.io/the-math-is-haunted/
- Added At: 2025-07-31 14:05:28
- [Link To Text](2025-07-31-the-math-is-haunted-—-overreacted_raw.md)

## TL;DR


该文介绍数学形式化语言Lean，演示其语法与`tactic`机制（如`rfl`、`rewrite`），并以错误公理示例说明形式系统潜在矛盾风险。通过费马大定理说明复杂证明依赖协作形式化进展，并推荐学习资源，强调Lean兼具编程与数学探索的趣味性。

## Summary


文章介绍了Lean这一用于数学形式化的编程语言，通过实例演示其基本用法与核心概念。作者以证明`2=2`切入，展示Lean将定理声明转化为类似函数定义的语法，并介绍`tactic`机制——如`rfl`自动证明自反性，`rewrite`进行符号替换等。通过引入荒谬的公理`math_is_haunted:2=3`，文章揭示了公理系统的潜在风险：错误的公理可导致矛盾（如证明`2+2=6`），类比数学史上因集合论悖论引发的危机。同时以费马大定理为例，说明复杂证明需依赖海量已验证定理的协作成果，当前该定理仍在逐步形式化过程中。结尾推荐新手资源（如Natural Numbers Game、Mathematics in Lean），强调Lean兼具编程与数学探索的趣味性。全文结构包括：Lean基本语法操作、公理系统隐患、高阶定理形式化挑战、学习路径建议四部分，通过具体代码片段串联数学形式化的技术流程与哲学思考。
