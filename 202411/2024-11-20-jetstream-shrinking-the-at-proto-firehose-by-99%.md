# Jetstream: Shrinking the AT Proto Firehose by >99%
- URL: https://jazco.dev/2024/09/24/jetstream/
- Added At: 2024-11-20 14:05:18

## TL;DR
Bluesky的AT Proto firehose流量因巴西禁令激增，导致基础设施压力增大。为解决此问题，开发了Jetstream，通过轻量级JSON转换和过滤，显著减少带宽和存储需求，使在廉价云基础设施上运行成为可能。

## Summary
1. **背景**：
   - **活动激增**：由于巴西禁止Twitter，Bluesky的AT Proto事件流（firehose）流量激增，平均事件率增加了约1,300%。
   - **流量增加**：在活动激增前，firehose每天产生约24 GB的流量，激增后增加到超过232 GB/天。

2. **问题**：
   - **基础设施压力**：在廉价的云基础设施上，保持与完整验证的firehose同步变得不切实际。

3. **解决方案**：
   - **Jetstream**：为了减轻操作机器人、feed生成器、标签器等非验证AT Proto服务的负担，开发了Jetstream，这是一个轻量级的、可过滤的JSON firehose。

4. **Firehose工作原理**：
   - **机制**：AT Proto firehose用于保持所有用户repo的验证、完全同步副本。
   - **Merkle Search Trees (MST)**：每个firehose事件包含用户MST的更新，包括从根到修改叶的所有更改块。
   - **验证**：路径的根由repo所有者签名，消费者可以通过应用事件中的差异来保持repo的MST更新。

5. **Jetstream工作原理**：
   - **转换**：Jetstream消费AT Proto的`com.atproto.sync.subscribeRepos`流，并将其转换为轻量级的、友好的JSON。
   - **过滤**：Jetstream丢弃事件中的所有块，除了叶节点块，通常每个事件只留下一个块。
   - **体积减少**：Jetstream的JSON firehose几乎是完整协议firehose的1/10大小，但缺乏协议级firehose的验证和签名。

6. **性能优化**：
   - **zstd压缩**：通过使用`zstd`压缩，进一步减少带宽消耗。
   - **字典模式**：使用预训练的字典初始化编码器/解码器，以提高压缩效率。
   - **存储优化**：在PebbleDB中存储序列化的JSON和`zstd`压缩的事件，以支持回放。

7. **效果**：
   - **带宽减少**：使用自定义字典后，平均Jetstream事件从482字节减少到211字节（压缩比约为0.44）。
   - **成本降低**：Jetstream可以以每天约850 MB的流量实时跟踪Bluesky的所有帖子，而在巴西Twitter禁令周末期间，所有事件的流量从232 GB/天减少到18 GB/天。

8. **总结**：
   - **资源节省**：Jetstream通过压缩和过滤，显著减少了带宽和存储需求，使得在廉价基础设施上运行成为可能。
