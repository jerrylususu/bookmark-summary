# Some esoteric versioning schemes (monotonic moronity)
- URL: https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/
- Added At: 2025-02-12 13:25:14
- [Link To Text](2025-02-12-some-esoteric-versioning-schemes-(monotonic-moronity)_raw.md)

## TL;DR
文章探讨了多种软件版本控制方案，包括SemVer、CalVer等主要方案，以及EffVer、0Ver等替代方案，分析了各自的优缺点，提出了选择版本控制方案应根据开发者的具体需求。

## Summary
1. **软件版本历史**：软件自始以来就有版本号，开发者通过添加新功能或修复Bug来发布新版本。

2. **主要版本控制方案**：
   - **SemVer**：
     - 格式通常为`1.2.3`，表示主要版本、次要版本和补丁版本。
     - 主要问题：
       1. 数字可能不是十进制，难以判断版本新旧。
       2. 缺乏发布时间的语义信息。
   - **CalVer**：
     - 版本号基于发布日期，如Ubuntu的`YY.MM`格式。
     - 主要问题：
       1. 使用`YYYY-MM`格式更清晰。
       2. 小版本号如`24.04.1`可能让人误解为日期。
       3. 无法反映重大或破坏性变化。

3. **替代版本控制方案**：
   - **EffVer**：基于开发工作量的版本控制，尝试标准化SemVer。
   - **PrideVer**：基于开发者对自己代码的自豪感，适用于有自信的开发者。
   - **RuffVer**：结合SemVer和CalVer，稳定版使用偶数，预览版使用奇数。
   - **0Ver**：零基础版本控制，适用于不敢承诺完成时间的开发者。
   - **PiVer**：使用π的数字作为版本号，适合追求完美的开发者。
   - **NameVer**：使用命名版本，如Ubuntu的`Bionic Beaver`，按字母顺序排列。
   - **WinVer**：微软Windows的版本号，逻辑复杂，跳过9的原因据称是技术原因。
   - **KelVer**：基于开尔文温标的版本控制，版本号从高到低表示稳定性。

4. **非单调版本控制**：
   - **HashVer**：使用代码的加密哈希值作为版本号。
   - **RandVer**：随机选择未使用过的版本号，完全无语义信息。

5. **总结**：各种版本控制方案都有其优缺点，选择合适的方案取决于开发者的需求和偏好。
