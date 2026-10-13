# Don't sleep on wrapture
- URL: https://simonwillison.net/2026/Sep/11/wrapture/
- Added At: 2026-10-13 14:20:40
- Tags: #read #tools #python

## TL;DR
Simon推荐Graham的新Python库wrapture：猴子补丁，兼顾测试与调用追踪，可零代码TOML配置。虽处alpha但很实用，不该被忽视。

## Summary
这篇文章是 Simon Willison 写的一篇推荐博客，主角是 Graham Dumpleton 开发的新 Python 库 **wrapture**。核心意思是：这个库非常好用，但关注度太低，不该被忽视。

**wrapture 是什么**

它是一个 monkey patching（猴子补丁）库，能在运行时动态修改代码行为。特别之处在于，它同时服务于两个场景：

- **测试**：功能上可以替代 `unittest.mock` 那类工具
- **可观测性**：类似 New Relic 风格的调用追踪（tracing）

**作者为什么推荐**

Graham Dumpleton 从 2026 年 8 月 31 日发布初版后，几乎每天发一篇教程，文章把它们全列了出来：

1. **Introducing wrapture** — 库的总体介绍，测试与追踪兼顾。
2. **Unit testing with wrapture** — 做 `unittest.mock` 类似的事。
3. **Recording calls with wrapture** — 把方法调用记录成时间线，再处理和展示为树状结构。
4. **Phased behaviour in wrapture** — 让被打补丁的方法在多次调用中切换行为。
5. **Beyond callables in wrapture** — 不只打补丁函数，还能处理属性、字典、生成器。
6. **Live tracing with wrapture** — 追踪一个正在运行的应用，看清它到底怎么执行。
7. **Zero-code tracing with wrapture** — 不用改一行 Python 代码，只用一个单独的 TOML 文件就能配置追踪。
8. **Tracing Flask with wrapture** — 借助配套的 `wrapture-instrumentation` 包给 Flask 应用插桩。这个配套包还支持一大批库：`aiohttp.client`、`aiohttp.web`、`django`、`fastapi`、`flask`、`grpc`、`http.client`、`httpx`、`jinja2`、`requests`、`sqlalchemy`、`sqlite3`、`starlette`、`urllib.request`、`urllib3`、`uvicorn`、`werkzeug.serving`、`wsgiref.simple_server`、`xmlrpc.client`、`xmlrpc.server`。
9. **Finding slow code with wrapture** — 记录计时信息，既能看单次调用，也能看多次调用的聚合结果，用来定位慢代码。
10. **OpenTelemetry export in wrapture** — 把追踪数据导出到 OpenTelemetry。

**其他资源与现状**

Graham 还准备了一套交互式工作坊（JupyterLab notebook 形式）。wrapture 目前仍是 alpha 阶段，但已经相当可用，尤其是「零代码、纯 TOML 配置」这一点让它试起来门槛很低。

**作者的判断**

Simon 认为这属于那种「瑞士军刀型」的包：一旦掌握，未来很多年都能用来解决各种各样的问题。所以他提醒大家——别睡在 wrapture 上（别错过它）。
