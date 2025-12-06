# Fizz Buzz in CSS - Susam Pal
- URL: https://susam.net/fizz-buzz-in-css.html
- Added At: 2025-12-06 09:52:11
- Tags: #read #hack #frontend
- [Link To Text](2025-12-06-fizz-buzz-in-css---susam-pal_raw.md)

## TL;DR
本文介绍仅用CSS实现Fizz Buzz序列的4行代码方案。通过CSS计数器、伪元素和选择器组合，在特定倍数项显示数字和替换文本。作者鼓励尝试更简洁的写法，并提供了参考链接。

## Summary
本文探讨了如何使用CSS实现Fizz Buzz序列，要求所有输出内容必须直接来自CSS，不允许在HTML或JavaScript中添加。作者提出了一种简洁的解决方案：利用CSS计数器（`counter-increment`）和伪元素（`::before`、`::after`）结合选择器（如`:nth-child`）生成序列。具体代码只有4行，通过伪元素在列表项前显示数字或"Fizz"，在特定倍数项后添加"Buzz"。

完整示例如链接所示。作者提到，虽然代码可压缩成单行以减少字符数（如minify后为152个字符），但这不是重点，更鼓励读者挑战更短方案。文末还附带了相关内容的参考链接。
