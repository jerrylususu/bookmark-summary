# Interactive Git Log - Visual Studio Marketplace
- URL: https://marketplace.visualstudio.com/items?itemName=interactive-smartlog.interactive-smartlog
- Added At: 2024-11-24 04:32:48

## TL;DR
Interactive Git Log (IGL) 是一款VSCode插件，通过图形界面简化Git操作，包括文件变更显示、分支管理、冲突解决和提交堆栈编辑，显著提升开发效率。

## Summary
1. **产品简介**：
   - Interactive Git Log (IGL) 是一款为VSCode设计的强大Git图形用户界面，旨在简化并增强用户与Git仓库的交互。

2. **主要功能**：
   - **自动文件变更显示**：
     - 工作副本中的文件变更会自动显示在IGL中，类似于运行`git status`。
     - 提供**Commit**和**Amend**按钮，点击后可在右侧边栏编写详细的提交信息。
   - **分支管理**：
     - 显示从主远程分支（通常是`origin/main`或`origin/master`）分叉的提交和分支的树形视图。
     - 支持直接点击分支标签切换分支，并可直接在IGL中添加、删除和获取分支。
   - **未提交变更**：
     - 文件旁边的颜色和图标显示文件的修改状态（修改、添加或删除）。
     - 文件名的不透明度表示文件是否已暂存（通过`git add`）。
     - 悬停文件时，IGL会动态显示一组可操作按钮，方便执行Git命令，如暂存、取消暂存、还原修改或删除新添加的文件。
   - **重基与冲突解决**：
     - 悬停分支时显示重基按钮，点击后将当前分支重基到目标分支。
     - 检测到合并冲突时，IGL会在未提交变更列表中添加未解决冲突的文件。
     - 打开每个文件并解决冲突标记后，点击IGL中每个文件旁边的加号图标标记为已解决。
     - 命令运行时，底部屏幕会显示进度信息和错误消息。
   - **提交堆栈编辑**：
     - 在具有多个提交的分支上，会出现**Edit stack**按钮。
     - 点击后打开对话框，可重新排序、压缩和删除提交。
     - 点击**Save changes**触发IGL运行git交互式重基以编辑堆栈。

3. **总结**：
   - IGL通过提供直观的图形界面和丰富的功能，极大地简化了Git操作，特别是对于分支管理、冲突解决和提交堆栈编辑等复杂任务。
