# Bootstrapping HTTP/1.1, HTTP/2, and HTTP/3
- URL: https://www.netmeister.org/blog/http-123.html
- Added At: 2025-05-29 14:30:03
- [Link To Text](2025-05-29-bootstrapping-http-1.1,-http-2,-and-http-3_raw.md)

## TL;DR


HTTP协议升级历经HTTPS（通过301重定向、HSTS预加载及HTTPS DNS记录降级风险）、HTTP/2（ALPN协议协商与Alt-Svc头）、HTTP/3（基于QUIC需新建连接，各浏览器策略各异如Chrome竞速机制）等阶段。现代协议依赖TLS扩展、DNS记录和客户端策略，复杂度远超基于TCP的早期机制。

## Summary


文章内容围绕HTTP协议的版本切换与安全升级过程，具体描述如下：

### 从HTTP到HTTPS的升级
1. **3xx重定向**：服务器通过返回301状态码（永久重定向）引导客户端切换HTTPS，需新增TCP连接和TLS握手，导致额外延迟。  
2. **HSTS头（HTTP严格传输安全）**：  
   - 服务器返回HSTS头，告知客户端未来仅使用HTTPS连接，但首次HTTP请求可能仍被拦截修改。  
   - 浏览器通过静态HSTS预加载列表（如`hstspreload.org`）强制指定域名始终使用HTTPS，若子域名未预加载可能导致意外HTTP拒绝。  
3. **HTTPS DNS记录**：添加`HTTPS` DNS记录，通过`alpn`参数（如`h3,h2`）直接提示客户端支持协议，减少多次握手。

---

### 从HTTP/1.1到HTTP/2的升级
1. **ALPN扩展**：在TLS握手阶段，客户端通过ALPN（RFC7301）协商协议（如HTTP/2），确保当前连接使用目标协议。  
2. **Alt-Svc头（备用服务）**：服务器声明支持HTTP/2和HTTP/3协议，客户端后续连接可直接使用该协议，但需依赖自身缓存。  
3. **HTTPS DNS记录与浏览行为**：添加`alpn="h2"`参数后，客户端可直接选择HTTP/2。部分浏览器（如Chrome/Firefox）利用该记录加速协议选择。

---

### 从HTTP/2到HTTP/3的升级
1. **协议切换限制**：HTTP/3基于QUIC协议，无法通过现有TCP连接的ALPN升级，需新建QUIC/UDP连接。  
2. **客户端处理策略**：  
   - **Chrome**：采用QUIC-TCP竞速机制（Parallel QUIC/TCP Connection），并行尝试两种协议后选择更快的（多为HTTP/3），失败则回退。  
   - **Firefox**：需启用DNS-over-HTTPS（DoH），若通过`HTTPS`记录获取到`alpn="h3"`则直接使用，否则回退。  
   - **Safari**：优先直接使用HTTP/3，失败后才使用HTTP/2。  
3. **注意事项**：  
   - 需通过QUIC内的ALPN协商当前连接协议，或通过`Alt-Svc`和`HTTPS`记录指导未来连接。  
   - 部分代理（如Tor）因不支持UDP阻碍HTTP/3使用。

---

### 协议升级策略总结
- **当前连接**：通过TLS握手时的ALPN协议协商激活指定协议（HTTP/2需ALPN，HTTP/3需QUIC内的ALPN）。  
- **未来连接**：利用`Alt-Svc`头或`HTTPS` DNS记录的`alpn`参数提供协议提示，优化初次连接效率。  
- **复杂性提升**：现代HTTP协议需结合DNS、TLS扩展及客户端策略，与早期基于TCP的简单机制相比更为复杂。
