# Marimo 学习教程源码库

## 项目简介

这是一个专门用于学习 Marimo 教程的源代码库。[Marimo](https://github.com/marimo-team/marimo) 是一个开源的响应式笔记本，旨在简化 Python 开发过程中的界面设计和交互实现。通过本教程，我们将逐步学习 Marimo 的核心功能，并通过实际项目加深理解。

## 项目里程碑

### 第一阶段：教程篇
- **目标**：学习 Marimo 中的 UI 库基础组件，掌握各个基本组件的使用方法。

### 第二阶段：应用篇
- **目标**：通过复刻小项目来进一步巩固 Marimo 的应用。

## 进度表

| 教程编号 | 教程标题           | 视频链接                         | 源代码          | 浏览器预览* | 更新于 |
|----------|------------------|--------------------------------|----------------|-----------|-----------|
| 001      | Marimo 导引      | [初见-这是伪装成markdown的编程工具？](https://www.bilibili.com/video/BV1eMpqekEAf) | [源代码](./tutorial/e01_first_guide.py) | - | 2024.09.09 |
| 002      | 时间滑动条       | [古希腊掌管时间的神（日期选择与滑动条）](https://www.bilibili.com/video/BV1jrtseFEXQ) | [源代码](./tutorial/e02_time_progress.py) | - | 2024.09.16 |
| 003      | 文件浏览和编辑    | [谁是幸运儿（文件浏览与代码编辑器）](https://www.bilibili.com/video/BV19Rt6evEhU) | [源代码](./tutorial/e03_random_file.py) | - | 2024.09.21 |
| 004      | 文本输入与提交    | [热点检索工具（热点之词云展示）](https://www.bilibili.com/video/BV1CtxyeXEbc) | [源代码](./tutorial/e04_hot_search.py) | - | 2024.09.29 |
| 005      | UI 批处理       | [登录框（Batch 批量化）](https://www.bilibili.com/video/BV1uk1DYjEAu) | [源代码](./tutorial/e05_login_box.py) | [![Open](https://marimo.io/shield.svg)](https://marimo.app/?slug=r02qcv) | 2024.10.05 |
| 006      | 数组和字典       | [点杯奶茶（数组化与字典化）](https://www.bilibili.com/video/BV11f1eY8Ers) | [源代码](./tutorial/e06_dict_and_array.py) | [![Open](https://marimo.io/shield.svg)](https://marimo.app/?slug=ypougm) | 2024.10.06 |
| 007      | 开关和按钮       | [开关和按钮](https://www.bilibili.com/video/BV1GP26YxEAr) | [源代码](./tutorial/e07_run_button.py) | [![Open](https://marimo.io/shield.svg)](https://marimo.app/?slug=qidvhf) | 2024.10.14 |

### 如何使用本教程源码？

1. 假设你已经安装了 Python 环境但还没有安装 marimo，那可以通过 `pip install marimo` 来安装
2. 克隆本项目或者点击右上角 Code -> Download Zip 下载到本地
3. 在命令行中运行如下代码， `marimo edit` 后可以换成任意你想打开的文件名
```bash
cd tutorial
marimo edit e02_time_progress.py
```

### 什么是浏览器预览？
借助 micropip 和浏览器的 wasm 机制，marimo 可以将 python 完全运行在浏览器中，无需本地环境即可运行。可以查阅表格对应链接的演示效果。

但目前只有部分教程支持，一部分是由于网络请求的跨域，另一部分是有些包尚且不兼容，希望这个问题后续有办法解决 :-)

# 联系方式

如果你在学习过程中遇到任何问题，欢迎随时联系作者。
- [b站](https://space.bilibili.com/497412)