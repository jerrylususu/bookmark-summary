# How iOS Restricts Features by Region: A Look at MobileGestalt and Eligibility
- URL: https://type.cyhsu.xyz/2024/09/ios-feature-regional-lockout/
- Added At: 2024-09-27 14:46:36

## TL;DR
iPhone 16系列因区域差异导致功能受限，主要通过MobileGestalt和Eligibility系统组件实现。iOS 18.1前Apple Intelligence等功能在中国大陆和欧盟不可用。非越狱设备曾利用sparserestore漏洞解锁，但iOS 18.1已修复此漏洞。

## Summary
1. **iPhone 16系列发布**：
   - **功能限制**：iPhone 16系列发布时，某些功能（如Apple Intelligence）在iOS 18.1之前不可用，且在中国大陆和欧盟地区无法使用。
   - **区域差异**：不同地区的iPhone功能差异显著，几乎像是不同型号的手机。

2. **苹果的决策**：
   - **商业决策**：苹果作为盈利公司，有权决定是否及如何遵守全球复杂的监管环境。
   - **用户选择**：用户可以通过购买行为表达对苹果决策的看法。

3. **iOS区域功能限制的管理**：
   - **主要组件**：
     - **MobileGestalt**：位于`/usr/lib/libMobileGestalt.dylib`的系统库，存储设备模型、硬件能力和某些功能的可用性。
     - **Eligibility**：包含`/usr/libexec/eligibilityd`守护进程和`/usr/lib/system/libsystem_eligibility.dylib`系统库，根据模型、位置、区域和账户地区等因素决定设备是否“合格”使用某些功能。

4. **MobileGestalt详解**：
   - **功能**：作为数据库，其他系统组件可以通过API查询设备信息。
   - **信息存储**：部分信息动态获取，部分静态存储在`/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist`。
   - **属性示例**：
     - **ArtworkTraits**：显示规格（如Dynamic Island、广色域等）。
     - **device-name**：设备类别（如iPhone）。
     - **RegionCode**：区域代码（如US、CH）。
     - **RegionInfo**：模型后缀以识别区域（如LL/A、CH/A）。

5. **Eligibility详解**：
   - **输入因素**：考虑模型、位置、区域、账户地区等因素。
   - **管理功能**：使用元素名称（如Hydrogen、Carbon）作为功能代号。
   - **配置文件**：位于`/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_OSEligibility/purpose_auto/$HASH.asset/AssetData/Config.plist`，包含功能可用性的配置。
   - **缓存机制**：`eligibilityd`缓存检查结果，缓存文件位于`/private/var/db/os_eligibility/eligibility.plist`。

6. **非越狱解锁工具的利用**：
   - **漏洞利用**：利用iOS 15.2以来的sparserestore漏洞，通过修改系统文件实现功能解锁。
   - **具体方法**：通过目录遍历和硬链接机制，绕过iOS的系统文件保护，修改`RegionCode`和`RegionInfo`以绕过区域限制。

7. **总结**：
   - **技术细节**：MobileGestalt和Eligibility是iOS实现区域功能限制的核心组件。
   - **漏洞与修复**：iOS 18.1 beta 5已修复sparserestore漏洞，限制了非越狱设备的解锁能力。
