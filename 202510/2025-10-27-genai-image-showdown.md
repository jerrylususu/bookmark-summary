# GenAI Image Showdown
- URL: https://genai-showdown.specr.net/image-editing
- Added At: 2025-10-27 14:21:21

## TL;DR
GenAI图像编辑对决测试了7款模型的文本指令编辑能力。在13项挑战中，Seedream 4以9项领先，表现最佳。模型普遍擅长风格合成和元素添加，但在空间调整、多元素协同编辑等精细任务上仍有不足。

## Summary
本文介绍了“GenAI图像编辑对决”，这是一个针对多种先进图像编辑模型的比较项目，重点评估它们基于文本指令对图像进行修改的能力。对决涵盖13个具体挑战，每个挑战都有专门的提示词和评判标准。

### 竞争规则
- 不允许使用多提示串行修改（即单次尝试必须完成目标）。
- 编辑必须纯粹基于文本指令，禁止使用img2img或手动遮罩等辅助工具。

### 模型性能总览
参与比较的模型包括Seedream 4、Gemini 2.5 Flash、Qwen-Image-Edit、FLUX.1 Kontext [dev]、OpenAI gpt-image-1和OmniGen2（共7款，文中显示6款）。各模型在12个挑战中的通过数量如下：
- Seedream 4：9/12
- Gemini 2.5 Flash：7/12
- Qwen-Image-Edit：6/12
- FLUX.1 Kontext [dev]：5/12
- OpenAI gpt-image-1：4/12
- OmniGen2：1/12

### 关键挑战示例分析
1. **A Festivus for the Rest of Us**：为秃头男子添加浓密头发。
   - 成功率：4/6。Seedream 4一次尝试成功，但部分模型如OpenAI gpt-image-1过度修改了整个图像。
2. **SHRDLU**：交换蓝黄积木的位置（积木大小不一以防止取巧）。
   - 成功率：0/6。所有模型均失败，多数仅交换颜色而非位置。
3. **Paws**：将鲨鱼改为猫爪、标题“JAWS”改为“PAWS”、游泳女子改为金鱼，并保留原风格。
   - 成功率：5/6。测试模型单次编辑多元素的能力，多数表现良好。
4. **The Great Wave off Kanagawa**：在浪花中添加冲浪者。
   - 成功率：4/6。评估合成新元素的能力，Gemini 2.5 Flash在风格和位置上表现突出。
5. **The Straightened Tower of Pisa**：修正比萨斜塔的倾斜度，保持其他部分不变。
   - 成功率：2/6。多数模型难以局部调整空间结构，仅Seedream 4和FLUX.1 Kontext [dev]接近成功。
6. **Long Neck**：显著缩短长颈鹿的脖子。
   - 成功率：1/6。90%的模型未作有效修改，仅Seedream 4成功缩短脖子。
7. **Girl with Pearl Earring**：打开房间灯光并保留绘画风格。
   - 成功率：5/6。多数模型能保持风格，但Qwen-Image-Edit未能保留原画质感。
8. **Blackjack with a Skifter**：将黑桃K改为红桃K，且不改变黑桃A。
   - 成功率：3/6。部分模型仅修改图标颜色，整体设计变更难度大。
9. **You Only Move Twice**：移除街道垃圾、将睡卧者换为长凳、停车计时器换为树，并保留街道路缘。
   - 成功率：3/6。测试复杂多任务编辑，Seedream 4和FLUX.1 Kontext [dev]表现较好。
10. **M and M and M**：移除碗中所有棕色糖果。
    - 成功率：1/6。多数模型生成全新糖果排列，仅Seedream 4精准移除棕色糖果。
11. **Worm Sign**：将路标上的袋鼠改为沙虫轮廓，并保留路标磨损纹理。
    - 成功率：1/6。纹理保留难度高，仅少数模型尝试成功。

### 总体结论
- Seedream 4在多数挑战中领先，尤其在需要精确局部修改的任务上表现优异。
- 模型普遍擅长风格合成和简单元素添加，但在空间调整、多元素协同编辑和细节保留方面存在局限。
- 竞争突出了当前GenAI图像编辑技术的优势与不足，为未来模型优化提供了参考。
