# Gist of Go: Pipelines
- URL: https://antonz.org/go-concurrency/pipelines/
- Added At: 2024-12-12 15:55:59

## TL;DR
本文是《Go并发编程》书籍的一部分，重点介绍了如何使用goroutine和channel构建并发管道，涵盖了goroutine泄露、取消通道、合并通道、管道构建及防止goroutine泄露等内容，强调了并发编程中的常见问题和解决方法。

## Summary
1. **引言**：
   - 本章节是《Go并发编程》书籍的一部分，通过交互式示例从基础开始讲解Go并发编程。
   - 本章重点介绍如何将goroutine和channel组合成并发管道。

2. **内容概述**：
   - 本章涵盖了以下主题：
     - [泄露的goroutine](#leaked-goroutine)
     - [取消通道](#cancel-channel)
     - [取消与完成](#cancel-vs-done)
     - [合并通道：顺序](#merging-channels-sequentially)
     - [合并通道：并发](#merging-channels-concurrently)
     - [合并通道：选择](#merging-channels-select)
     - [管道](#pipeline)
     - [防止goroutine泄露](#preventing-goroutine-leaks)
     - [继续前进](#keep-it-up)

3. **泄露的goroutine**：
   - 示例展示了一个将指定范围内的数字发送到通道的函数。
   - 如果在循环中提前退出，`rangeGen()`中的goroutine会被阻塞，导致goroutine泄露。
   - 泄露的goroutine会占用内存，最终可能导致内存耗尽。

4. **取消通道**：
   - 通过创建一个单独的`cancel`通道，`main()`可以通知`rangeGen()`提前退出。
   - 使用`select`语句，goroutine可以在接收到取消信号时退出，避免泄露。

5. **取消与完成**：
   - 取消通道与完成通道类似，但用途不同：
     - 取消通道用于通知goroutine停止工作。
     - 完成通道用于通知goroutine已完成工作。

6. **合并通道（顺序）**：
   - 有时需要将多个独立函数的输出通道合并为一个通道。
   - 顺序合并通道的方法会导致并发性不足，效率低下。

7. **合并通道（并发）**：
   - 通过启动多个goroutine并发读取输入通道，可以提高合并效率。
   - 使用`sync.WaitGroup`确保所有输入通道读取完成后关闭输出通道。

8. **合并通道（选择）**：
   - 使用`select`语句可以在单个goroutine中实现并发合并。
   - 通过将已关闭的通道设置为`nil`，可以避免从已关闭的通道中读取数据。

9. **管道**：
   - 管道是由一系列操作组成的序列，每个操作处理输入数据并输出结果。
   - 管道通常包括读取器、处理器和写入器，每个阶段都可以有多个并发处理器。

10. **防止goroutine泄露**：
    - goroutine泄露是并发程序中的常见问题，通常由于忘记创建取消通道或goroutine在`select`中阻塞。
    - 通过在`select`中嵌套`select`或在通道操作前检查取消信号，可以防止goroutine泄露。

11. **总结**：
    - 管道是并发编程中的常见模式，本章介绍了如何组合、拆分和合并数据流，以及如何取消管道阶段和防止goroutine泄露。
    - 并发编程复杂，需要仔细测试代码，确保没有goroutine泄露。
