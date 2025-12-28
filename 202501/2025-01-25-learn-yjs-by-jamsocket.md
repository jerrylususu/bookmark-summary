# Learn Yjs by Jamsocket
- URL: https://learn.yjs.dev/
- Added At: 2025-01-25 22:20:53

## TL;DR
Learn Yjs 是一个交互式教程系列，专注于使用 Yjs CRDT 库构建实时协作应用。教程涵盖基础知识、分布式状态处理、CRDT 介绍及挑战解决方案，通过互动演示和代码练习帮助用户深入理解。项目由 Jamsocket 开发，使用 Astro 和 React 构建，支持实时同步和多用户互动。

## Summary
1. **教程简介**：
   - **Learn Yjs** 是一个交互式教程系列，专注于使用 [Yjs CRDT 库](https://github.com/yjs/yjs) 构建实时协作应用程序。
   - 当前页面本身就是一个实时协作应用的示例，页面上的光标代表其他正在阅读页面的真实用户。

2. **教程内容**：
   - **基础知识**：从 Yjs 的基础开始，逐步深入。
   - **分布式应用状态处理**：探讨在分布式应用中如何处理状态。
   - **CRDT 介绍**：解释什么是 CRDT（Conflict-Free Replicated Data Type），以及为什么需要使用它。
   - **挑战与解决方案**：讨论构建协作应用时可能遇到的陷阱，并提供避免这些陷阱的方法。
   - **互动演示与代码练习**：通过可探索的演示和代码练习，帮助用户深入理解 Yjs 的工作原理。

3. **互动演示示例**：
   - **客户端模拟**：页面上的每个框代表一个客户端（即运行 Yjs 应用的独立计算机）。
   - **实时同步**：用户在一个客户端上的操作会自动同步到其他客户端。
   - **网络延迟模拟**：通过顶部的滑块可以控制客户端之间的网络延迟，观察不同网络条件下的交互效果。

4. **教程入口**：
   - 点击按钮进入 **Lesson 1**，开始学习 Yjs 的基础知识。
   - [Lesson 01 Introduction](https://learn.yjs.dev/lessons/01-introduction/)

5. **项目背景**：
   - **Jamsocket**：Learn Yjs 是由 [Jamsocket](https://jamsocket.com/) 开发的项目，Jamsocket 是一个用于构建实时应用的平台。
   - **Y-Sweet**：页面上的实时光标和多用户花园功能由 [Y-Sweet](https://jamsocket.com/y-sweet) 提供支持，这是一个开源的 Yjs 服务器，具有内置的持久化功能。

6. **技术栈**：
   - **网站构建**：使用 [Astro](https://astro.build/) 构建。
   - **互动演示与练习**：使用 [React](https://react.dev/) 和 [Yjs](https://github.com/yjs/yjs) 构建。

7. **总结**：
   - Learn Yjs 提供了一个从基础到高级的完整学习路径，帮助开发者掌握如何使用 Yjs 构建实时协作应用。
   - 通过互动演示和代码练习，用户可以直观地理解 Yjs 的工作原理，并应用于实际项目中。
