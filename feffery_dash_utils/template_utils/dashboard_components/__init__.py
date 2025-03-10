from dash import html
from typing import Union
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
from dash.development.base_component import Component

__ALL__ = ['welcome_card', 'blank_card', 'simple_chart_card', 'index_card']


def welcome_card(
    title: Component = None,
    description: Component = None,
    avatar: Component = None,
    extra: Component = None,
) -> Component:
    """欢迎卡片

    Args:
        title (Component, optional): 标题元素. Defaults to None.
        description (Component, optional): 标题下方辅助描述元素. Defaults to None.
        avatar (Component, optional): 头像元素. Defaults to None.
        extra (Component, optional): 额外元素. Defaults to None.

    Returns:
        Component: 构造完成的欢迎卡片
    """

    return html.Div(
        fac.AntdFlex(
            [
                fac.AntdSpace(
                    [
                        avatar,
                        fac.AntdSpace(
                            [
                                fac.AntdText(
                                    title, strong=True, style=style(fontSize=20)
                                ),
                                fac.AntdText(
                                    description,
                                    type='secondary',
                                ),
                            ],
                            size='small',
                            direction='vertical',
                        ),
                    ],
                    size=18,
                ),
                extra,
            ],
            justify='space-between',
            align='center',
        ),
        style=style(
            padding=20,
            background='#fff',
            borderRadius=8,
            boxSizing='border-box',
            boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
        ),
    )


def blank_card(children: Component = None) -> Component:
    """空白卡片

    Args:
        children (Component, optional): 子元素. Defaults to None.

    Returns:
        Component: 构造完成的卡片
    """

    return html.Div(
        children,
        style=style(
            padding=20,
            background='#fff',
            borderRadius=8,
            boxSizing='border-box',
            boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
        ),
    )


def simple_chart_card(
    title: Component = None,
    description: Component = None,
    chart: Component = None,
    extra: Component = None,
    height: Union[int, float, str] = 300,
) -> Component:
    """简单图表卡片

    Args:
        title (Component, optional): 标题元素. Defaults to None.
        description (Component, optional): 标题右侧辅助描述元素. Defaults to None.
        chart (Component, optional): 图表元素. Defaults to None.
        extra (Component, optional): 额外元素. Defaults to None.
        height (Union[int, float, str], optional): 卡片高度. Defaults to 300.

    Returns:
        Component: 构造完成的简单图表卡片
    """

    return html.Div(
        fac.AntdFlex(
            [
                fac.AntdFlex(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdText(
                                    title,
                                    strong=True,
                                    style=style(
                                        fontSize=20,
                                    ),
                                ),
                                (
                                    description
                                    and fac.AntdText(
                                        description, type='secondary'
                                    )
                                ),
                            ],
                            size=4,
                            align='baseline',
                        ),
                        extra,
                    ],
                    justify='space-between',
                ),
                fac.AntdDivider(
                    lineColor='#f0f0f0',
                    style=style(marginTop=12, marginBottom=12),
                ),
                html.Div(chart, style=style(height='100%')),
            ],
            vertical=True,
            gap=0,
            style=style(width='100%', height='100%'),
        ),
        style=style(
            height=height,
            padding=20,
            background='#fff',
            borderRadius=8,
            boxSizing='border-box',
            boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
        ),
    )


def index_card(
    index_name: Component = None,
    index_description: Component = None,
    index_value: Component = None,
    extra_content: Component = None,
    footer_content: Component = None,
) -> Component:
    """指标卡片

    Args:
        index_name (Component, optional): 指标名称. Defaults to None.
        index_description (Component, optional): 指标描述内容. Defaults to None.
        index_value (Component, optional): 指标值元素. Defaults to None.
        extra_content (Component, optional): 额外元素. Defaults to None.
        footer_content (Component, optional): 底部元素. Defaults to None.

    Returns:
        Component: 构造完成的指标卡片
    """

    return html.Div(
        fac.AntdSpace(
            [
                fac.AntdFlex(
                    [
                        fac.AntdFlex(
                            [
                                index_name,
                                (
                                    index_description
                                    and fac.AntdTooltip(
                                        fac.AntdIcon(
                                            icon='antd-info-circle',
                                        ),
                                        title=index_description,
                                    )
                                ),
                            ],
                            justify='space-between',
                            style=style(
                                color='rgba(0, 0, 0, 0.65)', fontSize=16
                            ),
                        ),
                        fac.AntdText(index_value, style=style(fontSize=28)),
                    ],
                    vertical=True,
                    justify='space-between',
                    style=style(height=64, overflowY='hidden'),
                ),
                html.Div(
                    html.Div(extra_content, style=style(height='100%')),
                    style=style(
                        height=56,
                        marginBottom=12,
                        overflowX='hidden',
                        overflowY='hidden',
                    ),
                ),
                fac.AntdDivider(style=style(marginTop=0, marginBottom=0)),
                html.Div(
                    footer_content,
                    style=style(
                        height=22,
                        paddingTop=9,
                        overflowY='hidden',
                    ),
                ),
            ],
            size=0,
            direction='vertical',
            style=style(width='100%'),
        ),
        style=style(
            padding='20px 20px 8px',
            background='#fff',
            borderRadius=8,
            boxSizing='border-box',
            boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
        ),
    )
