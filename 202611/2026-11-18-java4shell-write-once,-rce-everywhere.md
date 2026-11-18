# Java4Shell: Write once, RCE everywhere
- URL: https://calif.io/java4shell
- Added At: 2026-11-18 15:30:23
- Tags: #read #security

## TL;DR
文章披露 Java4Shell：HotSpot x86-64 Base64 intrinsic 因 padding 掩码错误造成固定字节堆越界写，可升级为堆泄漏、任意写和 RCE；影响多版本 JDK，但利用依赖堆布局、时序和定制链，建议升级或禁用该 intrinsic。

## Summary
这篇文章讲的是 OpenJDK HotSpot 中 x86-64 Base64 intrinsic 的一个越界写漏洞，作者把它命名为 **Java4Shell**。它的核心不是 Java 应用层逻辑漏洞，而是 JVM 的 JIT 编译器在把 Base64 解码热路径编译成使用 AVX-512 的本地代码后，尾部 padding 掩码计算错误，导致固定内容的堆越界写。文章进一步把这个“只能写固定字节、位置可控”的弱点发展成堆泄漏、任意写，最终远程代码执行。

漏洞的技术本质在 Base64 解码 intrinsic 的小输入路径。解码器处理小于 64 字节的尾部时，会用 `evmovdqub`/`VMOVDQU8` 和 64 位掩码决定哪些字节写入内存。掩码原本根据输入长度和输出长度计算，再根据 `'='` padding 调整。问题是：当剩余输入形如 `=、==、X=、X==、XY=、===` 时，输出长度可能先算成 0，再因 padding 被减成 `-1` 或 `-2`。随后用于生成掩码的 `bzhiq(-1, output_len)` 在长度大于等于 64 时不会截断任何位，结果得到全 1 掩码，于是 `evmovdqub` 一次写入 64 字节。比如 65 字节输入 `[64 字节] + '='` 会分配约 50 字节输出缓冲区，但写入从偏移 48 开始写 64 字节，造成越界。文章还提到 JDK 17 上触发长度阈值更高，可能需要 `'A' * 128 + '='`。

这个写原语本身很弱：只有写入落点可控，写入内容大部分不可控。起始字节有少量可控，后面特别是偏移 48 到 63 的字节固定为 `0x9a`。所以作者没有直接拿它打代码指针，而是采用类似 JavaScript 引擎利用中的经典思路：先覆盖相邻数组的长度字段，把数组变成 `writer`。长度被放大后，这个数组就能用攻击者选择的字节进行有界线性写。再用类似方法覆盖另一个数组的长度，让它越界读并把内容带回 HTTP 响应，形成 `reader`，从而泄漏 Java 堆内容。作者把这种堆泄漏能力称为 **JavaBleed**，可能泄露 PII、私钥、令牌等敏感数据。

在获得 `writer` 和 `reader` 后，利用链会修复被破坏的对象以维持 JVM 运行，对应用逻辑做 data-only 攻击，再逐步把有界写升级为任意写，最终触达 Code Cache 或 JVM hooks 实现代码执行。文章强调，具体到某个产品的武器化利用链暂时不公开，等大家升级后再发布。

远程利用的关键是堆布局。HotSpot 的 G1 GC 把堆划分成固定大小 region，而每个 Java 线程默认有自己的 TLAB，导致不同请求线程分配的 Base64 缓冲、writer、reader 不在可预测顺序里。作者通过控制数组大小和 TLAB 剩余空间，影响对象是走 TLAB 内分配还是 outside-TLAB 分配；再用 spray and pray 喷洒多组 writer/reader，让解码输出有较大概率落在目标 region 下方。远程场景下，他们把 HTTP 请求分段发送，等到关键堆分配即将发生时再发剩余部分，并利用 TCP ACK 控制时序。攻击对 RTT 和抖动敏感，所以作者在同一区域租 VM 来提高稳定性。nginx 默认缓冲请求体会破坏这种分段释放；Elasticsearch 这种一次性完整请求的链路不受该设置影响；WebSocket 升级后的帧也可以绕过请求体缓冲。

文章把利用流程概括为：WARM 预热让 JIT 选中受影响快速路径；REHEARSE 可选校准；TRIGGER 发送畸形尾部触发越界；DISCLOSE 通过 writer 扩大 reader 并收集响应中的堆字节；REPAIR 恢复被临时破坏的对象；FINISH 执行应用特定修改并验证。限制也很明确：没有通用 payload，每个目标都需要定制 profile，包括解码路由、可用的 writer、能回显的 reader、堆布局和应用动作。因此标题里的 “Write once, RCE everywhere” 更偏向营销式概括：漏洞代码普遍存在于受影响 JDK 中，但实际利用不是 point-and-shoot。

影响范围方面，文章称 OpenJDK 17.0.6 及更新版本受影响，多个基于 OpenJDK 的发行版也受影响，包括 Amazon Corretto、Eclipse Temurin、Microsoft Build of OpenJDK、Azul Zulu、BellSoft Liberica、SAP SapMachine、Red Hat OpenJDK、Oracle OpenJDK、Oracle Java SE、Oracle GraalVM for JDK 等。Oracle 列出了若干受影响版本。硬件条件也很关键：需要 x86-64 且支持 AVX-512 VBMI，ARM64 不受影响；常见满足条件的有 Intel Ice Lake、Sapphire Rapids、Emerald Rapids、Granite Rapids，以及 AMD Zen 4 或更新的 EPYC/Ryzen。Linux 上可检查 CPU flags 是否包含 `avx512f`、`avx512bw`、`avx512vbmi`、`bmi2`。

修复建议是立即升级到包含补丁的版本。临时缓解可以启动参数 `-XX:-UseBASE64Intrinsics` 禁用硬件加速 Base64，或在 x86-64 上使用 `-XX:UseAVX=2` 禁用 AVX-512；后者在 ARM 上不识别，不能乱用。文章还提供了一个有界 PoC：预热解码器后把畸形 `64 × "A" + "="` 解码进 4096 字节数组，受影响环境会打印 `REPRODUCED`，实际越界写落在真实数组内部，不会破坏堆外内存。

整体看，这篇文章的价值在于展示了一个 JIT intrinsic 中掩码计算错误如何从“固定字节越界写”升级为堆泄漏和 RCE，同时也说明现代 Java 利用的难点已经从单纯找内存破坏，转移到堆布局、远程时序和应用特定链的工程化上。它的影响面广，但利用条件并不低，不能简单理解为所有 Java 服务都能被同一个 payload 直接打穿。
