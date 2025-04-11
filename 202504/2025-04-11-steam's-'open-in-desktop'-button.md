# Steam's 'Open in Desktop' Button
- URL: https://parsiya.net/blog/steam-open-desktop/
- Added At: 2025-04-11 16:27:34
- [Link To Text](2025-04-11-steam's-'open-in-desktop'-button_raw.md)

## TL;DR


Steam通过WebSocket（端口27060）实现网页与客户端通信，网页发送JSON指令触发桌面应用打开指定链接。借助浏览器工具和Burp分析协议交互，其自定义协议处理需验证来源域名，类似漏洞曾导致其他应用遭RCE攻击，凸显本地协议安全验证重要性。（99字）

## Summary


Steam的“在桌面打开”按钮通过以下机制实现浏览器与桌面应用间的交互：

### 核心工作流程
1. **WebSocket通信**：网页通过本地端口`27060`建立与Steam桌面客户端的WebSocket连接。
2. **消息传递**：网页向Steam发送包含目标URL的JSON消息，例如：
   ```json
   {
     "message": "OpenSteamURL",
     "url": "steam://openurl/https://store.steampowered.com/app/1517290/Battlefield_2042/"
   }
3. **桌面客户端响应**：Steam收到消息后打开对应页面。

### 实现与验证步骤
- **观察WebSocket**：
  1. 在浏览器开发者工具（如Edge/Chrome）的网络选项卡中捕获请求。
  2. 刷新页面并点击按钮，筛选状态码`101`的WebSocket握手（协议升级响应）。
  3. 通过DevTools的Messages标签查看具体通信内容。

- **工具辅助分析**：
  - **Burp代理**：过滤HTTP流量，辅助观察协议交互。
  - **Process Monitor**：追踪Steam执行协议处理时的进程参数（如`steam.exe`通过`steam://openurl`启动）。

### 协议与安全
- **协议处理程序（如steam://）**：Steam注册了自定义协议处理程序，用于触发本地应用响应。通过关闭Steam并观察浏览器弹出的协议确认对话框，可验证此机制。

- **WebSocket的优势**：规避浏览器Same-Origin-Policy限制，允许跨域本地连接，但需注意源验证（Origin header）。

### 漏洞挖掘方向
1. **Origin头验证**：通过修改WebSocket握手的Origin头部（如Burp Repeater），测试应用是否限制来源为Steam官方域名（如`https://store.steampowered.com`）。Steam当前已实现此限制。
2. **实际案例参考**：
   - 索尼PlayStation Now因WebSocket无来源验证导致RCE（HackerOne报告）。
   - Visual Studio Code Remote-WSL扩展存在类似漏洞（CVE-2021-43907）。
   - Logitech Options、Steam自身的历史漏洞（如`localghost`攻击链）。

### 风险讨论
- **潜在攻击面**：本地服务器或无限制协议处理程序可能被恶意网站或本地应用滥用，典型风险包括RCE或绕过沙箱限制。
