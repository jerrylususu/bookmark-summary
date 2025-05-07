# An year of the Linux Desktop
- URL: https://xeiaso.net/blog/2025/yotld/
- Added At: 2025-05-07 13:47:09
- [Link To Text](2025-05-07-an-year-of-the-linux-desktop_raw.md)

## TL;DR


2025年作者尝试以Fedora替代Windows，因Copilot干扰和隐私问题推动。选用AMD Ryzen 9与RX 9070 XT硬件，初期遭遇驱动兼容故障，后升级Fedora 42 Beta并手动修复XWayland权限问题，解决图形应用崩溃。Steam需禁用iGPU，但FF14仍存休眠崩溃隐患。NAS挂载配置失误间接导致系统不稳定，修正后环境趋于稳定。文章指出Linux办公游戏可行性提升，但硬件更新延迟、配置细节易引发问题，适合愿自主调试的技术爱好者。

## Summary


本文总结作者2025年尝试以Linux（主要使用Fedora）作为桌面系统的经历，涵盖硬件选择、系统安装调试及遇到的技术挑战。主要内容如下：

### **技术挑战与解决方案**
1. **Windows的困境**  
   - 强制推送Copilot、AI功能干扰用户体验，隐私安全风险促使转向Linux。  
   - 游戏依赖（如iRacing、FF14）因性能或兼容性问题仍需Windows，但寻求减少依赖。

2. **硬件配置与选择**  
   - 采用AMD Ryzen 9 9800X3D + RX 9070 XT组合，解决NVIDIA显存不足问题（游戏占用超16GB VRAM）。  
   - B850M主板及全白主题组装，但硬件兼容性初期在Fedora 41中引发驱动问题（如网络设备未识别、分辨率限制）。

3. **Fedora系统的安装调试**  
   - **Fedora 41**：首次安装遭遇显卡驱动异常，导致启动卡在splash界面，需重装。  
   - **升级至Fedora 42 Beta**：硬件兼容性显著改善，但后续更新导致XWayland服务崩溃（无法启动Steam、Xeyes等X11应用）。  
   - 通过自定义服务脚本修复`/tmp/.X11-unix`目录权限问题（手动创建并设置粘滞位），恢复图形界面功能。

4. **Steam与AMD GPU配置**  
   - Steam默认启用iGPU导致渲染问题（如"llvmpipe"软件渲染），需禁用BIOS中iGPU。  
   - 休眠/唤醒后FF14出现显卡崩溃（"shader pipeline爆炸"），推测与Proton、Mesa驱动或AMDGPU内核模块相关，尚无明确解决方案。

### **配置错误与调试发现**
- **NAS自动挂载配置失误**：  
  原`mnt-itsuki.automount`单元定义错误（依赖`remote-fs-pre.target`而非`multi-user.target`），导致系统服务依赖循环，间接引发XWayland不稳定。修正配置后问题消失。

### **软件生态问题**
- **RPM Fusion仓库限制**：  
  非自由软件仓库（如包含H.264编解码器的完整版FFmpeg）因旧版本下架，导致降级调试受阻，作者呼吁仓库维护者保留历史版本。

### **结论与反思**
- **可行性验证**：经过排查与调试，Linux（Fedora）最终能满足游戏（FF14）与办公需求，但需较强系统维护能力。  
- **经验教训**：硬件新品兼容性延迟（需新内核支持）、配置细节错误易引发级联问题，系统管理需谨慎处理依赖关系。  
- **未来展望**：尽管存在学习成本与坑点，但开源生态的进步使Linux桌面环境逐渐成熟，尤其适合技术爱好者自主掌控硬件与软件环境的需求。

文章以幽默口吻记录技术细节，强调"调试既是杀手也是侦探"的自嘲，最终认可了Linux在特定场景下的实用性。
