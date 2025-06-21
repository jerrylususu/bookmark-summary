# Decoding Google: Converting a Black Box to a White Box
- URL: https://brutecat.com/articles/decoding-google
- Added At: 2025-06-21 09:29:14
- [Link To Text](2025-06-21-decoding-google-converting-a-black-box-to-a-white-box_raw.md)

## TL;DR


本文介绍了逆向解析Google黑箱系统的实用技术，涵盖网页端API密钥认证、安卓模拟获取令牌及签名绑定、X-Goog-Spatula头伪造客户端权限，以及利用API错误消息逆向参数定义的自动化方法。同时指出因验证机制缺陷及测试接口文档泄露等遗留问题存在的安全隐患。

## Summary


本文介绍了通过逆向工程将Google复杂系统（“黑箱”）转化为可分析的“白箱”的方法，主要包括以下技术手段：

---

### **网页版API认证机制**
- **API密钥作用**：通过`X-Goog-Api-Key`头调用内部API（如Internal People API），需搭配用户Cookie及`SAPISIDHASH`进行身份验证。
- **权限关联性**：不同密钥绑定至不同Google Cloud项目，仅有授权项目可访问。例如某密钥仅能访问测试环境（staging），需添加`Referer`头验证来源。
- **测试环境文档泄露**：公开和测试API的发现文档（discovery documents）存在差异，测试版曾包含详尽注释说明功能逻辑，但后续被移除。

---

### **“秘密”可见性标签**
- **隐藏端点暴露**：某些内部API需附加`labels`参数（如`?labels=PANTHEON`）才能访问受保护的端点或接口文档。
- **客户端特定权限**：特定客户端（如Google Chat应用）通过其项目的密钥或Spatula头可获得额外API权限，需匹配对应的包名和SHA1签名。

---

### **安卓系统的API认证**
- **Android Refresh Token获取**：通过模拟设备访问`https://accounts.google.com/EmbeddedSetup`，获取匿名`oauth_token`后，向`android.googleapis.com`发送POST请求交换得到`aas/xx`刷新令牌。
- **Bearer Token生成**：使用上述刷新令牌及目标应用的包名（如`com.google.android.play.games`）、签名哈希（`client_sig`）和所需范围（`scopes`），生成具备特定项目上下文的访问令牌。
- **签名源**：开发者收集了Google应用的包名及对应的`client_sig`值，并提供工具（如`aas-rs`）进行暴力测试以寻找兼容签名。

---

### **X-Goog-Spatula头机制**
- **验证旁路**：该头为无密钥认证，包含安卓应用的包名及签名信息（Base64编码的Protobuf），利用其可冒充合法客户端访问受保护API（如`gameswhitelisted.googleapis.com`）。
- **无有效验证**：尽管部分客户端需DroidGuard验证，但目前未严格执行，允许伪造包名及签名组合以获取不同项目权限。

---

### **通过错误消息逆向API参数**
- **参数类型推断**：在Protobuf格式的API请求中，故意传入非法值（如将`browse_id`设为布尔值）触发错误，根据响应信息推导参数名称、数据类型及字段索引。
- **自动化工具辅助**：`req2proto`工具通过发送结构化测试数据并解析错误响应，自动生成API请求的Protobuf定义文件，加快逆向进程。

---

### **其他关键点**
- **API密钥局限性**：需确保密钥所属项目已启用目标API。如调用Play Atoms Private API需先在其控制台启用。
- **客户端上下文**：安卓请求中应用的范围和权限由包名及签名决定。工具`gapi-service`可用于自动检测所需权限范围。
- **安全漏洞风险**：遗留的测试接口或标签参数可能包含未公开功能，存在潜在的安全弱点，需持续监控Google的更新。
