# 灵签占卜 - 传统与现代交融的抽签体验

![GitHub Logo](https://img.shields.io/github/license/yourusername/lottery-app)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

一个基于Python和Tkinter开发的桌面灵签占卜程序，融合中国传统元素与现代UI设计理念，为用户打造沉浸式占卜体验。

---

## 🌟 功能亮点

### 1. **传统美学设计**
- 深蓝色星空背景搭配暖黄色主界面元素
- 精致的签筒矢量图形，还原传统中式占卜器具
- 六种签文类型：大吉、中吉、小吉、末吉、凶、大凶，每种签文配备专属解释

### 2. **动态交互体验**
- 点击求签按钮触发完整动画序列：
  - 签筒摇晃动画（8次左右摆动）
  - 星空背景随机闪烁效果
  - 色彩粒子爆炸效果（含重力下落）
  - 文字渐变显示效果
- 抽签结果区域边框颜色随签文类型变化

### 3. **字体容错机制**
支持字体加载失败时的降级处理，确保程序在不同系统环境下的稳定性：
```python
try:
    self.title_font = font.Font(family="Microsoft YaHei", size=24, weight="bold")
except:
    self.title_font = font.Font(size=24, weight="bold")
```

### 4. **透明度动画效果**
- 窗口透明度动态变化，增强视觉层次感
- 文字颜色渐变（支持tkinter 8.6+版本）

---

## 📦 安装方法

### 基本要求
- Python 3.6 或更高版本
- Tkinter库（通常随Python自带）

### 安装步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/yourusername/lottery-app.git
   cd lottery-app
   ```

2. 运行程序：
   ```bash
   python check.py
   ```

---

## 🖥️ 运行效果

![运行效果预览](docs/demo.gif)

- **启动界面**：星空背景下的抽签按钮和签筒
- **动画过程**：点击按钮后触发完整动画序列
- **结果展示**：抽签结果以彩色文本形式呈现

---

## 📂 项目结构

```
lottery-app/
├── check.py              # 主程序文件
├── README.md             # 项目说明
├── docs/                 # 文档和截图
│   └── demo.gif          # 动画演示
└── LICENSE               # 开源协议
```

---

## 🤝 贡献指南

欢迎提交Issue或Pull Request！我们鼓励以下类型的贡献：
- 新增签文类型和解释
- 优化动画效果
- 改进UI设计
- 增加多语言支持

---

## 📄 开源协议

本项目采用MIT开源协议。您可以在遵循协议条款的前提下自由使用、修改和分发本软件。

---

## 📣 特别说明

本程序仅供娱乐使用，结果不具有实际预测功能。我们尊重并倡导科学理性的生活态度。
