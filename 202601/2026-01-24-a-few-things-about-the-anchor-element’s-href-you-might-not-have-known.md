# A Few Things About the Anchor Element’s href You Might Not Have Known
- URL: https://blog.jim-nielsen.com/2025/href-value-possibilities/
- Added At: 2026-01-24 04:47:14
- Tags: #read #frontend

## TL;DR
文章探讨了HTML锚元素href属性的多种用法，包括协议链接、特殊值行为（如href="#"滚动到顶部）、数据URL和媒体片段等，作者通过JavaScript测试验证了这些行为的准确性。

## Summary
文章探讨了HTML锚元素（anchor）href属性的各种值及其行为，作者基于研究和测试总结了一些可能不为人知的用法。

- **已知的href值**：包括协议链接如`mailto:`、`tel:`、`sms:`和`javascript:`，用于处理特定操作；协议相关链接（如`href="//"`）；以及文本片段（如`href="#:~:text=foo"`），用于链接到页面特定文本。

- **href="#"**：默认滚动到文档顶部。但如果没有元素有`id="top"`，则`#top`也会滚动到顶部。此外，`#page=`可用于PDF页面深链接（如`my-file.pdf#page42`）。

- **href=""**：重新加载当前页面，保留查询参数（search string），但移除哈希参数（hash string）。例如，从`/path/?id=foo#bar`解析为`/path/?id=foo`。

- **href="."**：重新加载当前页面，移除查询参数和哈希参数。但注意URL结构：如果URL没有尾部斜杠，可能解析到父目录。例如，从`/path`解析为`/`，而从`/path/`解析为`/path/`。

- **href="?"**：重新加载当前页面，移除查询参数和哈希参数，但保留问号字符。不受尾部斜杠影响。例如，从`/path?id=foo`解析为`/path?`。

- **href="data:"**：允许使用数据URL链接到内嵌内容，如文本或HTML数据。需要编码以避免意外行为，例如`href="data:text/plain,hello%20world"`。

- **媒体片段**：如`href="video.mp4#t=10,20"`，可以链接到音频或视频的特定时间段（从10秒到20秒），但浏览器支持有限。

- **测试方法**：作者使用JavaScript的URL构造函数进行验证，并提供了代码片段来测试不同href值的解析行为。所有测试用例均通过，确保准确性。
