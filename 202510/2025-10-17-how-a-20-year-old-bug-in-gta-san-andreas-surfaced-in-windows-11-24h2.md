# How a 20 year old bug in GTA San Andreas surfaced in Windows 11 24H2
- URL: https://cookieplmonster.github.io/2025/04/23/gta-san-andreas-win11-24h2-bug/
- Added At: 2025-10-17 14:41:14
- [Link To Text](2025-10-17-how-a-20-year-old-bug-in-gta-san-andreas-surfaced-in-windows-11-24h2_raw.md)

## TL;DR
Windows 11 24H2更新暴露了《GTA圣安地列斯》中长达20年的隐藏bug，导致Skimmer水上飞机无法生成。原因是游戏配置文件缺失参数，加上Windows系统更新改变了栈空间使用方式，使未初始化变量异常扩大。修复方法可通过社区补丁或手动修改配置文件解决，突显代码健壮性和社区维护的重要性。

## Summary
本文深入分析了《GTA圣安地列斯》中一个因Windows 11 24H2更新而暴露的20年隐藏bug，该bug导致游戏中的Skimmer水上飞机无法正常生成。

### 问题现象
- **触发条件**：玩家升级到Windows 11 24H2后，Skimmer飞机会完全消失，无法通过修改器生成或在地图固定位置找到。
- **影响范围**：无论游戏是否安装模组（如SilentPatch），该问题均会复现，表明是系统更新导致的兼容性问题。

### 根本原因分析
1. **数据文件缺陷**：
   - Skimmer在`vehicles.ide`配置文件中被定义为飞机类型，但其数据行缺少后四个参数（包括前后轮尺寸参数），而其他飞机均完整定义。这是因为Skimmer在《GTA罪恶都市》中原本是船只类型，移植到《圣安地列斯》时遗漏了调整。
   - 游戏代码`CFileLoader::LoadVehicleObject`使用`sscanf`解析配置文件时，未对缺失参数进行默认值初始化，导致局部变量`frontWheelScale`和`rearWheelScale`保持未初始化状态。

2. **系统更新暴露bug**：
   - 在Windows 11 24H2之前，未初始化的轮子尺寸变量偶然保留了前一个车辆（Topfun）的值（0.7），使Skimmer能正常运作。
   - Windows 11 24H2改进了临界区（Critical Section）实现，导致`LeaveCriticalSection`函数占用更多栈空间，覆盖了之前保留的轮子尺寸值，使未初始化变量变为极大随机数。
   - 错误的轮子尺寸传递到碰撞模型计算中，造成飞机生成时Z坐标异常，最终使Skimmer被弹到极远距离（如10^31米高空）。

### 修复方案
- **代码层面**：SilentPatch模组通过钩子函数拦截`sscanf`调用，为缺失参数提供默认值（前后轮尺寸均设为0.7），已提交修复补丁。
- **手动修复**：用户可直接编辑`data\vehicles.ide`，在Skimmer行末尾添加缺失参数（`-1, 0.7, 0.7, -1`）。

### 深层启示
- **兼容性教训**：该bug依赖未定义行为（未初始化变量），本应在早期系统版本中暴露，但因栈布局巧合隐藏了20年。系统内部实现的微小变化（如栈使用方式）可能意外触发此类问题。
- **代码质量**：游戏应验证输入数据完整性并处理编译器警告，避免依赖未定义行为。
- **历史对比**：该bug在Xbox版及后续平台（如Steam、移动端）中已被Rockstar修复（默认值设为1.0），但PC原版长期未更新。

最终，文章强调社区模组在维护老游戏兼容性中的关键作用，并提醒开发者重视代码健壮性以防止类似问题。
