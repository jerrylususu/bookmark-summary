Title: GitHub - Zeyi-Lin/HivisionIDPhotos: ⚡️HivisionIDPhotos: a lightweight and efficient AI ID photos tools. 一个轻量级的AI证件照制作算法。

URL Source: https://github.com/Zeyi-Lin/HivisionIDPhotos

Markdown Content:
> **相关项目**：
> 
> *   [SwanLab](https://github.com/SwanHubX/SwanLab)：训练人像抠图模型全程用它来分析和监控，以及和实验室同学协作交流，大幅提升了训练效率。

目录
--

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#%E7%9B%AE%E5%BD%95)

*   [最近更新](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E6%9C%80%E8%BF%91%E6%9B%B4%E6%96%B0)
*   [项目简介](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E9%A1%B9%E7%9B%AE%E7%AE%80%E4%BB%8B)
*   [社区](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E7%A4%BE%E5%8C%BA)
*   [准备工作](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)
*   [Demo启动](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E8%BF%90%E8%A1%8C-gradio-demo)
*   [Python推理](https://github.com/Zeyi-Lin/HivisionIDPhotos#-python-%E6%8E%A8%E7%90%86)
*   [API服务部署](https://github.com/Zeyi-Lin/HivisionIDPhotos#%EF%B8%8F-%E9%83%A8%E7%BD%B2-api-%E6%9C%8D%E5%8A%A1)
*   [Docker部署](https://github.com/Zeyi-Lin/HivisionIDPhotos#-docker-%E9%83%A8%E7%BD%B2)
*   [联系我们](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC)
*   [贡献者](https://github.com/Zeyi-Lin/HivisionIDPhotos#%E8%B4%A1%E7%8C%AE%E8%80%85)

🤩 最近更新
-------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E6%9C%80%E8%BF%91%E6%9B%B4%E6%96%B0)

*   在线体验： [![SwanHub Demo](https://camo.githubusercontent.com/8fb49df59a8a73a5b9e615ae8a1fa6bd17449836e3685be9124d779855ee4913/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d44656d6f266d6573736167653d5377616e48756225323044656d6f26636f6c6f723d626c7565)](https://swanhub.co/ZeYiLin/HivisionIDPhotos/demo)、[![Spaces](https://camo.githubusercontent.com/f302d00c36a87c4bac8741c397b6a55f1017c961cec10b0990879eda5e15a3f4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462541342539372d4f70656e253230696e2532305370616365732d626c7565)](https://huggingface.co/spaces/TheEeeeLin/HivisionIDPhotos)
    
*   2024.09.08: 增加新的**抠图模型** [RMBG-1.4](https://huggingface.co/briaai/RMBG-1.4) | **ComfyUI工作流** - [HivisionIDPhotos-ComfyUI](https://github.com/AIFSH/HivisionIDPhotos-ComfyUI) 贡献 by [AIFSH](https://github.com/AIFSH/HivisionIDPhotos-ComfyUI)
    
*   2024.09.07: 增加**人脸检测API选项** [Face++](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/face++_CN.md)，实现更高精度的人脸检测
    
*   2024.09.06: 增加新的抠图模型 [modnet\_photographic\_portrait\_matting.onnx](https://github.com/ZHKKKe/MODNet)
    
*   2024.09.05: 更新 [Restful API 文档](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/api_CN.md)
    
*   2024.09.02: 更新**调整照片 KB 大小**，[DockerHub](https://hub.docker.com/r/linzeyi/hivision_idphotos/tags)
    
*   2023.12.01: 更新**API 部署（基于 fastapi）**
    
*   2023.06.20: 更新**预设尺寸菜单**
    

项目简介
----

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#%E9%A1%B9%E7%9B%AE%E7%AE%80%E4%BB%8B)

> 🚀 谢谢你对我们的工作感兴趣。您可能还想查看我们在图像领域的其他成果，欢迎来信:[zeyi.lin@swanhub.co](mailto:zeyi.lin@swanhub.co).

HivisionIDPhoto 旨在开发一种实用、系统性的证件照智能制作算法。

它利用一套完善的AI模型工作流程，实现对多种用户拍照场景的识别、抠图与证件照生成。

**HivisionIDPhoto 可以做到：**

1.  轻量级抠图（纯离线，仅需 **CPU** 即可快速推理）
2.  根据不同尺寸规格生成不同的标准证件照、六寸排版照
3.  支持 纯离线 或 端云 推理
4.  美颜（waiting）
5.  智能换正装（waiting）

[![](https://github.com/Zeyi-Lin/HivisionIDPhotos/raw/master/assets/demo.png)](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/assets/demo.png)

* * *

如果 HivisionIDPhoto 对你有帮助，请 star 这个 repo 或推荐给你的朋友，解决证件照应急制作问题！

🏠 社区
-----

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E7%A4%BE%E5%8C%BA)

我们分享了一些由社区构建的HivisionIDPhotos的有趣应用和扩展：

*   [HivisionIDPhotos-windows-GUI](https://github.com/zhaoyun0071/HivisionIDPhotos-windows-GUI)：Windows客户端应用，由 [zhaoyun0071](https://github.com/zhaoyun0071) 构建
*   [HivisionIDPhotos-ComfyUI](https://github.com/AIFSH/HivisionIDPhotos-ComfyUI)：ComfyUI证件照处理工作流，由 [AIFSH](https://github.com/AIFSH/HivisionIDPhotos-ComfyUI) 构建

[![](https://github.com/Zeyi-Lin/HivisionIDPhotos/raw/master/assets/comfyui.png)](https://github.com/AIFSH/HivisionIDPhotos-ComfyUI)

🔧 准备工作
-------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)

环境安装与依赖：

*   Python \>\= 3.7（项目主要测试在 python 3.10）
*   OS: Linux, Windows, MacOS

1\. 克隆项目
--------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#1-%E5%85%8B%E9%9A%86%E9%A1%B9%E7%9B%AE)

git clone https://github.com/Zeyi-Lin/HivisionIDPhotos.git
cd  HivisionIDPhotos

2\. 安装依赖环境
----------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#2-%E5%AE%89%E8%A3%85%E4%BE%9D%E8%B5%96%E7%8E%AF%E5%A2%83)

> 建议 conda 创建一个 python3.10 虚拟环境后，执行以下命令

pip install -r requirements.txt
pip install -r requirements-app.txt

3\. 下载权重文件
----------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#3-%E4%B8%8B%E8%BD%BD%E6%9D%83%E9%87%8D%E6%96%87%E4%BB%B6)

**方式一：脚本下载**

python scripts/download\_model.py --models all

**方式二：直接下载**

存到项目的`hivision/creator/weights`目录下：

*   `modnet_photographic_portrait_matting.onnx` (24.7MB): [MODNet](https://github.com/ZHKKKe/MODNet)官方权重，[下载](https://github.com/Zeyi-Lin/HivisionIDPhotos/releases/download/pretrained-model/modnet_photographic_portrait_matting.onnx)
*   `hivision_modnet.onnx` (24.7MB): 对纯色换底适配性更好的抠图模型，[下载](https://github.com/Zeyi-Lin/HivisionIDPhotos/releases/download/pretrained-model/hivision_modnet.onnx)
*   `mnn_hivision_modnet.mnn` (24.7MB): mnn转换后的抠图模型 by [zjkhahah](https://github.com/zjkhahah)，[下载](https://github.com/Zeyi-Lin/HivisionIDPhotos/releases/download/pretrained-model/mnn_hivision_modnet.mnn)
*   `rmbg-1.4.onnx` (176.2MB): [BRIA AI](https://huggingface.co/briaai/RMBG-1.4) 开源的抠图模型，[下载](https://huggingface.co/briaai/RMBG-1.4/resolve/main/onnx/model.onnx?download=true)后重命名为`rmbg-1.4.onnx`

4\. 人脸检测模型配置
------------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#4-%E4%BA%BA%E8%84%B8%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E9%85%8D%E7%BD%AE)

> 这是一个可选项

拓展人脸检测模型

介绍

使用文档

MTCNN

**离线**人脸检测模型，高性能CPU推理，为默认模型，检测精度较低

Clone此项目后直接使用

Face++

旷视推出的在线人脸检测API，检测精度较高，[官方文档](https://console.faceplusplus.com.cn/documents/4888373)

[使用文档](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/face++_CN.md)

🚀 运行 Gradio Demo
-----------------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E8%BF%90%E8%A1%8C-gradio-demo)

运行程序将生成一个本地 Web 页面，在页面中可完成证件照的操作与交互。

[![](https://github.com/Zeyi-Lin/HivisionIDPhotos/raw/master/assets/harry.png)](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/assets/harry.png)

🚀 Python 推理
------------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-python-%E6%8E%A8%E7%90%86)

核心参数：

*   `-i`: 输入图像路径
*   `-o`: 保存图像路径
*   `-t`: 推理类型，有idphoto、human\_matting、add\_background、generate\_layout\_photos可选
*   `--matting_model`: 人像抠图模型权重选择，可选`hivision_modnet`、`modnet_photographic_portrait_matting`
*   `--face_detect_model`: 人脸检测模型选择，可选`mtcnn`、`face_plusplus`

更多参数可通过`python inference.py --help`查看

1\. 证件照制作
---------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#1-%E8%AF%81%E4%BB%B6%E7%85%A7%E5%88%B6%E4%BD%9C)

输入 1 张照片，获得 1 张标准证件照和 1 张高清证件照的 4 通道透明 png

python inference.py \-i demo/images/test.jpg \-o ./idphoto.png \-\-height 413 \-\-width 295

2\. 人像抠图
--------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#2-%E4%BA%BA%E5%83%8F%E6%8A%A0%E5%9B%BE)

python inference.py \-t human\_matting \-i demo/images/test.jpg \-o ./idphoto\_matting.png \-\-matting\_model hivision\_modnet

3\. 透明图增加底色
-----------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#3-%E9%80%8F%E6%98%8E%E5%9B%BE%E5%A2%9E%E5%8A%A0%E5%BA%95%E8%89%B2)

输入 1 张 4 通道透明 png，获得 1 张增加了底色的图像）

python inference.py \-t add\_background \-i ./idphoto.png \-o ./idphoto\_ab.jpg  \-c 4f83ce \-k 30 \-r 1

4\. 得到六寸排版照
-----------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#4-%E5%BE%97%E5%88%B0%E5%85%AD%E5%AF%B8%E6%8E%92%E7%89%88%E7%85%A7)

输入 1 张 3 通道照片，获得 1 张六寸排版照

python inference.py \-t generate\_layout\_photos \-i ./idphoto\_ab.jpg \-o ./idphoto\_layout.jpg  \-\-height 413 \-\-width 295 \-k 200

⚡️ 部署 API 服务
------------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#%EF%B8%8F-%E9%83%A8%E7%BD%B2-api-%E6%9C%8D%E5%8A%A1)

启动后端
----

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#%E5%90%AF%E5%8A%A8%E5%90%8E%E7%AB%AF)

请求 API 服务
---------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#%E8%AF%B7%E6%B1%82-api-%E6%9C%8D%E5%8A%A1)

详细请求方式请参考 [API 文档](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/api_CN.md)，包含以下请求示例：

*   [cURL](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/api_CN.md#curl-%E8%AF%B7%E6%B1%82%E7%A4%BA%E4%BE%8B)
*   [Python](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/api_CN.md#python-%E8%AF%B7%E6%B1%82%E7%A4%BA%E4%BE%8B)
*   [Java](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/api_CN.md#java-%E8%AF%B7%E6%B1%82%E7%A4%BA%E4%BE%8B)
*   [Javascript](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/api_CN.md#javascript-%E8%AF%B7%E6%B1%82%E7%A4%BA%E4%BE%8B)

🐳 Docker 部署
------------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-docker-%E9%83%A8%E7%BD%B2)

1\. 拉取或构建镜像
-----------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#1-%E6%8B%89%E5%8F%96%E6%88%96%E6%9E%84%E5%BB%BA%E9%95%9C%E5%83%8F)

> 以下方式三选一

**方式一：拉取最新镜像：**

docker pull linzeyi/hivision\_idphotos

**方式二：Dockrfile 直接构建镜像：**

在确保将模型权重文件[hivision\_modnet.onnx](https://github.com/Zeyi-Lin/HivisionIDPhotos/releases/tag/pretrained-model)放到`hivision/creator/weights`下后，在项目根目录执行：

docker build -t linzeyi/hivision\_idphotos .

**方式三：Docker compose 构建：**

确保将模型权重文件 [hivision\_modnet.onnx](https://github.com/Zeyi-Lin/HivisionIDPhotos/releases/tag/pretrained-model) 放在`hivision/creator/weights`下后，在项目根目录下执行：

2\. 运行服务
--------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#2-%E8%BF%90%E8%A1%8C%E6%9C%8D%E5%8A%A1)

**启动 Gradio Demo 服务**

运行下面的命令，在你的本地访问 [http://127.0.0.1:7860](http://127.0.0.1:7860/) 即可使用。

docker run -d -p 7860:7860 linzeyi/hivision\_idphotos

**启动 API 后端服务**

docker run -d -p 8080:8080 linzeyi/hivision\_idphotos python3 deploy\_api.py

**两个服务同时启动**

环境变量
----

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)

本项目提供了一些额外的配置项，使用环境变量进行设置：

环境变量

类型

描述

示例

FACE\_PLUS\_API\_KEY

可选

这是你在 Face++ 控制台申请的 API 密钥

`7-fZStDJ····`

FACE\_PLUS\_API\_SECRET

可选

Face++ API密钥对应的Secret

`VTee824E····`

docker使用环境变量示例：

docker run  -d -p 7860:7860 \\
    -e FACE\_PLUS\_API\_KEY=7-fZStDJ···· \\
    -e FACE\_PLUS\_API\_SECRET=VTee824E···· \\
    linzeyi/hivision\_idphotos 

📖 引用项目
-------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E5%BC%95%E7%94%A8%E9%A1%B9%E7%9B%AE)

1.  MTCNN:

@software{ipazc\_mtcnn\_2021,
    author = {ipazc},
    title = {{MTCNN}},
    url = {https://github.com/ipazc/mtcnn},
    year = {2021},
    publisher = {GitHub}
}

2.  ModNet:

@software{zhkkke\_modnet\_2021,
    author = {ZHKKKe},
    title = {{ModNet}},
    url = {https://github.com/ZHKKKe/MODNet},
    year = {2021},
    publisher = {GitHub}
}

💻 开发小贴士
--------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E5%BC%80%E5%8F%91%E5%B0%8F%E8%B4%B4%E5%A3%AB)

**1\. 如何修改预设尺寸？**

修改[size\_list\_CN.csv](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/demo/size_list_CN.csv)后再次运行 `app.py` 即可，其中第一列为尺寸名，第二列为高度，第三列为宽度。

📧 联系我们
-------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#-%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC)

如果您有任何问题，请发邮件至 [zeyi.lin@swanhub.co](mailto:zeyi.lin@swanhub.co)

贡献者
---

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#%E8%B4%A1%E7%8C%AE%E8%80%85)

[![](https://camo.githubusercontent.com/e2e05f7f5f80fdf35730cbe7774a8481cc66ca2312b6b95d3c70e9e234cf9daa/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d5a6579692d4c696e2f4869766973696f6e494450686f746f73)](https://github.com/Zeyi-Lin/HivisionIDPhotos/graphs/contributors)[Zeyi-Lin](https://github.com/Zeyi-Lin)、[SAKURA-CAT](https://github.com/SAKURA-CAT)、[Feudalman](https://github.com/Feudalman)、[swpfY](https://github.com/swpfY)、[Kaikaikaifang](https://github.com/Kaikaikaifang)、[ShaohonChen](https://github.com/ShaohonChen)、[KashiwaByte](https://github.com/KashiwaByte)

StarHistory
-----------

[](https://github.com/Zeyi-Lin/HivisionIDPhotos#starhistory)

[![Star History Chart](https://camo.githubusercontent.com/19ad37011092c322f66584b9a76b498cd3d0dcd72e6e8f38d9af4edaf370d6b7/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d5a6579692d4c696e2f4869766973696f6e494450686f746f7326747970653d44617465)](https://star-history.com/#Zeyi-Lin/HivisionIDPhotos&Date)
