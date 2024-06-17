# feffery-dash-utils

包含一系列用于提升`Dash`应用开发效率的工具函数。

<div>

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/feffery-antd-components/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-dash-utils.svg?color=dark-green)](https://pypi.org/project/feffery-dash-utils/)

</div>

## 目录

[安装](#安装)<br>
[已有工具函数列表](#已有工具函数列表)<br>
[参与贡献](#参与贡献)<br>
[开发计划](#开发计划)

<a name="安装" ></a>

## 安装

```bash
pip install feffery-dash-utils -U
```

<a name="已有工具函数列表" ></a>

## 已有工具函数列表

- style_utils
  - [style()](#style)<br>

<a name="style" ></a>

### `style()`

用于快捷生成`Dash`组件的`style`参数字典，内置了绝大多数小驼峰命名格式的常用`css`属性，在常见 ide 中将鼠标悬停于参数名之上可查看对应的中英文属性功能介绍，内容基于`w3cschool`自动生成。

> 使用示例

```Python
from feffery_dash_utils.style_utils import style

# 方式一：直接编写键值对样式
fac.AntdText(
    '测试',
    style=style(
        fontSize=16,
        color='red'
    )
)

# 方式二：解析CSS代码片段
fac.AntdText(
    '测试',
    style=style(
        """
.IvkwhTOsc9wu6RdvHESR .yK52Sq0w7wspWaS28YNl {
    width: 91.46%;
    margin-left: 4.27%;
    margin-bottom: 5%;
    position: relative;
}"""
    )
)

# 方式三：混合使用
fac.AntdText(
    '测试',
    style=style(
        """
.IvkwhTOsc9wu6RdvHESR .yK52Sq0w7wspWaS28YNl {
    width: 91.46%;
    margin-left: 4.27%;
    margin-bottom: 5%;
    position: relative;
}""",
        fontSize=16,
        color='red'
    )
)
```

<a name="参与贡献" ></a>

## 参与贡献

```bash
git clone https://github.com/CNFeffery/feffery-dash-utils.git
cd feffery-dash-utils
# 安装开发环境所需依赖
pip install -r requirements/dev.txt
```

<a name="开发计划" ></a>

## 开发计划

- [ ] 样式相关工具函数子模块`style_utils`
  - [x] `style`参数编写辅助函数`style()`
- [ ] 布局相关工具函数子模块`layout_utils`
- [ ] 模板相关工具函数子模块`template_utils`
- [ ] 表格相关工具函数子模块`table_utils`
- [ ] 回调函数相关工具函数子模块`callback_utils`
- [ ] 树形处理相关工具函数子模块`tree_utils`
