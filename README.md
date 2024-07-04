# feffery-dash-utils

包含一系列用于提升`Dash`应用开发效率的工具函数/工具类。

<div>

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/feffery-antd-components/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-dash-utils.svg?color=dark-green)](https://pypi.org/project/feffery-dash-utils/)

</div>

## 目录

[安装](#install)<br>
[已有工具函数列表](#utils-list)<br>
[参与贡献](#contribute)<br>
[开发计划](#roadmap)

<a name="install" ></a>

## 安装

```bash
pip install feffery-dash-utils -U
```

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
- [ ] 布局相关工具函数子模块`layout_utils`
- [ ] 模板相关工具函数子模块`template_utils`
- [ ] 表格相关工具函数子模块`table_utils`
- [ ] 回调函数相关工具函数子模块`callback_utils`
- [ ] 树形处理相关工具函数子模块`tree_utils`
  - [x] 树形数据结构管理类`TreeManager`
    - [x] 树节点更新函数`update_tree_node()`
    - [x] 树节点前置插入函数`add_node_before()`
    - [x] 树节点后置插入函数`add_node_after()`
    - [x] 树节点删除函数`delete_node()`
    - [x] 树节点查询函数`get_node()`
- [ ] 主题样式相关工具函数子模块`theme_utils`
