# Thinking about tests: assertions and matchers
- URL: https://zverok.space/blog/2026-08-16-assertions-and-matchers.html
- Added At: 2026-08-17 13:36:23
- Tags: #read

## TL;DR
文章探讨测试框架中“断言”与“匹配器”的设计演变，指出将匹配器独立为可组合对象能提升测试代码的可读性、扩展性与维护性。作者认为这种低层次 API 设计在 AI 辅助开发时代反而更关键，因表达性强的测试代码更易审查、节省 token，并强调测试措辞会影响开发者思维与代码质量。

## Summary
这篇文章探讨了测试框架中“断言”（assertion）和“匹配器”（matcher）这两个概念的设计演变，以及为什么这种低层次的 API 设计仍然值得关注。作者是 Ruby 开发者，长期关注测试代码的可读性与表达性，认为测试代码应当像产品代码一样易于人类阅读和维护，而不是被当作枯燥的“苦役”。

文章从一个最小的测试检查开始：最简单的 `assert(expression)` 只能告诉你真假，失败时无法提供足够信息。于是出现了 `assert_equal(actual, expected)` 这样的专用断言函数，能在失败时显示“期望值是什么，实际值是什么”。这逐渐发展成各种 `assert_something` 风格的 API，至今仍是许多语言中最常见的测试风格。

转折点出现在 2005 年前后，行为驱动开发（BDD）理念兴起。核心变化不是技术上的，而是思维方式：从“写一个测试来验证代码”转向“描述代码应有的行为”。这种思维改变也体现在 API 措辞上——例如把 `assertEquals(expected, actual)` 改为 `shouldBeEqual(actual, expected)`。Ruby 的 RSpec 库由此诞生，并逐渐演化出“匹配器”的概念。

早期 RSpec 直接在基础对象上增加 `should` 方法，写出 `actual.should equal expected` 这样的代码。后来为了避免污染所有对象，演变为 `expect(actual).to matcher` 的形式。这里的重点是：`matcher` 是一个独立构造的对象，而不是被硬编码在断言方法内部。这种分离带来了很大的灵活性。

匹配器的价值主要体现在两方面。第一，它可以组合。例如在 RSpec 中可以用逻辑运算组合：`expect(user.email).to be_a(String).and match(/.+@.+/)`，或者嵌套匹配：`expect(emails).to all be_a String`。第二，自定义匹配器非常容易，通常只需要实现三四个简单方法（如匹配逻辑和失败消息）。在大型代码库中，自定义匹配器可以把复杂的验证逻辑封装成接近自然语言的短语，比如 `expect { some_code }.to create_record(User).with(name: 'Mary')`。

作者指出，并非所有看起来像匹配器的 API 都是真正的“匹配器”。例如 Jest 和 Chai 虽然也使用 `expect(actual).toSomething(expected)` 的形式，但它们把匹配器实现为包装对象的方法，而不是独立构造的对象，因此在扩展和组合上受到限制。而 Hamcrest 则使用 `assertThat(actual, equalTo(expected))` 的形式，同样引入了独立的匹配器概念。

文章还讨论了为什么这种设计在 AI 时代依然重要。作者认为，AI 代理会生成大量测试，但代码仍然会被人类和机器频繁阅读。更简洁、表达性更强的测试代码意味着更少的上下文窗口和更低的 token 消耗，也更容易被人类审查和微调。可读性不是过时的追求，反而变得更加关键。

最后，文章附带分析了 pytest 的特殊情况。pytest 使用原生 `assert` 语句，并通过元编程在失败时提供详细的表达式还原和变量值，但这种方法局限于语言内置的运算符。例如 `assert x == y` 能很好地显示差异，但 `assert re.match(...)` 失败时只会显示“Assert None”。pytest 的 `approx` 是一个有趣的例外：它通过返回一个特殊对象，利用 Python 的 `__eq__` 协议实现类似匹配器的行为，但整个库中只有这一种。第三方库 anys 则扩展了这一技巧，实现了通用的匹配器。这从侧面说明，“匹配器”作为一种基础组件，即使不被显式设计，也可能在某些框架中自发出现。

整体来看，文章的核心观点是：测试 API 的措辞和结构会影响开发者的思维和代码质量。将“断言”与“匹配器”分离，使得测试代码更接近自然语言描述，更容易组合和扩展，从而提升整个代码库的可维护性。这种关注细节的做法并非“过时”或“不重要”，尤其是在 AI 辅助开发的时代，表达性强的代码反而更具优势。
