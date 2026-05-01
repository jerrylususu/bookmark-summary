# Configure Access Point as Personal Hotspot (OpenWrt) · Nostalgia
- URL: https://www.yichya.dev/configure-access-point-as-personal-hotspot/
- Added At: 2026-05-01 21:34:20
- Tags: #read #tips #hack

## TL;DR
本文介绍在 OpenWrt 路由器上配置 Wi-Fi 信标中的特定信息元素，使 macOS 和 Windows 将其识别为个人热点，从而可能优化流量使用。通过抓包分析并修改 hostapd 配置，成功实现热点识别。

## Summary
本文介绍了如何在 OpenWrt 路由器上配置接入点，使其被 macOS 和 Windows 识别为个人热点，从而可能减少流量消耗。作者通过搜索发现，操作系统通过 Wi-Fi 信标中的供应商特定信息元素（Vendor-specific IEs）来识别热点。具体步骤如下：

1. **问题背景**：使用便携路由器插手机卡作为热点，但设备无法识别为热点，导致流量消耗快。macOS 和 Windows 有机制区分普通 Wi-Fi 和热点。
2. **原理探索**：通过搜索和逆向代码，发现 macOS 使用 `IOS_IE` 识别热点，Windows 则使用 Microsoft 定义的 vendor-specific IE（如 `DD080050F21102000200`）。
3. **抓包分析**：使用 macOS 自带工具 `airport` 抓取 Wi-Fi 信标，解析出 iOS 热点的 IE 数据，发现关键字段 `DD0A0017F206010103010000`。
4. **解决方案**：在 OpenWrt 的 hostapd 配置中添加 vendor_elements，命令为 `uci add_list wireless.radio0.hostapd_options='vendor_elements=DD0A0017F206010103010000'`，重启后生效。测试显示 macOS 和 Windows 均能识别为热点。

结果：配置成功，设备显示为个人热点，可能有助于优化流量使用。
