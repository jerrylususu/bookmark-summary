# The Claude Code Source Leak: fake tools, frustration regexes, undercover mode, and more
- URL: https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/
- Added At: 2026-04-01 13:48:04
- Tags: #read #agent #deepdive

## TL;DR
Anthropic因意外泄露Claude Code源代码，暴露了反蒸馏机制、隐蔽模式等技术细节及未发布产品KAIROS，核心损害在于泄露战略路线图，而非代码本身。

## Summary
文章分析了Anthropic因意外发布源映射文件而泄露Claude Code源代码的事件，揭示了以下关键内容：

1. **反蒸馏机制**：通过注入虚假工具和服务器端摘要来污染训练数据，但技术绕过相对容易，主要依赖法律手段保护。
2. **隐蔽模式**：强制AI隐藏内部代号和身份，防止在开源项目中暴露AI痕迹，且无法强制关闭。
3. **挫败感检测**：使用正则表达式识别用户负面情绪，以低成本替代LLM推理。
4. **原生客户端认证**：通过Bun的Zig层HTTP栈在请求中注入哈希值，验证客户端真实性，但存在绕过可能。
5. **资源浪费问题**：每日约25万次API调用因自动压缩失败而浪费，通过限制连续失败次数解决。
6. **未发布的自主代理模式KAIROS**：包含记忆蒸馏、GitHub集成等功能，显示未来产品路线图。
7.其他发现：包括四月愚人节玩笑的宠物系统、终端渲染优化、Zsh安全检查、提示缓存经济性等。

总结指出，泄露的核心损害在于暴露了产品路线图和战略细节，而非代码本身。同时，事件可能源于Anthropic收购的Bun工具链中的已知漏洞。
