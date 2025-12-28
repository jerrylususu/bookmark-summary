# YAGNI exceptions
- URL: https://lukeplant.me.uk/blog/posts/yagni-exceptions/
- Added At: 2024-08-07 14:51:26

## TL;DR
文章讨论了YAGNI原则的例外情况，包括Zero One Many规则、版本控制、日志记录、时间戳、数据收集和关系数据库的使用，强调在软件开发中应提前考虑这些事项以应对未来需求。

## Summary
1. **YAGNI原则信仰**：作者本质上相信YAGNI原则，即“你不会需要它”，主张在明确需要时才添加软件功能，包括通用性和抽象性，而不是提前添加。

2. **YAGNI的例外情况**：
   - **Zero One Many规则应用**：当需求从“每个用户需要存储一个地址”变为“每个用户需要存储两个地址”时，应直接设计为“每个用户可以存储多个地址”，因为很可能需要超过两个地址。
   - **版本控制**：对于协议、API、文件格式等，应提前考虑如何处理不同版本，特别是在不控制两端或无法同时更改它们的情况下。
   - **日志记录**：特别是事后调试，在非确定性或难以重现的情况下，问题出现后再添加日志往往为时已晚。
   - **时间戳**：
     - 创建时间戳，如Simon Willison所言，每个数据库表都应有自动填充的“created_at”列，以备后续调试使用。
     - 更普遍地，使用可空的时间戳（如`completed_at`）代替布尔标志（如`completed`），更为有用。
   - **数据收集**：收集比当前需要更多的数据通常不是问题，因为可以随时丢弃，但如果从未收集，则永远丢失。
   - **关系数据库**：如果需要数据库，应直接使用关系型数据库，而不是非关系型数据库，因为大多数数据本质上是关系的，关系型数据库提供了对未来需求变化的保险。

3. **总结**：作者列出了一些在软件开发中应提前考虑的事项，即使这些事项可能看起来在当前不需要，但长远来看会带来显著的好处。

4. **相关讨论**：
   - [Lobsters上的讨论](https://lobste.rs/s/quywfp/yagni_exceptions_2021)
   - [Twitter上的讨论](https://twitter.com/spookylukey/status/1409967250426281984)
   - Simon Willison关于PAGNIs的回应文章及其讨论：
     - [文章链接](https://simonwillison.net/2021/Jul/1/pagnis/)
     - [Twitter讨论](https://twitter.com/simonw/status/1410678459756552198)
     - [Lobsters讨论](https://lobste.rs/s/nokjr0/pagnis_probably_are_gonna_need_its)
   - Jacob Kaplan-Moss关于安全PAGNIs的回应文章及其讨论：
     - [文章链接](https://jacobian.org/2021/jul/8/appsec-pagnis/)
     - [Twitter讨论](https://twitter.com/jacobian/status/1413157068375302146)
