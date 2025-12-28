# Rainbow Deploys with Kubernetes | Brandon Dimcheff
- URL: https://brandon.dimcheff.com/2018/02/rainbow-deploys-with-kubernetes/
- Added At: 2025-06-15 10:51:04

## TL;DR


Olark团队提出Rainbow Deploy策略解决Kubernetes中文本服务无中断部署问题。通过基于Git Commit前6位的动态版本命名，实现新版本零停机流量切换，回滚简单且兼容原生资源；但需人工清理旧版本，资源消耗较高。该方案自2017年部署显著提升稳定性，但仍需自动化清理机制及资源优化。

## Summary


Olark团队为解决状态化服务在Kubernetes中的无中断部署问题，提出了Rainbow Deploy策略。其核心场景是聊天服务需保持用户持久连接，传统滚动部署会导致大规模强制断线和负载激增。早期尝试包括：

1. **初始方案失败**  
   - 使用`service-loadbalancer`与长时间`terminationGracePeriodSeconds`，但因连接提前中断失败。

2. **蓝绿部署局限**  
   - 双版本切换可避免中断，但每日仅能部署一次且资源占用较高（需持续运行多副本）。

3. **Rainbow Deploy实现**  
   - **动态版本命名**：以Git Commit SHA前6位（符合十六进制颜色码）为Deployment名称（如`chat-olark-com-$SHA`）。  
   - **零停机切换**：新部署就绪后，通过Service直接切换流量至新Deployment，回滚只需改回旧版本。  
   - **手动清理旧版本**：依赖用户连接自然衰减，由人工判断清理旧 Deployment，避免强制终止引发的中断。

**优点**  
- 支持高频部署，版本隔离彻底，降低回滚风险。  
- 兼容Kubernetes原生资源对象，无需复杂改造。

**现存问题与展望**  
- 缺乏自动化清理旧版本的机制，需人工监控连接状态。  
- 希望Kubernetes原生支持类似"Immutable"策略，允许Pod按需优雅退出，并通过生命周期钩子触发清理。

该方案自2017年6月部署，显著提升了Olark服务的可靠性，但仍需解决自动清理和资源优化问题。
