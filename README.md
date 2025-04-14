# feffery-dash-utils

简体中文 | [English](./README-en_US.md)

包含一系列用于提升`Dash`应用开发效率的工具函数/工具类。

<div>

[![Pyhton](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](./setup.py)
[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/feffery-antd-components/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-dash-utils.svg?color=dark-green)](https://pypi.org/project/feffery-dash-utils/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

</div>

## 目录

[安装](#install)<br>
[配合 vscode 插件](#with-vscode)<br>
[已有工具函数/工具类列表](#utils-list)<br>
[参与贡献](#contribute)<br>
[开发计划](#roadmap)

<a name="install" ></a>

## 安装

```bash
pip install feffery-dash-utils -U
```

<a name="with-vscode" ></a>

## 配合 vscode 插件

在`vscode`中配合插件[feffery-dash-snippets](https://github.com/CNFeffery/feffery-dash-snippets)可快捷实现对各工具函数/工具类的快捷导入，在`Python`文件中输入`utils:`即可触发相关快捷命令。

<a name="utils-list" ></a>

## 已有工具函数/工具类列表

- style_utils
  - [style()](#style)<br>
- tree_utils
  - [TreeManager](#TreeManager)<br>
    - [update_tree_node()](#update_tree_node)<br>
    - [add_node_before()](#add_node_before)<br>
    - [add_node_after()](#add_node_after)<br>
    - [delete_node()](#delete_node)<br>
    - [get_node()](#get_node)<br>
- i18n_utils
  - [Translator](#Translator)
- template_utils
  - [dashboard_components](#dashboard_components)
    - [welcome_card()](#welcome_card)<br>
    - [blank_card()](#blank_card)<br>
    - [simple_chart_card()](#simple_chart_card)<br>
    - [index_card()](#index_card)<br>
- version_utils
  - [check_python_version()](#check_python_version)<br>
  - [check_dependencies_version()](#check_dependencies_version)<br>

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

<a name="TreeManager" ></a>

### `TreeManager`

用于对类似`AntdTree`、`AntdTreeSelect`等树形组件所依赖的树形结构数据进行快捷管理操作，具体包含的方法有：

<a name="update_tree_node" ></a>

#### `update_tree_node()`

用于对树形结构数据中指定`key`对应节点进行整体或增量更新。

> 使用示例

```Python
from feffery_dash_utils.tree_utils import TreeManager

# 示例树形数据
demo_tree = [
    {
        'title': '节点1',
        'key': '节点1',
        'children': [
            {
                'title': '节点1-1',
                'key': '节点1-1',
                'children': [
                    {
                        'title': '节点1-1-1',
                        'key': '节点1-1-1',
                    },
                    {
                        'title': '节点1-1-2',
                        'key': '节点1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': '节点2', 'key': '节点2'},
]

# 对示例树形数据指定节点进行整体替换
TreeManager.update_tree_node(
    demo_tree,
    '节点1-1',
    {'title': '节点1-1', 'key': '节点1-1'},
)

# 对示例树形数据指定节点进行增量更新
TreeManager.update_tree_node(
    demo_tree,
    '节点1-1',
    {'title': '节点1-1new'},
    'overlay',
)
```

<a name="add_node_before" ></a>

#### `add_node_before()`

在树形结构数据中指定`key`对应节点之前插入平级新节点。

> 使用示例

```Python
from feffery_dash_utils.tree_utils import TreeManager

# 示例树形数据
demo_tree = [
    {
        'title': '节点1',
        'key': '节点1',
        'children': [
            {
                'title': '节点1-1',
                'key': '节点1-1',
                'children': [
                    {
                        'title': '节点1-1-1',
                        'key': '节点1-1-1',
                    },
                    {
                        'title': '节点1-1-2',
                        'key': '节点1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': '节点2', 'key': '节点2'},
]

# 在示例树形数据指定节点前插入平级新节点
TreeManager.add_node_before(
    demo_tree,
    '节点1-1',
    {'title': '节点1-0', 'key': '节点1-0'},
)
```

<a name="add_node_after" ></a>

#### `add_node_after()`

在树形结构数据中指定`key`对应节点之后插入平级新节点。

> 使用示例

```Python
from feffery_dash_utils.tree_utils import TreeManager

# 示例树形数据
demo_tree = [
    {
        'title': '节点1',
        'key': '节点1',
        'children': [
            {
                'title': '节点1-1',
                'key': '节点1-1',
                'children': [
                    {
                        'title': '节点1-1-1',
                        'key': '节点1-1-1',
                    },
                    {
                        'title': '节点1-1-2',
                        'key': '节点1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': '节点2', 'key': '节点2'},
]

# 在示例树形数据指定节点后插入平级新节点
TreeManager.add_node_after(
    demo_tree,
    '节点1-1',
    {'title': '节点1-2', 'key': '节点1-2'},
)
```

<a name="delete_node" ></a>

#### `delete_node()`

删除树形结构数据中指定`key`对应节点。

> 使用示例

```Python
from feffery_dash_utils.tree_utils import TreeManager

# 示例树形数据
demo_tree = [
    {
        'title': '节点1',
        'key': '节点1',
        'children': [
            {
                'title': '节点1-1',
                'key': '节点1-1',
                'children': [
                    {
                        'title': '节点1-1-1',
                        'key': '节点1-1-1',
                    },
                    {
                        'title': '节点1-1-2',
                        'key': '节点1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': '节点2', 'key': '节点2'},
]

# 删除示例树形数据指定节点
TreeManager.delete_node(demo_tree, '节点2')
```

<a name="get_node" ></a>

#### `get_node()`

查询树形结构数据中指定`key`对应节点。

> 使用示例

```Python
from feffery_dash_utils.tree_utils import TreeManager

# 示例树形数据
demo_tree = [
    {
        'title': '节点1',
        'key': '节点1',
        'children': [
            {
                'title': '节点1-1',
                'key': '节点1-1',
                'children': [
                    {
                        'title': '节点1-1-1',
                        'key': '节点1-1-1',
                    },
                    {
                        'title': '节点1-1-2',
                        'key': '节点1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': '节点2', 'key': '节点2'},
]

# 查询示例树形数据中存在的指定节点
TreeManager.get_node(demo_tree, '节点1-1')

# 查询示例树形数据中不存在的指定节点（将返回None）
TreeManager.get_node(demo_tree, '节点1-666')
```

<a name="Translator" ></a>

### `Translator`

用于在`Dash`应用中快捷构建国际化多语种方案，基于前端`cookies`和本地国际化配置文件驱动。

> 使用示例

示例应用见[i18n_test_app.py](/tests/i18n_utils/i18n_test_app.py)、[i18n_multi_test_app.py](/tests/i18n_utils/i18n_multi_test_app.py)，参考配置文件见[locales.json](/tests/i18n_utils/locales.json)、[locales1.json](/tests/i18n_utils/multi_locales/locales1.json)、[locales2.json](/tests/i18n_utils/multi_locales/locales2.json)

<a name="dashboard_components" ></a>

### `dashboard_components`

内置数据仪表盘页面搭建常用自定义组件，具体包含的组件有：

<a name="welcome_card" ></a>

#### `welcome_card()`

欢迎卡片。

<a name="blank_card" ></a>

#### `blank_card()`

空白卡片。

<a name="simple_chart_card" ></a>

#### `simple_chart_card()`

简单图表卡片。

<a name="index_card" ></a>

#### `index_card()`

指标卡片。

<a name="version_utils" ></a>

### `version_utils`

提供包含`Python`版本检查、依赖库版本检查等一系列与项目依赖版本相关的工具函数。

<a name="check_python_version" ></a>

#### `check_python_version()`

用于检查当前`Python`版本是否满足项目要求。

> 使用示例

```Python
from feffery_dash_utils.version_utils import check_python_version

check_python_version(
    min_version='3.8',
    max_version='3.12'
)

```

<a name="check_dependencies_version" ></a>

#### `check_dependencies_version()`

用于检查当前项目依赖库版本是否满足项目要求。

> 使用示例

```Python
from feffery_dash_utils.version_utils import check_dependencies_version

check_dependencies_version(
    rules=[
        {
            'name': 'dash',
            'specifier': '<=2.18.2'
        }
    ]
)

```

<a name="contribute" ></a>

## 参与贡献

```bash
git clone https://github.com/CNFeffery/feffery-dash-utils.git
cd feffery-dash-utils
# 安装开发环境所需依赖
pip install -r requirements/dev.txt
```

<a name="roadmap" ></a>

## 开发计划

- [ ] 样式相关工具函数子模块`style_utils`
  - [x] `style`参数编写辅助函数`style()`
- [ ] 模板相关工具函数子模块`template_utils`
  - [x] 仪表盘常用自定义组件子模块`dashboard_components`
    - [x] 欢迎卡片`welcome_card()`
    - [x] 空白卡片`blank_card()`
    - [x] 简单图表卡片`simple_chart_card()`
    - [x] 指标卡片`index_card()`
- [ ] 树形处理相关工具函数子模块`tree_utils`
  - [x] 树形数据结构管理类`TreeManager`
    - [x] 树节点更新函数`update_tree_node()`
    - [x] 树节点前置插入函数`add_node_before()`
    - [x] 树节点后置插入函数`add_node_after()`
    - [x] 树节点删除函数`delete_node()`
    - [x] 树节点查询函数`get_node()`
- [ ] 国际化相关工具函数子模块`i18n_utils`
  - [x] 文案内容快捷国际化操作类`Translator`
- [ ] 版本控制相关工具函数子模块`version_utils`
  - [x] `Python`版本检查函数`check_python_version()`
  - [x] 依赖库版本检查函数`check_dependencies_version()`
