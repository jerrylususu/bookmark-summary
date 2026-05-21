# Resident: vibe coding firmware (our new sandbox library for ESP32 devices)
- URL: https://interconnected.org/home/2026/05/20/resident
- Added At: 2026-05-21 14:07:18
- Tags: #read #hardware

## TL;DR
Resident 是 Inanimate 公司开源的 ESP32 代码沙盒库，支持 Wi-Fi 直接加载 AI 生成的代码，无需编译。它基于 Lua 运行时，提供安全运行环境，允许动态执行应用，适用于原型开发和产品部署，可实现智能设备交互。

## Summary
Resident 是 Inanimate 公司开源的 ESP32 设备代码沙盒库，支持通过 Wi-Fi 直接加载 AI 生成的代码，无需编译或刷写固件。其核心是为设备开发者提供安全的运行环境，允许 AI 代理动态编写并执行应用程序，同时限制对硬件和网络的访问权限，确保安全性。

该库基于 Lua 运行时，集成了 WebSocket、JSON 消息传递和 Wi-Fi 配置等功能，并提供后端服务器和 Claude 技能支持，便于快速开发和部署。Resident 适用于原型设计和产品开发，支持热加载应用，即使断网也能通过本地消息传递运行。

用户可通过 M5StickS3 开发板或网页模拟器体验 Resident，实现如智能时钟、烤箱定时器等交互功能。Inanimate 认为这种沙盒机制是未来 AI 与物理设备交互的基础，旨在让设备能安全、即时地响应用户意图。
