# The Design & Implementation of Sprites
- URL: https://fly.io/blog/design-and-implementation/
- Added At: 2026-01-17 06:35:34
- Tags: #read #arch #deepdive

## TL;DR
Sprites 是 Fly.io 推出的新型 Linux 虚拟机，设计为一次性计算机，具有秒级创建、持久存储和低成本特性。其实现基于无容器镜像、对象存储和内部编排，适用于原型开发和交互式任务，与 Fly Machines 互补，未来可无缝转换到生产环境。

## Summary
Sprites 是 Fly.io 推出的新型 Linux 虚拟机，设计为“一次性计算机”，强调即时创建、持久存储和低成本。核心特性包括：创建速度快（秒级）、100GB 持久根文件系统、自动休眠机制，以及按实际使用计费。

Sprites 的实现基于三个关键设计决策：
- **无容器镜像**：放弃用户自定义容器，改用标准容器，避免拉取和解压延迟，使创建操作快速如启动已有虚拟机。
- **对象存储磁盘**：根存储采用 S3 兼容对象存储，而非 NVMe 附加存储，确保数据持久性和易迁移性，结合 JuiceFS 模型缓存元数据。
- **内部编排**：编排工作移至虚拟机内部，用户代码运行在容器内，根命名空间处理服务管理、日志和网络，降低全局状态影响。

Sprites 与 Fly Machines（Fly.io 的旗舰产品）形成对比：Fly Machines 适合生产环境，但创建慢、依赖容器；Sprites 更适用于原型开发、交互式任务，并利用现有基础设施如 Corrosion 服务发现。未来可集成到工作流中，实现从 Sprites 原型到 Fly Machines 部署的转换。文章推荐用户亲身体验，以感受其便捷性和低成本优势。
