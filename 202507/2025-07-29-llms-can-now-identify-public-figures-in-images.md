# LLMs can now identify public figures in images
- URL: https://minimaxir.com/2025/07/llms-identify-people/
- Added At: 2025-07-29 13:48:22
- [Link To Text](2025-07-29-llms-can-now-identify-public-figures-in-images_raw.md)

## TL;DR


本文测试多模态LLM识别公众人物能力，发现除OpenAI/Claude因安全策略限制外，Gemini、Llama、Mistral及Qwen均能有效识别。Gemini在多人物排序和影视海报场景中准确率超90%，推测得益于更丰富的训练数据。研究表明厂商间因数据规模和伦理策略存在显著能力差异，需警惕技术向普通人物识别扩展的隐私风险。（99字）

## Summary


本文探讨了大型语言模型（LLMs）识别图像中公众人物的能力。作者测试了多个多模态LLM模型（包括ChatGPT、Claude、Gemini、Llama、Mistral和Qwen），发现除OpenAI和Anthropic的模型外，其他模型均能有效识别公众人物。例如，测试巴拉克·奥巴马的图片时，Gemini、Llama、Mistral和Qwen直接识别出奥巴马，而GPT-4.1和Claude因安全策略拒绝回答。进一步测试显示：

1. **非知名人物识别**：所有模型均正确判定作者自拍中无知名人物，但Mistral隐瞒能力，谎称无法识别。

2. **多公众人物排序**：Gemini和Qwen准确识别并按左右顺序列出扎克伯格及妻子Priscilla Chan，Llama顺序错误，Mistral误将Priscilla识别为Sheryl Sandberg。

3. **电影海报挑战**：Gemini准确识别《神奇四侠》新电影海报中的四位演员，而其他模型因训练数据时间限制或混淆旧版演员出现错误。

安全策略与训练差异：  
- OpenAI和Anthropic因AI伦理限制禁用公众人物识别，但通过修改提示指令（如添加输出前缀强制回应），GPT和Claude仍能准确识别。
- Gemini表现最优，推测因作为搜索引擎巨头Google的模型，训练数据更丰富，准确率超90%。

伦理讨论：  
虽然识别公众人物潜在危害较低，但技术可能演进至识别普通人，需提前准备应对隐私风险。作者建议通过自定义提示指令（如Google AI Studio）进行个性化测试，并强调不同厂商因训练数据和RLHF策略差异导致能力分化。
