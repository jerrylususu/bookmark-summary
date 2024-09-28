# Things You Didn't Know About GNU Readline
- URL: https://twobithistory.org/2019/08/22/readline.html
- Added At: 2024-09-28 11:48:55
- [Link To Text](2024-09-28-things-you-didn't-know-about-gnu-readline_raw.md)

## TL;DR
GNU Readline是一个强大的命令行编辑库，支持丰富的文本编辑功能和快捷键，可通过自定义配置文件进行个性化设置。由Chet Ramey长期维护，广泛应用于各种命令行工具中。

## Summary
1. **GNU Readline简介**：GNU Readline是一个不起眼的小型软件库，广泛用于命令行界面中的文本编辑和历史命令管理。它由Free Software Foundation在1980年代创建，现由Chet Ramey维护。

2. **功能丰富**：
   - **基本功能**：主要增强命令行界面的单行输入编辑功能，如通过快捷键移动光标、删除文本等。
   - **快捷键**：基于Emacs的快捷键设计，支持多种编辑操作，如删除单词、大小写转换、复制粘贴等。
   - **模式切换**：支持切换到Vim模式，允许用户使用Vim风格的命令进行编辑。

3. **自定义配置**：
   - **配置文件**：通过`~/.inputrc`文件自定义快捷键和行为，如重新绑定`Ctrl-K`删除整行。
   - **宏功能**：可以创建宏来简化常用操作，如自动添加`> output.txt`到命令行。
   - **变量设置**：通过设置变量来调整Readline的行为，如历史搜索和自动补全。

4. **维护者Chet Ramey**：
   - **背景**：Chet Ramey是Case Western Reserve University的高级技术架构师，自1994年起成为GNU Readline和Bash shell的唯一维护者。
   - **历史**：Readline最初是为了实现POSIX规范中的功能而创建的，早期作为Bash的一部分，后来独立成为库。
   - **现状**：Ramey长期无偿维护这两个项目，尽管用户众多，但他继续工作是因为对项目的深度投入和对提供有用软件的热情。

5. **使用示例**：
   - **C程序集成**：通过简单的C代码示例展示了如何在自定义程序中使用Readline库，获取用户输入并进行编辑。
   - **扩展性**：Readline库易于扩展，允许用户通过`~/.inputrc`文件添加新功能和配置。

6. **总结**：GNU Readline是一个强大且灵活的命令行编辑库，广泛应用于各种命令行工具中，通过自定义配置和扩展性，满足不同用户的需求。
