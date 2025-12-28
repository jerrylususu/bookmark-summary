# Visual Types
- URL: https://types.kitlangton.com/
- Added At: 2025-11-14 13:35:37
- Tags: #guide

## TL;DR
本文介绍了TypeScript类型系统的基础与进阶概念，包括类型定义、子类型关系、复合类型，以及泛型、类型操作符、条件类型和常用工具类型等，用于构建和操作类型。

## Summary
## 类型基础

**类型的定义**
- 类型是「运行时可能值的集合」的标签，集合大小不一，存在特殊极端情况。
- 字面量类型：表示单个确切值，如 `42` 仅包含值 42。
- 联合类型：通过 `|` 组合多个类型，包含所有成员类型的值，如 `true | false`。

**子类型关系**
- `A extends B` 表示 A 是 B 的子类型（即 A 是 B 的子集），若 A 与 B 相同也成立。

**复合类型**
- 元组类型：固定长度数组，各位置有特定类型，如 `[boolean]` 表示 `[true]` 或 `[false]`。
- 对象类型：基于属性定义集合，如 `{ alive: boolean }` 包含所有至少具有 `alive` 属性且类型为 boolean 的对象。
- 交叉类型：使用 `&` 创建，仅包含同时属于两个类型的值，如 `string & number` 结果为 `never`（无交集）。

## 进阶概念

**类型别名与泛型**
- 类型别名：为类型命名，使用时完全透明。
- 泛型类型别名：类似类型级函数，接收类型参数并返回新类型，如 `Identity<string>` 返回 `string`。

**类型操作符**
- `typeof`：编译时提取值的推断类型，如 `typeof message` 得到 `string`。
- `as const`：使对象属性或数组元素变为只读字面量类型，防止类型拓宽。

**特殊类型**
- `any` 和 `unknown`：均可接受任何值，但 `any` 禁用类型检查，`unknown` 需先收窄类型才能使用。

## 对象模式

**键操作**
- `keyof`：提取对象类型的所有键作为字面量联合，如 `keyof { a: number; b: string }` 得到 `"a" | "b"`。
- 索引访问类型：通过键查找属性类型，如 `{ color: string; size: number }["color"]` 得到 `string`。

**映射类型**
- 使用 `[K in ...]` 迭代键生成新对象类型，如 `{ [K in "x" | "y"]: number }` 生成 `{ x: number; y: number }`。

## 条件类型

**基本语法**
- 形式为 `T extends U ? X : Y`，根据 T 是否为 U 的子集返回 X 或 Y，如 `"red" extends string ? "yes" : "no"` 得到 `"yes"`。

**特性**
- 自反性：每个类型是自身的子类型，如 `string extends string` 为 `true`。
- 分配性：对联合类型逐个处理并合并结果，如 `42 extends string ? string : number` 得到 `number`。
- 禁用分配：用元组包装（如 `[T] extends [U]`）检查整个联合类型。

**高级用法**
- 使用 `never` 过滤非匹配分支，如 `Filter<string | number, string>` 得到 `string`。
- `infer` 在条件类型中捕获匹配形状的部分，如 `UnwrapPromise<Promise<string>>` 得到 `string`。

## 工具类型

**常用工具类型示例**
- `Pick<T, K>`：从 T 中选取指定键 K 的属性，如 `Pick<{ a: number; b: string; c: boolean }, "a" | "b">` 得到 `{ a: number; b: string }`。
- `ReturnType<T>`：提取函数返回类型，如 `ReturnType<() => string>` 得到 `string`。
- `Parameters<T>`：提取函数参数类型元组，如 `Parameters<(x: number, y: string) => void>` 得到 `[number, string]`。
