Title: Visual Types

URL Source: https://types.kitlangton.com/

Published Time: Thu, 13 Nov 2025 02:00:16 GMT

Markdown Content:
Foundation
----------

A type is a label for **a set of possible runtime values**. Some types are small, some infinite, and some special cases exist at the extremes.

boolean

{true, false}

A literal type represents a single, exact value. Unlike `number` which contains all numbers, the literal type `42` contains only one value: 42.

42

{42}

A union type combines multiple types using `|`. The resulting set contains all values from each member type. `"red" | "blue"` contains exactly two values, while `string | number` contains all strings and all numbers.

true | false

{true, false}

`A extends B` means A is a subtype of B. If types are sets, then subtypes are subsets. Type A is a subtype of B when every value in A exists in B (including when A and B are identical).

true extends boolean

true

boolean

A **tuple type** is a fixed-length array where each position has a specific type. Unlike regular arrays, tuples have known length and heterogeneous types.

[boolean]

{[true], [false]}

Object types define sets based on their properties. `{ id: number }` represents the set of all objects that have at least an `id` property of type `number`. Objects with extra properties still belong to this set.

{alive: boolean}

{{alive: true}, {alive: false}, {alive: true, x: 1}, ...}

The `&` operator creates an intersection containing only values that belong to BOTH types. For primitives like `string & number`, no value can be both, so the result is `never`. Objects must satisfy all properties from both sides.

string&number

never

Basics II
---------

Type aliases let you name a type. Using the alias is identical to using the type it points to; they are completely transparent.

UserId

string

Think of generic type aliases as **type-level functions**. Just as a function takes values and returns a new value, a generic type alias takes types as parameters and returns a new type.

Identity<string>

string

The `typeof` operator extracts the type from a runtime value. Unlike JavaScript's `typeof` which runs at runtime, TypeScript's `typeof` operates at compile-time to capture the inferred type.

typeof message

string

`as const` makes object properties and array elements readonly with literal types. Even with `const`, object/array values are normally widened - `as const` prevents this.

typeof config

{host: string;port: number}

You can assign any value to both `any` and `unknown`. `any` opts out of type-checking altogether, while `unknown` requires you to narrow the type before use.

x+10

Type-Check

Type-checks!

Run

15

Object Patterns
---------------

The `keyof` operator extracts all property keys from an object type as a union of string literals. This is essential for type-safe property access and building mapped types.

keyof{a: number;b: string}

"a" | "b"

Indexed access types look up the type of a property using bracket notation. You can use literal keys, union keys, or `keyof T` on objects—and the same syntax works for tuples and arrays with numeric indices.

{color: string;size: number}["color"]

string

Mapped types use `[K in ...]` to iterate over keys and create new object types.

{[K in"x" | "y"]: number}

K = "x"

x: number

K = "y"

y: number

{x: number;y: number}

Conditional Types
-----------------

Conditional types are type-level ternaries. The syntax `T extends U ? X : Y` checks whether T is a subset of U, then evaluates to X if true or Y if false.

"red"extends string?"yes":"no"

"yes"

In TypeScript, every type extends itself. This is called **reflexivity**.

string extends string?true:false

true

When a union is evaluated, TypeScript processes each member individually and then unions the results together. This behavior is called **distributivity**.

42 extends string?string:number

42 extends string?string:number

number

number

Wrap types in tuples `[T] extends [U]` to disable distribution. This checks if the entire union extends the target type, rather than distributing over individual members.

WrapInArray<string | number>

(string | number)[]

Use `never` to drop non-matching branches; the pieces that return `never` disappear from the union.

`type Filter<T, Match> = T extends Match ? T : never;`

Filter<string | number,string>

string

`infer` lets conditional types capture part of a matched shape and reuse it later in the same branch.

UnwrapPromise<Promise<string>>

string

Utility Types
-------------

```
type Pick<T, K extends keyof T> = {
  [P in K]: T[P]
}
```

Pick<{a: number;b: string;c: boolean},"a" | "b">

{a: number;b: string}

```
type ReturnType<T extends (...args: any) => any> = 
  T extends (...args: any) => infer R ? R : any
```

ReturnType<()=>string>

string

```
type Parameters<T extends (...args: any) => any> = 
  T extends (...args: infer P) => any ? P : never
```

Parameters<(x: number, y: string)=>void>

[number, string]