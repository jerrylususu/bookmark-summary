# Australia/Lord_Howe is the weirdest timezone | SSOReady
- URL: https://ssoready.com/blog/engineering/truths-programmers-timezones/
- Added At: 2024-11-01 12:55:22
- [Link To Text](2024-11-01-australia-lord_howe-is-the-weirdest-timezone-ssoready_raw.md)

## TL;DR
文章探讨了时区的复杂性和一些奇怪的时区规则，如尼泊尔的5小时45分钟偏移、摩洛哥和加沙的伊斯兰历调整、格陵兰的负夏令时等。这些时区在软件中通过IANA数据库管理，使用UTC偏移和设计符来标识。尽管时区规则复杂，但通过阅读标准文件可以理解和处理。

## Summary
1. **时区概述**：
   - 时区是有限度的奇怪，存在一些最奇怪的时区，它们在某些方面达到了时区所能达到的极限。

2. **奇怪的时区示例**：
   - `Asia/Kathmandu`：与UTC有奇怪的偏移。
   - `Africa/Casablanca`：不符合时区模型，因此被硬编码。
   - `America/Nuuk`：在-01:00进行夏令时调整（带有负号）。
     - `Africa/Cairo`和`America/Santiago`在24点进行夏令时调整（不是0点）。
   - `Australia/Lord_Howe`：拥有最奇怪的夏令时规则。

3. **软件表示**：
   - 通过查看原始时区文件，了解这些奇怪时区在软件中的表示方式。
   - 这些文件最终由IANA时区数据库（tzdb或zoneinfo）管理，包含二进制文件，编码为时区信息格式（TZIF）。

4. **日历系统**：
   - 西方的时间系统（格里高利历）是主导系统，即使在非西方国家，使用计算机的用户也熟悉格里高利系统。
   - 计算机将格里高利系统投射到未来和过去，称为“预设格里高利历”，虽然不历史准确，但大多数人并不在意。

5. **协调世界时（UTC）**：
   - UTC是现代化的GMT，几乎全球都同意基于UTC的偏移来设置时钟。
   - UTC仍然是平均太阳时，但与格林威治的联系不再重要。

6. **闰秒**：
   - 地球自转正在减慢，需要通过插入闰秒来调整，以保持现实世界与计算机时间的同步。
   - 闰秒是一个有趣的细节，但编程语言通常不支持表示61秒的分钟，因此可以忽略。

7. **奇怪的时区细节**：
   - `Asia/Kathmandu`：尼泊尔比UTC提前5小时45分钟。
   - `Africa/Casablanca`和`Asia/Gaza`：根据伊斯兰历的斋月调整夏令时，由于伊斯兰历基于月亮，与太阳历不同，因此需要硬编码未来的转换。
   - `America/Nuuk`：在-1点进行夏令时调整，实际发生在周六晚上11点。
   - `America/Santiago`和`Africa/Cairo`：在24点进行夏令时调整，实际上是下一天的开始。
   - `Australia/Lord_Howe`：有30分钟的夏令时调整，导致每小时的cron作业在本地时钟上错位。

8. **总结**：
   - 时区虽然奇怪，但有限度。每个时区由ID、一组硬编码的转换和未来转换规则组成。
   - 任何给定时间在时区中都可以通过UTC偏移和设计符来唯一标识。
   - 不要因为复杂性而认为某事不可能，标准文件可以阅读和理解。

9. **附录**：
   - 一些时区有数百个硬编码的未来转换，原因不明。
   - 例如，`Asia/Jerusalem`、`Africa/Cairo`、`America/Nuuk`、`America/Santiago`、`Pacific/Easter`和`Asia/Gaza`都有大量未来转换。
