# feffery-dash-utils

包含一系列用于提升`Dash`应用开发效率的工具函数。

<div>

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/feffery-antd-components/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-antd-components.svg?color=dark-green)](https://pypi.org/project/feffery-antd-components/)

</div>

## 安装

```bash
pip install feffery-dash-utils -U
```

## 已有工具函数列表

### `style()`

用于快捷生成`Dash`组件的`style`参数字典，内置了绝大多数小驼峰命名格式的常用`css`属性，在常见 ide 中将鼠标悬停于参数名之上可查看对应的中英文属性功能介绍，内容基于`w3cschool`。

#### 使用示例

```Python
from feffery_dash_utils.style_utils import style

fac.AntdText(
    '测试',
    style=style(
        fontSize=16,
        color='red'
    )
)
```
