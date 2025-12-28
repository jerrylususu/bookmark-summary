# Making PyPI's test suite 81% faster
- URL: https://blog.trailofbits.com/2025/05/01/making-pypis-test-suite-81-faster/
- Added At: 2025-05-11 06:38:21

## TL;DR


Trail of Bits与PyPI通过并行测试（pytest-xdist）、Python3.12的sys.monitoring覆盖率技术、精简测试路径(testpaths)及移除冗余依赖等优化，将测试执行时间缩短81%至30秒，测试用例数反增20%（4700条）。优化平衡了性能与安全（100%覆盖率），并感谢社区对数据库同步和DNS缓存的改进贡献。  

（99字）

## Summary


Trail of Bits与PyPI合作通过多项优化将测试套件执行时间从163秒缩短至30秒（81%提升），同时测试用例数量从3900增至4700。主要优化步骤如下：

### 一、核心优化措施
1. **并行测试执行（`pytest-xdist`）**  
   - 配置`--numprocesses=auto`利用32核CPU并行执行，减少67%时间。  
   - 解决挑战：  
     - 数据库隔离（为每个worker分配独立数据库实例）；  
     - 覆盖率报告整合（通过`sitecustomize.py`统一数据）；  
     - 输出可视化（集成`pytest-sugar`）。

2. **代码覆盖率优化（Python3.12 `sys.monitoring`）**  
   - 使用`COVERAGE_CORE=sysmon`替代传统覆盖率工具，减少53%执行时间。  
   - 依赖Python3.12+及最新版`coverage.py`。

3. **测试发现加速（`testpaths`）**  
   - 指定测试目录路径`tests/`，使发现时间从7.84秒降至2.6秒（66%减少）。  
   - 总时间缩短2秒，节省10%开销。

4. **移除冗余导入**  
   - 卸载生产环境使用的`ddtrace`库，测试启动时间减少3.4%。

### 二、未采纳的优化方案  
- **数据库迁移"合并"实验**：  
  将400+迁移脚本压缩为单次操作，测试时间减少13%。  
  **未采用原因**：可能增加维护复杂度，权衡后保留原始方案。

### 三、安全与开发效率协同  
- 快速测试缩短反馈循环，鼓励高频验证，提升安全防御能力。  
- 优化无损测试覆盖率（保持100%分支覆盖率），体现安全性与效率的结合。

### 四、实践建议  
1. 优先并行化测试（`pytest-xdist`）。  
2. 升级Python3.12+并启用`sys.monitoring`。  
3. 使用`testpaths`精准指定测试路径。  
4. 根据`python -X importtime`排查并移除冗余依赖。

### 五、社区贡献  
- 特别感谢开发人员对PostgreSQL文件同步优化（PR #16295）、DNS缓存改进（PR #16384）等贡献。  
- 依赖`pytest`、`coverage.py`等开源项目的底层支持。
