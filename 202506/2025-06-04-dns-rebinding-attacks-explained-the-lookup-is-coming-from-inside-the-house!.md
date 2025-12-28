# DNS rebinding attacks explained: The lookup is coming from inside the house!
- URL: https://github.blog/security/application-security/dns-rebinding-attacks-explained-the-lookup-is-coming-from-inside-the-house/
- Added At: 2025-06-04 14:18:06

## TL;DR


DNS重绑定攻击利用浏览器DNS缓存漏洞，通过动态切换域名解析IP地址绕过同源策略，使攻击者可访问受害者本地或内网服务。攻击者可能结合路径遍历漏洞读取配置文件，进而执行代码。防御需强制HTTPS、验证Host头、启用认证并禁用多余服务，需将此类攻击纳入安全防护体系。

## Summary


DNS重绑定攻击通过利用浏览器与DNS协议之间的漏洞，绕过同源策略（SOP），使攻击者通过普通网页访问本地或内网Web服务。攻击流程包括：  
1. **攻击原理**：  
   - 攻击者控制DNS响应，先返回公网IP加载恶意脚本，随后切换到本地内网IP（如127.0.0.1或局域网IP）。  
   - 浏览器误判为同一域名，允许脚本访问本地服务，绕过跨域限制。  

2. **漏洞场景**：  
   - **Deluge WebUI案例**：  
     - 未认证的`/js`端点存在路径遍历漏洞，攻击者可构造`/js/deluge-all/..%2F../..%2Fweb.conf`等路径读取配置文件。  
     - 配置文件中包含密码哈希（SHA1）和会话信息，可暴力破解密码或直接利用会话劫持。  
     - 进一步结合CVE-2017-7178漏洞安装恶意插件，实现远程代码执行。  

3. **绕过防护手段**：  
   - 利用浏览器DNS缓存失效或工具（如Singularity）自动化发起攻击。  
   - 针对支持CORS-RFC1918的浏览器，绕过其隔离策略（如0.0.0.0地址欺骗Linux/macOS系统）。  

4. **防御措施**：  
   - **强制HTTPS**：TLS握手时证书需匹配域名，阻止本地服务欺骗。  
   - **Host头验证**：拒绝非预期的Host值（如攻击域名非允许列表内）。  
   - **严格认证**：即使本地服务也启用加密认证，避免依赖“仅内网部署”假设。  
   - **禁用不必要服务**：关闭不必要的本地公共端点，避免暴露路径遍历漏洞。  

该攻击暴露了浏览器安全机制与网络协议的深层冲突，需将DNS重绑定纳入威胁模型，确保本地服务与浏览器交互的安全边界。
