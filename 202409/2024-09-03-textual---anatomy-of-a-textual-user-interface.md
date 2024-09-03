# Textual - Anatomy of a Textual User Interface
- URL: https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/
- Added At: 2024-09-03 14:30:15
- [Link To Text](2024-09-03-textual---anatomy-of-a-textual-user-interface_raw.md)

## TL;DR
本文介绍了作者开发的一个终端AI聊天TUI，灵感来自电影《异形》中的AI角色Mother。详细讲解了代码结构、依赖项、UI组件定义、布局样式、事件处理及应用运行方法，并提供了完整代码链接和社区讨论邀请。

## Summary
1. **简介**：
   - 作者开发了一个在终端中与AI代理聊天的文本用户界面（TUI），灵感来自电影《异形》中的AI角色Mother。

2. **代码剖析**：
   - **顶部样板代码**：
     - 包含Python版本和依赖项（如`llm`和`textual`）的声明。
     - 导入必要的模块，定义系统提示`SYSTEM`。
   - **依赖项声明**：
     - 使用内联方式指定依赖项，便于工具自动设置环境。
   - **导入模块**：
     - 导入`textual`用于UI，`llm`用于与ChatGPT等LLM通信。

3. **UI组件定义**：
   - **Prompt和Response类**：
     - 定义用于显示用户输入和LLM响应的组件，继承自内置的`Markdown`组件。
   - **MotherApp类**：
     - 定义应用的布局和样式，使用TCSS（Textual Cascading Style Sheets）进行样式定义。
     - 设置`AUTO_FOCUS`属性，使应用启动时焦点位于`Input`组件。

4. **布局和样式**：
   - **布局定义**：
     - 使用`compose`方法添加初始组件，如`Header`、`VerticalScroll`、`Input`和`Footer`。
     - `VerticalScroll`容器自动添加滚动条，预填充欢迎消息。
   - **样式定义**：
     - 使用TCSS定义组件的外观，如背景色、边框等。
     - 可以通过代码或CSS表达样式。

5. **事件处理**：
   - **on_mount方法**：
     - 在应用挂载时获取LLM模型对象。
   - **on_input方法**：
     - 处理用户在`Input`组件中提交的输入，清空输入框，添加用户输入和LLM响应的组件。
   - **send_prompt方法**：
     - 使用`@work`装饰器将方法变为线程化工作，发送提示并逐块接收LLM响应，更新UI。

6. **运行应用**：
   - 创建`MotherApp`实例并运行，可能需要设置OpenAI API密钥。

7. **附加信息**：
   - 提供完整代码链接，建议使用`uv`工具运行脚本。
   - 邀请加入Discord服务器讨论相关话题。
