"""
cd scripts
python generate_style_utils.py
"""

import re
from DrissionPage import SessionPage

page = SessionPage()

# 访问中文目标页面
page.get('https://www.w3school.com.cn/cssref/index.asp')

raw_texts = [
    item.raw_text
    for item in page.eles(
        'xpath://table[@class="dataintable"]//td'
    )
]

# 构造中文css常用属性字典
zh_cn_styles = {
    name: description
    for name, description in zip(
        raw_texts[:-1:2], raw_texts[1::2]
    )
}

# 访问英文目标页面
page.get('https://www.w3schools.com/cssref/index.php')

raw_texts = [
    item.raw_text
    for item in page.eles(
        'xpath://table[contains(@class, "ws-table-all")]//td'
    )
]

# 构造英文css常用属性字典
en_us_styles = {
    name: description
    for name, description in zip(
        raw_texts[:-1:2], raw_texts[1::2]
    )
}


# 合并中英文css常用属性字典
styles = {
    ''.join(
        [
            s if i == 0 else s.capitalize()
            for i, s in enumerate(key.split('-'))
        ]
    ): '{}  {}'.format(
        zh_cn_styles[key].replace('\n', ' '),
        re.sub(
            ' {2,}',
            ' ',
            en_us_styles[key].replace('\n', ' '),
        ),
    )
    for key in (
        set(zh_cn_styles.keys()) & set(en_us_styles.keys())
    )
    if re.match('[\-a-z]+', key)
}

# 生成style_utils.py文件

raw_code = '''import inspect

def style(
<函数参数定义>
    **kwargs
) -> dict:
    """
    Args:
<函数参数说明>
"""

    _, _, _, args = inspect.getargvalues(inspect.currentframe())
    kwargs = args.pop('kwargs')
    # 去除None值属性
    args = {key: value for key, value in args.items() if value is not None}
    return {**args, **kwargs}
'''

# 生成<函数参数定义>
raw_code = raw_code.replace(
    '<函数参数定义>',
    '\n'.join(
        [
            '    {}=None,'.format(key)
            for key in sorted(styles.keys())
        ]
    ),
)

# 生成<函数参数说明>
raw_code = raw_code.replace(
    '<函数参数说明>',
    '\n'.join(
        [
            '        - {}: {}'.format(key, styles[key])
            for key in sorted(styles.keys())
        ]
    ),
)

with open(
    '../feffery_dash_utils/style_utils/style.py',
    'w',
    encoding='utf-8',
) as f:
    f.write(raw_code)
    print('style_utils.py文件生成成功')
