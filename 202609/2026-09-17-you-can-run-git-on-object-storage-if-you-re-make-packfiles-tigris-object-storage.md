# You can run git on object storage if you re-make packfiles | Tigris Object Storage
- URL: https://www.tigrisdata.com/blog/objgit-packfiles/
- Added At: 2026-09-17 14:37:21
- Tags: #read #git #deepdive

## TL;DR
作者在 Tigris 上实现 Git 服务器 objgit，重设面向对象存储的 packfile，用 bin/cue 索引支持精确 Range 读取，性能大增；但项目仍早期，缺认证授权。

## Summary
这篇文章讲的是：作者在 Tigris 对象存储上实现了一个 Git 服务器（开源项目 objgit），把 Git 仓库直接存进对象存储。为了让这件事在真实规模的仓库上跑得动，他不得不重新设计了一种面向对象存储的 packfile 格式。

**Git 的本质：一堆对象**

Git 仓库本质上就是两样东西：一大片对象，以及一些指向这些对象的命名引用（分支、标签）。每次 commit 时，Git 把内容作为对象写进 `.git/objects` 目录。每个对象是内容寻址的压缩文件——文件名就是内容字节的 SHA1，所以同样的内容在任何地方都是同一个对象。

对象分三类：commit、tree、blob。commit 指向 tree，tree 指向文件（blob），层层嵌套就构成了仓库。

小仓库这样存没问题，但 Linux 内核有 1100 万个对象。如果每个对象一个文件，就会撞上 inode 上限——就像当年 `node_modules` 那种无限嵌套文件夹的问题。

**Git 的对策：packfile**

Git 把对象打包进 packfile：一个压缩的包，所有对象存在同一个文件里，配一个 `.idx` 索引。索引记录每个对象的偏移量，Git 用这些偏移去 packfile 里定位。本地文件系统上这套工作得很好，因为 Git 用 mmap 把 packfile 映射成内存页，内核按需加载。

问题在于：这套设计默认你在本地磁盘上。本地文件系统读取顶多 10 纳秒，而任何网络往返至少 10 毫秒——差了至少一百万倍。更麻烦的是，Git 有个 Unix 习惯：写文件后立刻读回来算 hash。在对象存储里，你没法 Get 一个还没完成 Put 的对象。

**那能不能用 HTTP Range 请求从 packfile 里只取一个对象？**

理论上可以：你知道对象在 packfile 里的偏移，就直接 Range GET 那一段。但实际操作不行。索引里告诉你的是对象**解压后**的大小，而不是**压缩后**的大小。你不知道对象在 packfile 里实际占多少字节，就没法构造出精确的 Range 请求。这正是作者要发明新格式的核心原因之一。

**灵感来自 CD 的 .bin/.cue**

CD 是一个大二进制容器，里面分 session 和 track。为了让播放器能跳到任意一首歌，而不是从头读整张盘，就有了 `.cue` 文件——纯文本，记录每个 track 在 `.bin` 里的位置。播放器解析 cue，一个 seek 就能定位。`.cue` 还顺便解决了多 session 的问题（Dreamcast 游戏碟就是靠这个伪装成音频 CD 的）。

**新格式：objects.bin + objects.cue**

作者借鉴了这个思路，做了一个两文件的结构：

- **objects.bin**：对象一个接一个存放，通常最大 128MiB。为什么是 128MiB？“因为看起来比较圆。”
- **objects.cue**：二进制列式索引。开头 16 字节头（magic `OGCU`、版本、记录大小、记录条数），之后是固定 58 字节的记录，每条包含：
  - hash 20 字节
  - type 1 字节
  - comp 1 字节
  - bin_offset 8 字节
  - bin_length 4 字节
  - size 4 字节
  - delta_base 20 字节

关键改动是**同时存了压缩后大小和解压后大小**，还存了偏移量。这样就能精确构造 HTTP Range 请求，只把想要的对象从 Tigris 里捞出来。

其他改动：
- 用 zstd 替代 zlib，更快、压缩率更好。
- delta 对象单独存放，不再贴在基础对象尾部，避免“想读一个对象却要先读它和它的一堆 delta”。

因为记录是固定宽度，第 N 条记录的位置就是 `16 + N*58`，一次 seek 加一次 Range GET 就能定位到任意对象。这让整个结构变成了一个**列式存储**——元数据和数据分离，元数据可以单独高效扫描。

**读取策略：和后台下载赛跑**

Git 库每次请求 packfile 里的对象时，整个 packfile 会在后台下载到临时目录。如果请求的对象在“远端”（下载进度还没到的地方），就直接用 Range 请求从 Tigris 抢过来，和后台下载赛跑——谁先到就用谁。等后台下载追上时，就不需要再发 Range 请求了。这样整体延迟很小。

**性能结果**

作者用三个仓库做了 push 和 clone 测试：objgit 自身、一个十年的实验性 monorepo（Xe/x）、一个含大量图片不易压缩的博客仓库（tigris-blog）。测试环境是 Wi-Fi 笔记本，刻意选了比较差的网络条件。

Push 方面，对象存储请求数大幅下降：
- objgit：231 → 18，墙钟 8.7s → 2.2s（4 倍）
- Xe/x：9,236 → 30，墙钟 3m29s → 14.3s（14.6 倍）
- tigris-blog：3,324 → 136，墙钟 2m13s → 26.5s（5 倍）

Clone 方面同样受益：
- objgit：323 → 17 请求，11.8s → 2.6s（4.5 倍）
- Xe/x：6,428 → 17 请求，3m23s → 54.4s（3.7 倍）
- tigris-blog：3,675 → 158 请求，2m23s → 1m22s（1.8 倍）

**现状与局限**

作者说这还在活跃开发中，自己都还不放心用在自己项目上，也不建议别人现在用。还没做认证、授权、API、限流——如果把它暴露到公网，任何能连上的人都能任意 pull/push。packfile 目前会无限累积，未来需要做压缩合并把小的 packfile 合并成大的。如果仓库里有大二进制文件，暂时别用这个架构，他计划之后实现 Git LFS。

**一句话总结**

Git 的 packfile 格式非常适合本地文件系统的约束，但一旦引入网络往返就全盘崩溃。所以需要一个从零设计的、对 Range 请求原生友好的对象存储版本——而分布式版本控制的特性（每个克隆都包含完整历史）让这种“自己造格式”的风险变得可以接受：真出问题，重新 push 一次就恢复了。
