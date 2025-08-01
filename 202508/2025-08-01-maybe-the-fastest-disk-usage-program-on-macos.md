# Maybe the Fastest Disk Usage Program on macOS
- URL: https://healeycodes.com/maybe-the-fastest-disk-usage-program-on-macos
- Added At: 2025-08-01 12:23:11
- [Link To Text](2025-08-01-maybe-the-fastest-disk-usage-program-on-macos_raw.md)

## TL;DR


作者开发的macOS磁盘分析工具dumac通过结合`getattrlistbulk`系统调用和Rust+Tokio协程，实现性能突破：批量获取文件元数据降低系统调用次数，利用轻量级并发控制减少锁竞争，最终比传统`du -sh`快6.4倍，较Go版方案提升13倍。实验证明macOS原生接口与Rust零开销抽象为性能核心。

## Summary


该文章介绍了作者开发的macOS磁盘使用分析工具dumac，旨在超越传统`du -sh`和现有开源工具的性能。核心内容如下：

### **性能挑战**
- **基准测试场景**：包含12层目录、每层100个小文件、总4095个目录和409500个文件的复杂目录结构。
- **传统`du`的缺陷**：通过`lstat`逐个获取文件大小，需执行400万次系统调用，单线程处理导致效率低下，仅能占用CPU 43%资源。
- **现有工具对比**：
  - GNU/Linux工具如diskus因未使用macOS专用API性能受限
  - 原生`du -sh`耗时2.57秒

### **关键技术优化**
1. **`getattrlistbulk`系统调用**
   - 批量获取目录项及元数据（如文件类型、大小、inode），单次调用可处理百个条目，大幅降低系统调用次数。
   - 结合缓冲区优化（128KB最佳），减少磁盘I/O开销。

2. **多语言实现对比**
   - **Go+CGO**：使用C函数调用`getattrlistbulk`，性能提升近3倍（0.85秒），但受CGO调用开销（约40ns/次）限制。
   - **Rust+Tokio**：直接调用`libc`绕过CGO开销，采用轻量级协程（tokio task）并行处理目录遍历，进一步优化锁竞争和inode去重（分片HashSet）。

### **性能结果**
- **最终测试数据**：
  - dumac比传统`du -sh`快6.4倍（0.52秒 vs 3.33秒）
  - 比diskus快2.58倍，比Go版快13倍
  - 系统调用耗时占91%，其余开销为tokio调度和inode锁（1.5%）

### **实现细节**
- **目录递归策略**：通过`getattrlistbulk`一次性获取完整目录元数据，消除逐个`stat`开销。
- **并发控制**：Rust版本采用信号量限制并行任务（MAX_CONCURRENT=64），平衡资源使用。
- **硬链接去重**：基于 inode 的分片锁机制降低并发冲突。

### **优化总结**
- macOS专用系统调用`getattrlistbulk`是核心提速因素。
- Rust的高性能协程与零成本抽象显著优于Go的CGO方案。
- 性能瓶颈仍主要来自内核级I/O操作，未来可探索更细粒度的并发调度优化。

该工具证明了通过结合macOS原生接口与Rust语言特性，可显著提升磁盘分析类工具的性能。
