# Cracking The Dave & Buster’s Anomaly | Rambo Codes
- URL: https://rambo.codes/posts/2025-05-12-cracking-the-dave-and-busters-anomaly
- Added At: 2025-06-05 13:58:53
- [Link To Text](2025-06-05-cracking-the-dave-&-buster’s-anomaly-rambo-codes_raw.md)

## TL;DR


iOS消息应用因语音转录未对"Dave & Buster’s"中的"&"进行HTML实体转义，导致接收端解析失败。BlastDoor安全机制检测到XML格式错误后强制阻断，使消息消失。此设计虽造成功能损失，但通过严格解析规则防止了潜在的内存破坏等攻击，体现了iOS安全优先的设计哲学。

## Summary


iOS消息应用存在一个特殊故障：当发送语音消息包含“Dave and Buster’s”（美式餐饮品牌名称）时，接收端将显示持续数秒的“...”动画后消失，消息无法接收。作者通过iOS 18.5 RC设备复现问题，发现错误根源在于消息转录系统未对“&”符号进行HTML实体转义。  

**问题溯源**：收到消息后，系统日志显示`MessagesBlastDoorService`因`XHTMLParseFailure`报错。分析发现，语音转录文本“Dave & Buster’s”中的“&”未转换为合法HTML实体`&amp;`，导致XML解析失败。BlastDoor安全机制检测到异常后强制中断解析流程，消息因此无法正常显示。  

**技术细节**：苹果BlastDoor服务采用严格的XML/XHTML解析规则（MBDXMLParserContext），要求所有特殊符号必须转义。当转录文本包含未转义的“&”时（如“M&M’s”等品牌名），解析器认为其可能代表HTML实体（如`&lt;`表示<），但因缺少终止分号而判定为无效格式，触发防护机制。  

**安全分析**：该故障并非安全漏洞，而是BlastDoor按设计阻断潜在攻击的结果。宽松的解析策略易被利用（如内存破坏攻击），而苹果通过严格验证数据格式优先保障了系统安全。  

事件揭示了iOS安全架构的保守策略：以功能性损失为代价，防止恶意数据利用解析漏洞入侵系统。
