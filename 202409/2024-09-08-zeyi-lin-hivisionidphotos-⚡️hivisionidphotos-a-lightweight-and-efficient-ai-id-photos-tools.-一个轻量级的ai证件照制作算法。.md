# Zeyi-Lin/HivisionIDPhotos: ⚡️HivisionIDPhotos: a lightweight and efficient AI ID photos tools. 一个轻量级的AI证件照制作算法。
- URL: https://github.com/Zeyi-Lin/HivisionIDPhotos
- Added At: 2024-09-08 11:22:48
- [Link To Text](2024-09-08-zeyi-lin-hivisionidphotos-⚡️hivisionidphotos-a-lightweight-and-efficient-ai-id-photos-tools.-一个轻量级的ai证件照制作算法。_raw.md)

## TL;DR
HivisionIDPhotos项目旨在开发智能证件照制作算法，支持轻量级抠图、多种尺寸生成及美颜等功能。近期更新包括新增抠图模型和人脸检测API，提供在线体验和API服务部署。项目依赖Python 3.7+，支持多平台，可通过Gradio Demo进行本地操作。

## Summary
1. **最近更新**：
   - **在线体验**：
     - [SwanHub Demo](https://swanhub.co/ZeYiLin/HivisionIDPhotos/demo)
     - [Spaces](https://huggingface.co/spaces/TheEeeeLin/HivisionIDPhotos)
   - **新增功能**：
     - 2024.09.08: 增加新的**抠图模型** [RMBG-1.4](https://huggingface.co/briaai/RMBG-1.4) 和 **ComfyUI工作流** [HivisionIDPhotos-ComfyUI](https://github.com/AIFSH/HivisionIDPhotos-ComfyUI)
     - 2024.09.07: 增加**人脸检测API选项** [Face++](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/face++_CN.md)
     - 2024.09.06: 增加新的抠图模型 [modnet\_photographic\_portrait\_matting.onnx](https://github.com/ZHKKKe/MODNet)
     - 2024.09.05: 更新 [Restful API 文档](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/api_CN.md)
     - 2024.09.02: 更新**调整照片 KB 大小**，[DockerHub](https://hub.docker.com/r/linzeyi/hivision_idphotos/tags)
     - 2023.12.01: 更新**API 部署（基于 fastapi）**
     - 2023.06.20: 更新**预设尺寸菜单**

2. **项目简介**：
   - **目标**：开发一种实用、系统性的证件照智能制作算法。
   - **功能**：
     - 轻量级抠图（纯离线，仅需 **CPU** 即可快速推理）
     - 根据不同尺寸规格生成不同的标准证件照、六寸排版照
     - 支持 纯离线 或 端云 推理
     - 美颜（waiting）
     - 智能换正装（waiting）

3. **社区**：
   - **社区构建的应用和扩展**：
     - [HivisionIDPhotos-windows-GUI](https://github.com/zhaoyun0071/HivisionIDPhotos-windows-GUI)：Windows客户端应用
     - [HivisionIDPhotos-ComfyUI](https://github.com/AIFSH/HivisionIDPhotos-ComfyUI)：ComfyUI证件照处理工作流

4. **准备工作**：
   - **环境安装与依赖**：
     - Python >= 3.7（主要测试在 python 3.10）
     - OS: Linux, Windows, MacOS
   - **步骤**：
     - 克隆项目
     - 安装依赖环境
     - 下载权重文件
     - 人脸检测模型配置（可选）

5. **Demo启动**：
   - **运行 Gradio Demo**：生成一个本地 Web 页面，完成证件照的操作与交互。

6. **Python推理**：
   - **核心参数**：
     - `-i`: 输入图像路径
     - `-o`: 保存图像路径
     - `-t`: 推理类型（idphoto、human_matting、add_background、generate_layout_photos）
     - `--matting_model`: 人像抠图模型权重选择
     - `--face_detect_model`: 人脸检测模型选择
   - **具体操作**：
     - 证件照制作
     - 人像抠图
     - 透明图增加底色
     - 得到六寸排版照

7. **API服务部署**：
   - **启动后端**
   - **请求 API 服务**：详细请求方式请参考 [API 文档](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/api_CN.md)

8. **Docker部署**：
   - **拉取或构建镜像**：
     - 拉取最新镜像
     - Dockerfile 直接构建镜像
     - Docker compose 构建
   - **运行服务**：
     - 启动 Gradio Demo 服务
     - 启动 API 后端服务
     - 两个服务同时启动

9. **环境变量**：
   - **配置项**：
     - FACE_PLUS_API_KEY
     - FACE_PLUS_API_SECRET

10. **引用项目**：
    - **MTCNN**
    - **ModNet**

11. **开发小贴士**：
    - **修改预设尺寸**：修改 `size_list_CN.csv` 后再次运行 `app.py`

12. **联系我们**：
    - 邮件联系：[zeyi.lin@swanhub.co](mailto:zeyi.lin@swanhub.co)

13. **贡献者**：
    - [Zeyi-Lin](https://github.com/Zeyi-Lin)、[SAKURA-CAT](https://github.com/SAKURA-CAT)、[Feudalman](https://github.com/Feudalman)、[swpfY](https://github.com/swpfY)、[Kaikaikaifang](https://github.com/Kaikaikaifang)、[ShaohonChen](https://github.com/ShaohonChen)、[KashiwaByte](https://github.com/KashiwaByte)

14. **StarHistory**：
    - [Star History Chart](https://star-history.com/#Zeyi-Lin/HivisionIDPhotos&Date)
