# Reading NFC Passport Chips in Linux
- URL: https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/
- Added At: 2025-06-24 15:11:36

## TL;DR


本文介绍如何使用Linux下pypassport工具读取护照NFC芯片。需通过MRZ密码验证，作者通过计算校验码重建被裁剪的MRZ（含出生日期、有效期等字段）。工具依赖Python安装，可解析芯片数据组。其他工具如mrtdreader等无效。成功可读取明文信息如照片，但无法检测护照是否吊销，且存在数米内通信窃听风险，建议仅作合法用途使用。

## Summary


该文章介绍了在Linux系统下使用 Roeften 开发的 pypassport 工具读取护照NFC芯片数据的实践经验。主要内容包括：

1. **背景与挑战**  
   - 护照NFC芯片需MRZ（机读区）密码验证，密码包含护照号、出生日期、有效期及校验码  
   - 已注销护照的MRZ被裁剪，但芯片仍可工作（因英国规定注销时仅裁剪特定区域保留芯片）  

2. **MRZ重建方法**  
   - 通过已知信息（护照号、出生日期、有效期）计算校验码生成完整MRZ，Python代码示例：  
     ```python
     def calculateMRZ(passportNumber, DOB, expiry):
         ...  # 含校验码计算函数及组合逻辑  
     ```

3. **密码学与安全机制**  
   - 采用标准公钥加密，芯片无访问次数限制但支持防暴力破解设计  
   - 暴力破解分析：若已知护照号和出生日期，需尝试最多36525种有效期组合，耗时约2天  

4. **工具安装与使用**  
   - 安装步骤：pip安装pyasn1后通过pypassport示例代码读取数据  
     ```python
     from pypassport import epassport, reader
     ep.readPassport()  
     ```
   - 数据分组解析：数据存储于60（元数据）、61（基础信息）、75（生物特征图像）等数据组  

5. **失败尝试的工具**  
   - mrtdreader（NFC库过时）、Python 2版pyPassport、beaujean's pyPassport（仅漏洞检测）、d-Logic商业软件、Android应用（无法Linux移植）  

6. **结论与风险**  
   - 修复后的MRZ可有效读取芯片，但仅获取明文可见信息（姓名、照片等）  
   - 现有方法无法检测护照是否被吊销或存在加密异常，仅适合合法用途  

附注：文章提及商业级NFC读取器可实现15cm远距离读取，ICAO警告未加密通信可能在数米内被窃听。
