# GPT Image Generator and Editor

[English](#english) | [中文](#chinese)

<a name="english"></a>
## English

### Overview

This project provides a simple interface to Azure's AI image generation and editing capabilities. It allows you to:

1. Generate new images from text prompts
2. Edit existing images with text instructions
3. Apply masks to edit specific parts of images

### Requirements

- Python 3.x
- Azure account with API access to GPT image generation services
- Required Python packages (see `requirement.txt`):
  - python-dotenv
  - requests
  - IPython (for notebook functionality)

### Setup

1. **Important:** Create a `.env` file in the root directory with the following variables:
   ```
   AZURE_API_KEY=your_azure_api_key
   BASE_URL=your_azure_endpoint_url
   ```

2. Install required packages:
   ```
   pip install -r requirement.txt
   ```

### Usage

#### Through Python Code

```python
from azure_gpt_image import generate_image, edit_image

# Generate a new image
generate_image(
    prompt="A Studio Ghibli style picture of a brown dog riding a yellow Honda motorbike",
    size="1024x1024",  # Optional: Default is 1024x1024
    quality="medium",  # Optional: Default is "medium"
    out_path="my_image.png"  # Optional: Default is "generated_image.png"
)

# Edit an existing image
edit_image(
    image_path="my_image.png",
    prompt="Change the motorbike to white, keep everything else the same",
    mask_path=None,  # Optional: Path to a mask image
    out_path="edited_image.png"  # Optional: Default is "edited_image.png"
)
```

#### Through Jupyter Notebook

The project includes a sample notebook `gpt-image.ipynb` that demonstrates basic usage.

### Output

Generated and edited images are saved as PNG files in your project directory.

---

<a name="chinese"></a>
## 中文

### 概述

此项目提供了一个简单的接口来使用Azure的AI图像生成和编辑功能。它允许你：

1. 根据文本提示生成新图像
2. 使用文本指令编辑现有图像
3. 应用蒙版来编辑图像的特定部分

### 要求

- Python 3.x
- 具有GPT图像生成服务API访问权限的Azure账户
- 所需Python包（见`requirement.txt`）：
  - python-dotenv
  - requests
  - IPython（用于笔记本功能）

### 设置

1. **重要：** 在根目录下创建一个`.env`文件，包含以下变量：
   ```
   AZURE_API_KEY=你的azure_api_key
   BASE_URL=你的azure端点url
   ```

2. 安装所需包：
   ```
   pip install -r requirement.txt
   ```

### 使用方法

#### 通过Python代码

```python
from azure_gpt_image import generate_image, edit_image

# 生成新图像
generate_image(
    prompt="一个吉卜力风格的画，一只棕色的狗骑着一辆黄色的本田摩托车",
    size="1024x1024",  # 可选：默认为1024x1024
    quality="medium",  # 可选：默认为"medium"
    out_path="my_image.png"  # 可选：默认为"generated_image.png"
)

# 编辑现有图像
edit_image(
    image_path="my_image.png",
    prompt="将摩托车改为白色，其它保持不变",
    mask_path=None,  # 可选：蒙版图像的路径
    out_path="edited_image.png"  # 可选：默认为"edited_image.png"
)
```

#### 通过Jupyter笔记本

项目包含一个示例笔记本`gpt-image.ipynb`，展示了基本用法。

### 输出

生成和编辑的图像将作为PNG文件保存在项目目录中。
