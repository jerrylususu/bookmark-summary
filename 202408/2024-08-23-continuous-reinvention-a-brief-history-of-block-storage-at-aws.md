# Continuous reinvention: A brief history of block storage at AWS
- URL: https://www.allthingsdistributed.com/2024/08/continuous-reinvention-a-brief-history-of-block-storage-at-aws.html
- Added At: 2024-08-23 14:51:40
- [Link To Text](2024-08-23-continuous-reinvention:-a-brief-history-of-block-storage-at-aws_raw.md)

## TL;DR
本文由AWS的EBS团队成员Marc Olson撰写，回顾了EBS从依赖共享硬盘的简单块存储服务发展为每日处理超过140万亿次操作的庞大网络存储系统的历程。文章强调了排队理论、全面仪器化、增量改进的重要性，以及约束如何激发创新，并分享了从HDD到SSD的技术转变、性能优化、团队重组和领导力发展的经验，展望了未来的持续创新和迭代。

## Summary
1. **引言**：
   - **作者背景**：Marc Olson在AWS的Elastic Block Store (EBS)团队工作超过十年，见证了EBS从依赖共享硬盘的简单块存储服务发展为每日处理超过140万亿次操作的庞大网络存储系统。
   - **文章目的**：分享EBS的发展历程，强调排队理论、全面仪器化、增量改进的重要性，以及约束如何激发创新。

2. **EBS的起源**：
   - **初期挑战**：EBS于2008年8月20日推出，初期仅有少数存储专家和分布式系统专家，面临着巨大的技术挑战。
   - **技术选择**：最初基于共享硬盘驱动器(HDD)，后来转向固态硬盘(SSD)，以提高性能和可靠性。

3. **技术演进**：
   - **排队理论应用**：通过银行排队比喻，解释计算机系统如何与存储设备交互，强调队列在处理高峰负载中的必要性。
   - **存储技术转变**：从HDD到SSD的转变，显著提高了IOPS和平均延迟，减少了尾延迟。

4. **性能优化**：
   - **全面仪器化**：建立方法在多个子系统中仪器化每个IO，以识别和优先修复问题。
   - **系统优化**：通过减少系统中的队列数量、优化网络软件和核心持久性引擎，提高整体性能。

5. **组织与管理**：
   - **团队重组**：将 monolithic 开发团队重组为专注于特定领域的小团队，提高迭代和变更的独立性。
   - **领导力发展**：作者通过个人经验分享，如何从个人贡献者转变为能够扩展自己和团队能力的领导者。

6. **网络与硬件优化**：
   - **网络调优**：通过实验调整网络参数，提高吞吐量和减少延迟。
   - **硬件创新**：利用Nitro卡将处理从Xen hypervisor转移到专用硬件，减少操作系统队列，提高性能和安全性。

7. **持续改进**：
   - **增量改进**：通过一系列增量改进，逐步提高EBS的性能和可靠性，而不是进行大规模的架构变更。
   - **未来展望**：强调持续创新和迭代的重要性，以满足客户不断增长的需求。

8. **结论**：
   - **回顾与展望**：回顾EBS从初始阶段到当前高性能状态的历程，强调通过一系列增量改进实现客户价值的持续交付，并展望未来的创新挑战。