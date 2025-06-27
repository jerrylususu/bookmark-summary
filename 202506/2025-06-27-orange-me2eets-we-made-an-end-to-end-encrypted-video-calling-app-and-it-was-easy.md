# Orange Me2eets: We made an end-to-end encrypted video calling app and it was easy
- URL: https://blog.cloudflare.com/orange-me2eets-we-made-an-end-to-end-encrypted-video-calling-app-and-it-was/
- Added At: 2025-06-27 15:38:32
- [Link To Text](2025-06-27-orange-me2eets-we-made-an-end-to-end-encrypted-video-calling-app-and-it-was-easy_raw.md)

## TL;DR


Cloudflare团队为Orange Meets视频通话实现端到端加密，基于WebRTC和Cloudflare SFU架构。采用MLS协议实现动态组密钥协商，客户端通过Rust编译的WASM模块逐帧加密音视频流，SFU仅中立转发数据。针对VP8编解码器，仅加密关键帧后数据并保留未加密头部以兼容浏览器渲染。通过指定提交者算法和TLA+模型验证确保密钥同步可靠性，服务端仅处理基础状态协调。方案实现安全性与低延迟，相关代码开源验证了无需复杂服务端的高效E2EE视频架构。

## Summary


Cloudflare团队在Orange Meets视频通话应用中实现了端到端加密（E2EE），基于WebRTC和Cloudflare Realtime SFU基础设施。核心设计包括：

**技术实现**  
1. **MLS协议应用**：采用IETF标准的Messaging Layer Security（MLS）协议，实现动态组密钥协商，确保前向安全性和后量子安全性。通过Rust编写WASM加密模块，客户端对音视频流逐帧加密/解密，SFU仅作为中立数据转发节点。

2. **视频编解码适配**：针对VP8编解码器特性，仅加密关键帧（Keyframe）后的数据，保留前1-10字节未加密头信息以避免浏览器渲染错误。

3. **指定提交者算法**：解决用户加入/退出时密钥分发问题。制定「指定提交者」角色（按组内最小索引用户）处理密钥更新操作，通过TLA+模型验证算法在5人组内的正确性，确保协议无状态冲突。

**系统架构**  
- 客户端：负责密钥协商、流加密，通过Web Workers进行计算密集型任务。
- SFU：不感知加密内容，维持低延迟媒体转发。
- 服务端：基于Cloudflare Workers的简单协调器，仅广播通话状态变化，不处理密钥逻辑。

**安全性增强**  
- **安全编号验证**：显示群组加密状态的唯一ID，用户可通过带外验证防止中间人攻击。
- **边缘案例处理**：解决指定提交者失效、用户未同步消息等问题，确保协议鲁棒性。

**挑战与方案**  
1. **编解码兼容性**：加密打破浏览器对媒体流格式的预期，导致画面噪点问题，通过拆分VP8头部解决。
2. **用户加入协议**：避免依赖服务器密钥管理，设计客户端主导的密钥分发流程，降低服务端复杂度。
3. **协议可靠性**：模型检查发现并修复了指定提交者中途失效时的恢复问题，确保密钥同步。

**未来优化方向**  
- 解决JavaScript可信执行问题，探索Web Application Manifest透明日志方案。
- 集成身份提供商（如OpenPubkey）简化密钥验证，增强用户身份绑定。

该实现证明E2EE视频通话能通过标准化协议和客户端侧扩展高效达成，未增加服务端负担，相关代码已开源。
