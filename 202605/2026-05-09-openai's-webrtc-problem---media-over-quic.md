# OpenAI's WebRTC Problem - Media over QUIC
- URL: https://moq.dev/blog/webrtc-is-the-problem/
- Added At: 2026-05-09 13:15:21
- Tags: #read #backend

## TL;DR
本文批评OpenAI在语音AI中使用WebRTC，指出其在产品适配、缓冲、扩展性等方面存在根本问题，主张短期用WebSocket、长期采用基于QUIC的协议（如MoQ）作为更优替代方案。

## Summary
这篇文章批评了OpenAI在语音AI中使用WebRTC的做法，并主张采用基于QUIC的协议（如MoQ）作为替代方案。作者从自身在Twitch和Discord开发WebRTC SFU的经验出发，指出WebRTC存在多个根本性问题：

1. **产品适配性差**：WebRTC为实时音视频会议设计，会为了低延迟主动丢包，这不适合语音AI场景。用户更希望等待稍长但准确的响应，而非接受被降级的音频。
2. **缓冲机制不足**：WebRTC缺乏有效缓冲，依赖到达时间渲染，导致语音生成（快于实时）时需人为引入延迟并可能丢包，降低质量。
3. **端口与扩展性问题**：WebRTC依赖多端口和复杂协议（如STUN、DTLS），在大规模部署时面临端口耗尽、防火墙阻挡和Kubernetes兼容性问题。OpenAI的负载均衡方案是必要但临时的“黑客”手段。
4. **连接建立缓慢**：WebRTC连接需多次RTT（约8次），即使服务器同地也需冗余握手，影响用户体验。
5. **协议碎片化**：WebRTC由45个RFC和草案组成，实现复杂且受Google主导，迫使应用（如Discord） fork协议或依赖原生客户端。

作者建议替代方案：
- **短期**：使用WebSocket流式传输音频，利用现有TCP/HTTP基础设施，简化部署。
- **长期**：采用基于QUIC的协议（如MoQ），因为QUIC具有以下优势：
  - 连接建立仅需1次RTT（QUIC+TLS）。
  - 使用`CONNECTION_ID`实现无状态负载均衡，避免依赖共享状态（如Redis）。
  - 支持Anycast+Unicast混合部署，无需独立负载均衡器，提升全球扩展性。

结论：WebRTC不适合语音AI，QUIC能更好解决产品、负载均衡和扩展性问题。作者承认OpenAI团队面临压力，但认为WebRTC是“明显但错误的选择”，并幽默地将WebRTC比作“Jared Leto”（常被批评的演员）。
