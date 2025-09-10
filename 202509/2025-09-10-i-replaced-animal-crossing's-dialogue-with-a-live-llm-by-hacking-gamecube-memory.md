# I Replaced Animal Crossing's Dialogue with a Live LLM by Hacking GameCube Memory
- URL: https://joshfonseca.com/blogs/animal-crossing-llm
- Added At: 2025-09-10 14:01:54
- [Link To Text](2025-09-10-i-replaced-animal-crossing's-dialogue-with-a-live-llm-by-hacking-gamecube-memory_raw.md)

## TL;DR
作者通过逆向工程修改《动物森友会》内存系统，在不触及游戏原始代码的情况下，以Python脚本与模拟器共享内存，成功接入了云端LLM模型，实现了AI驱动动态对话，带来角色实时讨论新闻和群体行为等新玩法。

## Summary
作者通过修改《动物森友会》GameCube版的游戏内存，成功将游戏原本的重复对话系统替换为基于云端大型语言模型（LLM）的动态对话生成系统，而未修改任何原始游戏代码。

项目主要流程如下：

1. **利用游戏源代码**：得益于《动物森友会》反编译社区完成了源代码（C语言）的发布，作者得以分析和修改对话系统相关函数（如`mMsg_ChangeMsgData`），实现文本替换。

2. **内存通信方案**：作者放弃了直接在GameCube上实现网络功能的复杂方案，转而采用“内存邮箱”（Memory Mailbox）技术，即通过Dolphin模拟器在GameCube RAM中预留共享内存区域，实现游戏与外部Python脚本的数据交换。

3. **内存地址定位**：通过反复的内存扫描和冻结测试，作者确定了关键内存地址（如说话者名称地址`0x8129A3EA`和对话缓冲区地址`0x81298360`），使得脚本能够读取对话内容并写入新文本。

4. **游戏控制码处理**：游戏使用专用控制码（类似HTML标签）管理对话格式、暂停、颜色和结束等。作者基于社区文档编写了编解码工具，确保AI生成的文本能正确转换为游戏可识别的字节序列。

5. **AI架构设计**：采用双模型流水线（Writer和Director）分工协作。Writer负责根据角色设定生成创意对话，Director负责添加游戏控制码以调整对话表现形式（如表情、音效和停顿）。

6. **涌现行为与结果**：接入新闻源和共享记忆后，游戏角色开始动态讨论实时事件（如政治新闻）并发展出群体行为（如反Tom Nook运动），但也因新闻源（Fox News）出现了意想不到的阴暗内容。

项目展示了逆向工程、内存操作和AI技术的结合，最终实现了经典游戏与现代AI的无缝交互。所有代码已开源在GitHub上。
