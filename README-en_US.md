# feffery-dash-utils

[简体中文](./README.md) | English

Contains a series of tool functions/classes designed to enhance the development efficiency of `Dash` applications.

<div>

[![Pyhton](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](./setup.py)
[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/feffery-antd-components/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-dash-utils.svg?color=dark-green)](https://pypi.org/project/feffery-dash-utils/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

</div>

## Table of Contents

[Install](#install)<br>
[Use with vscode plugin](#with-vscode)<br>
[Utils List](#utils-list)<br>
[Contribute](#contribute)<br>
[Roadmap](#roadmap)

<a name="install" ></a>

## Install

```bash
pip install feffery-dash-utils -U
```

<a name="with-vscode" ></a>

## Use with vscode plugin

In `vscode`, with the plugin [feffery-dash-snippets](https://github.com/CNFeffery/feffery-dash-snippets), you can quickly import various utility functions and classes. In a `Python` file, typing `utils:` will trigger the relevant quick commands.

<a name="utils-list" ></a>

## Utils List

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

Used for quickly generating the `style` parameter dictionary of `Dash` components, it includes most of the commonly used `css` properties in camelCase naming format. Hovering the mouse over the parameter name in common IDEs will display the corresponding Chinese and English property introductions, which are automatically generated based on `w3cschool`.

> Usage Example

```Python
from feffery_dash_utils.style_utils import style

# Method one: Directly write key-value pair styles
fac.AntdText(
    'Test',
    style=style(
        fontSize=16,
        color='red'
    )
)

# Method two: Parse CSS code snippets
fac.AntdText(
    'Test',
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

# Method three: Mixed use
fac.AntdText(
    'Test',
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

Used for quick management operations on tree structure data that components like `AntdTree` and `AntdTreeSelect` depend on. The specific methods included are:

<a name="update_tree_node" ></a>

#### `update_tree_node()`

Used to perform overall or incremental updates on a specified `key` corresponding node in the tree structure data.

> Usage Example

```Python
from feffery_dash_utils.tree_utils import TreeManager

# Example tree data
demo_tree = [
    {
        'title': 'Node 1',
        'key': 'Node 1',
        'children': [
            {
                'title': 'Node 1-1',
                'key': 'Node 1-1',
                'children': [
                    {
                        'title': 'Node 1-1-1',
                        'key': 'Node 1-1-1',
                    },
                    {
                        'title': 'Node 1-1-2',
                        'key': 'Node 1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': 'Node 2', 'key': 'Node 2'},
]

# Replace a specified node in the example tree data as a whole
TreeManager.update_tree_node(
    demo_tree,
    'Node 1-1',
    {'title': 'Node 1-1', 'key': 'Node 1-1'},
)

# Incrementally update a specified node in the example tree data
TreeManager.update_tree_node(
    demo_tree,
    'Node 1-1',
    {'title': 'Node 1-1new'},
    'overlay',
)
```

<a name="add_node_before" ></a>

#### `add_node_before()`

Insert a new sibling node before the specified `key` corresponding node in the tree structure data.

> Usage Example

```Python
from feffery_dash_utils.tree_utils import TreeManager

# Example tree data
demo_tree = [
    {
        'title': 'Node 1',
        'key': 'Node 1',
        'children': [
            {
                'title': 'Node 1-1',
                'key': 'Node 1-1',
                'children': [
                    {
                        'title': 'Node 1-1-1',
                        'key': 'Node 1-1-1',
                    },
                    {
                        'title': 'Node 1-1-2',
                        'key': 'Node 1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': 'Node 2', 'key': 'Node 2'},
]

# Insert a new sibling node before the specified node in the example tree data
TreeManager.add_node_before(
    demo_tree,
    'Node 1-1',
    {'title': 'Node 1-0', 'key': 'Node 1-0'},
)
```

<a name="add_node_after" ></a>

#### `add_node_after()`

Insert a new sibling node after the specified `key` corresponding node in the tree structure data.

> Usage Example

```Python
from feffery_dash_utils.tree_utils import TreeManager

# Example tree data
demo_tree = [
    {
        'title': 'Node 1',
        'key': 'Node 1',
        'children': [
            {
                'title': 'Node 1-1',
                'key': 'Node 1-1',
                'children': [
                    {
                        'title': 'Node 1-1-1',
                        'key': 'Node 1-1-1',
                    },
                    {
                        'title': 'Node 1-1-2',
                        'key': 'Node 1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': 'Node 2', 'key': 'Node 2'},
]

# Insert a new sibling node after the specified node in the example tree data
TreeManager.add_node_after(
    demo_tree,
    'Node 1-1',
    {'title': 'Node 1-2', 'key': 'Node 1-2'},
)
```

<a name="delete_node" ></a>

#### `delete_node()`

Delete the node corresponding to the specified `key` in the tree structure data.

> Usage Example

```Python
from feffery_dash_utils.tree_utils import TreeManager

# Example tree data
demo_tree = [
    {
        'title': 'Node 1',
        'key': 'Node 1',
        'children': [
            {
                'title': 'Node 1-1',
                'key': 'Node 1-1',
                'children': [
                    {
                        'title': 'Node 1-1-1',
                        'key': 'Node 1-1-1',
                    },
                    {
                        'title': 'Node 1-1-2',
                        'key': 'Node 1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': 'Node 2', 'key': 'Node 2'},
]

# Delete the specified node in the example tree data
TreeManager.delete_node(demo_tree, 'Node 2')
```

<a name="get_node" ></a>

#### `get_node()`

Query the node corresponding to the specified `key` in the tree structure data.

> Usage Example

```Python
from feffery_dash_utils.tree_utils import TreeManager

# Example tree data
demo_tree = [
    {
        'title': 'Node 1',
        'key': 'Node 1',
        'children': [
            {
                'title': 'Node 1-1',
                'key': 'Node 1-1',
                'children': [
                    {
                        'title': 'Node 1-1-1',
                        'key': 'Node 1-1-1',
                    },
                    {
                        'title': 'Node 1-1-2',
                        'key': 'Node 1-1-2',
                    },
                ],
            }
        ],
    },
    {'title': 'Node 2', 'key': 'Node 2'},
]

# Query the specified node in the example tree data
TreeManager.get_node(demo_tree, 'Node 1-1')

# Query a specified node that does not exist in the example tree data (will return None)
TreeManager.get_node(demo_tree, 'Node 1-666')
```

<a name="Translator" ></a>

### `Translator`

Used for quickly building an internationalization and multi-language solution in `Dash` applications, driven by front-end `cookies` and local internationalization configuration files.

> Usage Example

Example applications can be found in [i18n_test_app.py](/tests/i18n_utils/i18n_test_app.py) and [i18n_multi_test_app.py](/tests/i18n_utils/i18n_multi_test_app.py), and reference configuration files can be found in [locales.json](/tests/i18n_utils/locales.json), [locales1.json](/tests/i18n_utils/multi_locales/locales1.json), and [locales2.json](/tests/i18n_utils/multi_locales/locales2.json).

<a name="dashboard_components" ></a>

### `dashboard_components`

Built-in data dashboard page building common custom components, including:

<a name="welcome_card" ></a>

#### `welcome_card()`

Welcome card.

<a name="blank_card" ></a>

#### `blank_card()`

Blank card.

<a name="simple_chart_card" ></a>

#### `simple_chart_card()`

Simple chart card.

<a name="index_card" ></a>

#### `index_card()`

Index card.

<a name="version_utils" ></a>

### `version_utils`

Provides a series of utility functions related to project dependency versions, including Python version checking and dependency library version checking.

<a name="check_python_version" ></a>

#### `check_python_version()`

Used to check if the current Python version meets the project requirements.

> Usage Example

```Python
from feffery_dash_utils.version_utils import check_python_version

check_python_version(
    min_version='3.8',
    max_version='3.12'
)

```

<a name="check_dependencies_version" ></a>

#### `check_dependencies_version()`

Used to check if the current project dependency library versions meet the project requirements.

> Usage Example

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

## Contribute

```bash
git clone https://github.com/CNFeffery/feffery-dash-utils.git
cd feffery-dash-utils
# Install dependencies required for the development environment
pip install -r requirements/dev.txt
```

<a name="roadmap" ></a>

## Roadmap

- [ ] Style-related utility function submodule `style_utils`
  - [x] `style` parameter writing assistant function `style()`
- [ ] Template-related utility function submodule `template_utils`
  - [x] Dashboard common custom component submodule `dashboard_components`
    - [x] Welcome card `welcome_card()`
    - [x] Blank card `blank_card()`
    - [x] Simple chart card `simple_chart_card()`
    - [x] Index card `index_card()`
- [ ] Tree processing-related utility function submodule `tree_utils`
  - [x] Tree data structure management class `TreeManager`
    - [x] Tree node update function `update_tree_node()`
    - [x] Tree node front insertion function `add_node_before()`
    - [x] Tree node rear insertion function `add_node_after()`
    - [x] Tree node deletion function `delete_node()`
    - [x] Tree node query function `get_node()`
- [ ] Internationalization-related utility function submodule `i18n_utils`
  - [x] Text content quick internationalization operation class `Translator`
- [ ] Version control-related utility function submodule `version_utils`
  - [x] `Python` version check function `check_python_version()`
  - [x] Dependencies version check function `check_dependencies_version()`
- [ ] Component parameter auxiliary generation utility function submodule `component_prop_utils`  
 - [x] Auxiliary generation utility function `to_box_data()` for the `data` parameter of the `fact.AntdBox` box plot component