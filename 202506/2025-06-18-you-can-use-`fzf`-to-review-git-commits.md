# You can use `fzf` to review git commits
- URL: https://jvns.ca/til/fzf-preview-git-commits/
- Added At: 2025-06-18 13:21:19
- [Link To Text](2025-06-18-you-can-use-`fzf`-to-review-git-commits_raw.md)

## TL;DR


FZF通过两个非传统用例展示灵活性：1. 结合Git，用自定义Bash脚本实现实时查看提交文件diff，禁用搜索并绑定方向键控制；2. 与JQ配合，创建交互式环境，直接预览JSON处理结果。作者强调，尽管FZF以搜索为核心，但其框架可灵活构建非搜索类界面，彰显工具复用价值。

## Summary


该文章介绍了 FZF 工具的两个非传统用例，展示其灵活性。第一个用例是结合 Git 查看提交记录：通过一个自定义的 Bash 脚本，用户可在左侧滚动浏览提交涉及的文件列表，右侧实时预览对应文件的 diff 内容。脚本通过禁用搜索功能，绑定方向键操作，并利用 `--preview` 参数动态生成预览窗口实现。第二个用例是作为 JSON 处理工具 JQ 的交互式 playground，用户输入 JQ 查询时，右侧窗口会立即显示对指定文件的处理结果。作者强调 FZF 虽以搜索为核心，但其框架可灵活构建非搜索类交互界面，例如上述两个场景，体现了工具的复用价值。
