# Testing JavaScript without a (third-party) framework
- URL: https://alexwlchan.net/2023/testing-javascript-without-a-framework/
- Added At: 2026-05-03 02:28:27
- Tags: #read #frontend

## TL;DR
本文介绍了一种极简的浏览器内单元测试方案，通过三个核心函数（it、assertEqual、assertTrue/False）在HTML中直接运行测试，无需第三方框架或构建环境。该方法适合小型纯JS项目，降低维护成本，快速提供测试反馈，务实且轻量。

## Summary
这篇文章介绍了作者如何在不使用第三方测试框架的情况下，为纯JavaScript项目编写单元测试。作者认为，对于小型或内容型网站，使用复杂的构建系统和测试框架（如Jest、Jasmine）会增加环境维护的负担，尤其在长时间未维护后难以快速重启测试。因此，他开发了一个极简的浏览器内测试方案。

核心思路是利用浏览器本身运行JavaScript的能力，通过几个简单的辅助函数在HTML文件中编写测试用例，并在浏览器中直接查看结果。测试框架仅包含三个关键函数：
- `it(description, body_of_test)`：定义测试用例，通过try-catch捕获异常，成功则显示绿色通过，失败则显示红色错误信息。
- `assertEqual(x, y)`：比较两个值是否相等，支持基本类型和数组比较。
- `assertTrue/assertFalse`：基于assertEqual的辅助断言。

测试结果通过DOM元素直接渲染在页面上，配合少量CSS样式（绿色勾选/红色叉号）提供视觉反馈。作者以书本追踪器中的`createPublicationYearLabel`函数为例，展示了如何测试这种纯函数逻辑。

这种方法的优势在于：
- 无需安装npm或配置构建环境，测试文件可直接在浏览器中打开运行。
- 适合小型项目或偶尔维护的代码，降低测试门槛。
- 快速编写（作者耗时不到10分钟），但能有效捕捉bug并提供回归保障。

作者承认这不是原创想法，类似QUnit也支持浏览器运行，但强调对于他的简单需求，自定义极简方案已足够。整体上，这是一种务实、轻量的测试策略，尤其适合纯JavaScript的个人项目。
