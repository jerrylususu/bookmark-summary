# Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide
- URL: https://simonwillison.net/2025/Sep/9/apollo-ai-adoption/
- Added At: 2025-09-09 13:34:38
- [Link To Text](2025-09-09-recreating-the-apollo-ai-adoption-rate-chart-with-gpt-5,-python-and-pyodide_raw.md)

## TL;DR
作者利用GPT-5和Pyodide成功复现阿波罗全球管理公司的AI采用率图表。通过搜索数据源、Python处理和移动平均调整实现精确重现，验证了GPT-5与浏览器端Python数据可视化的能力。

## Summary
作者通过使用GPT-5、Python和Pyodide，成功地复现了阿波罗全球管理公司发布的AI采用率图表。整个过程分为多个步骤：首先，通过GPT-5搜索功能定位到美国人口普查局的原始数据源，下载了包含企业规模和AI采用率的Excel文件；其次，利用GPT-5的代码解释器功能，使用Python（结合pandas和matplotlib）处理数据并生成初始图表，但发现与原始图表存在差异；经检查发现原始图表使用了六期移动平均，调整后最终成功复现了图表；最后，通过Pyodide在浏览器中实现了客户端图表渲染，包括加载数据、运行Python代码并显示图像。

整个过程展示了GPT-5在数据搜索、代码生成和问题解决方面的强大能力，同时验证了Pyodide在浏览器端运行Python数据可视化的可行性。作者总结了几点收获：GPT-5能高效查找复杂数据，代码解释器可准确复现图表，Pyodide简化了浏览器端Python应用开发，并分享了加载外部数据和渲染图像的技术细节。这些方法将在未来项目中继续应用。
