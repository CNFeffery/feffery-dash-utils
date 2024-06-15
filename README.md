# feffery-dash-utils

包含一系列用于提升`Dash`应用开发效率的工具函数。

## 已有函数列表

### `style()`

用于快捷生成`Dash`组件的`style`参数字典，内置了绝大多数小驼峰命名格式的常用`css`属性。

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
