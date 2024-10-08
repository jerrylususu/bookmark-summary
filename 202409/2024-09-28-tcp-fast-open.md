# TCP Fast Open
- URL: https://dbwu.tech/posts/network/what-is-tcp-fast-open/
- Added At: 2024-09-28 11:47:36
- [Link To Text](2024-09-28-tcp-fast-open_raw.md)

## TL;DR
文章介绍了TCP Fast Open (TFO) 技术，通过在TCP三次握手过程中允许发送数据，减少首次数据发送的延迟。TFO在首次连接时生成并保存TFO Cookie，后续连接中携带该Cookie和数据，实现快速握手。文章还讨论了TFO的优点和局限性，并通过Linux环境下的实验展示了TFO的实现和效果。

## Summary
1. **概述**：
   - 传统的TCP连接建立需要三次握手，且这三次握手只发送`SYN`和`ACK`报文，不携带应用数据。
   - 这种机制导致网络带宽资源利用率低，且在短连接和移动设备场景中，首次发送数据的延迟较大。
   - 使用`TFO`（TCP Fast Open）解决方案可以减少这种延迟。

2. **TFO**：
   - **TCP Fast Open (TFO)**：在传统的三次握手基础上进行优化，允许在握手过程中发送数据，从而减少首次发送数据的延迟。
   - **实现原理**：
     - **首次连接**：
       1. 发送方发送`SYN`报文。
       2. 接收方返回`SYN-ACK`报文，附带一个随机生成的`TFO Cookie`。
       3. 发送方保存`TFO Cookie`，发送`ACK`报文，完成三次握手，开始传输数据。
     - **后续连接**：
       1. 发送方在`SYN`报文中携带`TFO Cookie`和应用层数据。
       2. 接收方验证`TFO Cookie`后，处理数据并返回`SYN-ACK`报文。
       3. 发送方发送`ACK`报文，完成三次握手。
   - **优点**：
     - 发送方和接收方在第一次握手时即可发送和处理数据，减少了1.5个RTT和1个RTT的延迟。
   - **局限性**：
     1. 需要通信双方都支持TFO，否则回退到传统TCP连接。
     2. 增加了接收方的安全攻击面，可能引发安全风险。
     3. 对内核版本有要求，且需要修改内核参数。
     4. 应用数据过大时，TFO的优势不明显。

3. **模拟环境**：
   - 使用两个Linux服务器作为通信发送方和接收方，内核版本要求>=3.7。
   - **内核参数调整**：
     - `0`：关闭TFO。
     - `1`：启用发送方模式TFO。
     - `2`：启用接收方模式TFO。
     - `3`：同时启用发送方和接收方模式TFO。

4. **程序代码**：
   - **接收方 (服务端) 代码**：
     - 初始化服务端监听对象，绑定/监听指定端口，接收客户端的TCP连接。
   - **发送方 (客户端) 代码**：
     - 初始化客户端监听对象，设置TFO选项，向服务端发送数据。

5. **运行程序实验**：
   - **步骤**：
     1. 启动服务端程序，并确认监听状态。
     2. 客户端开始抓包。
     3. 运行客户端程序。
     4. 查看客户端TCP连接状态。

6. **WireShark 抓包结果分析**：
   - **第一次建立连接**：
     - 发送方发送`SYN`报文，接收方返回`SYN-ACK`报文并附带`TFO Cookie`，发送方发送`ACK`报文，完成三次握手。
   - **后续建立连接**：
     - 发送方在`SYN`报文中携带`TFO Cookie`和应用层数据，接收方验证后处理数据并返回`SYN-ACK`报文。

7. **Reference**：
   - [TCP Fast Open](https://datatracker.ietf.org/doc/html/rfc7413)
