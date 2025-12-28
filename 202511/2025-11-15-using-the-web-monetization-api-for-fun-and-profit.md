# Using the Web Monetization API for fun and profit
- URL: https://blog.tomayac.com/2025/11/07/using-the-web-monetization-api-for-fun-and-profit/
- Added At: 2025-11-15 09:40:22
- Tags: #read #money

## TL;DR
Web Monetization API 允许用户按浏览时长或一次性支付来资助内容创作者。用户需安装扩展并配置钱包，发布者通过在网页中添加标签接收款项。该功能支持动态内容调整，有潜力推动网络小额支付发展。

## Summary
本文介绍了Web Monetization API 的用途、安装与使用方法。Web Monetization 是一项旨在为内容发布者和用户提供实时、无缝支付支持的提议标准，允许用户按浏览时长或一次性支付资助内容创作者。

对于用户来说，安装扩展程序（如 Chrome 上的 polyfill 扩展）、设置支持法定货币的钱包（如 GateHub）后，即可浏览支持该技术的网站。扩展图标会显示页面是否已激活支付，并允许调整每小时支付金额或进行一次性付款，交易详情可在开发者工具中查看。

对于发布者，只需在网页中添加 `<link rel="monetization">` 标签并指向个人支付指针，即可接收资金。此外，Web Monetization JavaScript API 可检测支付事件，实现动态内容调整（如移除广告或显示感谢信息）。作者认为该标准有潜力推动网络内容的可持续发展。

该 API 目前在 Chromium 中有原生实现支持，由 Interledger Foundation 资助开发，未来有望成为网络小额支付的重要解决方案。
