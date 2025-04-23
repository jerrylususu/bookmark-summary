# Abusing DuckDB-WASM by making SQL draw 3D graphics (Sort Of)
- URL: https://www.hey.earth/posts/duckdb-doom
- Added At: 2025-04-23 14:53:01
- [Link To Text](2025-04-23-abusing-duckdb-wasm-by-making-sql-draw-3d-graphics-(sort-of)_raw.md)

## TL;DR


开发者基于DuckDB-WASM创建了SQL驱动的3D文字版Doom游戏，利用SQL表管理游戏元素，通过递归CTE模拟三维raycasting渲染，并完成碰撞检测等核心逻辑。尽管性能受限（6-7 FPS），但证明了SQL在复杂算法中的潜力，适合用于学习优化与跨语言协作，非游戏开发用途。

## Summary


- **项目概述：**  
  通过滥用DuckDB-WASM（浏览器端分析型数据库）构建了一个SQL驱动的3D文字版Doom克隆游戏。游戏数据、状态更新及渲染均通过SQL操作实现，JavaScript仅用于事件协调和 sprites 绘制。

- **核心技术方案：**  
  1. **数据库作为游戏世界**：所有游戏元素（地图、玩家、敌人、子弹等）存储为DuckDB表，包括16x16地图、玩家坐标、移动方向及游戏设置。  
  2. **SQL驱动游戏逻辑**：  
     - 玩家移动：通过`COS()`和`SIN()`函数更新坐标。  
     - 子弹与敌人交互：使用`JOIN`检测碰撞，通过`DELETE`移除物体。  
  3. **SQL视图实现三维渲染**：通过递归公用表表达式（CTE）模拟raycasting算法，计算每列屏幕的墙面距离并修正鱼眼效果； 使用`string_agg`函数将字符（如空格、色块）拼接为最终的3D文本帧。  
  4. **JavaScript辅助层**：处理键盘输入、游戏循环调度，并通过Z缓冲检测判断 sprites 是否应覆盖墙面，最终将渲染结果输出到`<pre>`标签。

- **主要挑战与解决方案：**  
  1. **库加载失败**：问题源于CDN链接配置错误，通过使用DuckDB-WASM提供的`getJsDelivrBundles`和`+esm`端点修复。  
  2. **SQL方言差异**：DuckDB不支持`AUTOINCREMENT`，改用`SEQUENCE`生成ID。  
  3. **查询规划冲突**：因表函数无法动态引用设置表字段，将生成范围预设为固定值再通过过滤调整，解决引用未解析错误。  
  4. **异步竞态条件**：通过`isProcessingTick`布尔锁和`try...finally`块确保数据库操作顺序执行。  
  5. **Sprites渲染问题**：额外创建`column_distances`视图存储墙面距离，结合JavaScript在渲染时检查Z缓冲。

- **性能表现：**  
  - 6-7 FPS（每秒帧数），主要开销来自SQL raycasting查询（80-100ms/次）。  
  - JavaScript负责的 sprites 绘制耗时较短，游戏移动和碰撞检测响应尚可。

- **项目启示：**  
  1. SQL的扩展能力远超预期，甚至能处理复杂算法（如递归CTE、窗口函数）。  
  2. DuckDB-WASM性能强大，浏览器端可执行每秒6-7次复杂递归查询。  
  3. 跨语言协作必要性：SQL处理核心逻辑，JavaScript负责协调和性能敏感任务。  
  4. 跨语言调试难度大，需依赖日志追踪问题根源。  
  5. 查询规划逻辑的关键性：需针对SQL引擎的规则调整逻辑以避免错误。

- **项目推荐与展望：**  
  - **生产游戏开发**：不建议，因性能和适用性限制。  
  - **学习实验**：推荐，深度学习SQL优化、3D投影算法、异步模式及WASM浏览器特性。  
  - 未来可能方向：尝试将DuckDB用于浏览器端的物理模拟、路径寻找或全文搜索等非典型场景。

- **扩展资料：**  
  代码开源（GitHub链接），总代码约500行，SQL和JavaScript各占一半。作者鼓励尝试添加纹理、复杂场景或移动敌人等更高级功能。
