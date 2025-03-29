from dash import html
from typing import Union
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
from dash.development.base_component import Component

__ALL__ = ['welcome_card', 'blank_card', 'simple_chart_card', 'index_card']

_Component = Union[Component, str, int, float, list]


def welcome_card(
    title: _Component = None,
    description: _Component = None,
    avatar: _Component = None,
    extra: _Component = None,
    root_id: Union[str, dict] = None,
    rootStyle: dict = None,
    rootClassName: str = None,
    titleStyle: dict = None,
    titleClassName: str = None,
    descriptionStyle: dict = None,
    descriptionClassName: str = None,
) -> Component:
    """欢迎卡片

    Args:
        title (Component, optional): 标题元素. Defaults to None.
        description (Component, optional): 标题下方辅助描述元素. Defaults to None.
        avatar (Component, optional): 头像元素. Defaults to None.
        extra (Component, optional): 额外元素. Defaults to None.
        root_id (Union[str, dict], optional): 根元素id. Defaults to None.
        rootStyle (dict, optional): 根元素样式. Defaults to None.
        rootClassName (str, optional): 根元素类名. Defaults to None.
        titleStyle (dict, optional): 标题样式. Defaults to None.
        titleClassName (str, optional): 标题类名. Defaults to None.
        descriptionStyle (dict, optional): 描述样式. Defaults to None.
        descriptionClassName (str, optional): 描述类名. Defaults to None.

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
                                    title,
                                    strong=True,
                                    className=titleClassName,
                                    style={
                                        **dict(fontSize=20),
                                        **(titleStyle or {}),
                                    },
                                ),
                                fac.AntdText(
                                    description,
                                    type='secondary',
                                    className=descriptionClassName,
                                    style=descriptionStyle,
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
        className=rootClassName,
        style={
            **dict(
                padding=20,
                background='#fff',
                borderRadius=8,
                boxSizing='border-box',
                boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            ),
            **(rootStyle or {}),
        },
        **(dict(id=root_id) if root_id else {}),
    )


def blank_card(
    children: _Component = None,
    root_id: Union[str, dict] = None,
    rootStyle: dict = None,
    rootClassName: str = None,
    backgroundImage: str = None,
) -> Component:
    """空白卡片

    Args:
        children (Component, optional): 子元素. Defaults to None.
        root_id (Union[str, dict], optional): 根元素id. Defaults to None.
        rootStyle (dict, optional): 根元素样式. Defaults to None.
        rootClassName (str, optional): 根元素类名. Defaults to None.
        backgroundImage (str, optional): 背景图url. Defaults to None.

    Returns:
        Component: 构造完成的卡片
    """

    return html.Div(
        children,
        className=rootClassName,
        style={
            **dict(
                padding=20,
                background='#fff',
                borderRadius=8,
                boxSizing='border-box',
                boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            ),
            **(rootStyle or {}),
            **(
                style(
                    backgroundImage=f'url({backgroundImage})',
                    backgroundSize='cover',
                    backgroundPosition='center',
                )
                if backgroundImage
                else {}
            ),
        },
        **(dict(id=root_id) if root_id else {}),
    )


def simple_chart_card(
    title: _Component = None,
    description: _Component = None,
    chart: _Component = None,
    extra: _Component = None,
    height: Union[int, float, str] = 300,
    root_id: Union[str, dict] = None,
    rootStyle: dict = None,
    rootClassName: str = None,
    titleStyle: dict = None,
    titleClassName: str = None,
    descriptionStyle: dict = None,
    descriptionClassName: str = None,
) -> Component:
    """简单图表卡片

    Args:
        title (Component, optional): 标题元素. Defaults to None.
        description (Component, optional): 标题右侧辅助描述元素. Defaults to None.
        chart (Component, optional): 图表元素. Defaults to None.
        extra (Component, optional): 额外元素. Defaults to None.
        height (Union[int, float, str], optional): 卡片高度. Defaults to 300.
        root_id (Union[str, dict], optional): 根元素id. Defaults to None.
        rootStyle (dict, optional): 根元素样式. Defaults to None.
        rootClassName (str, optional): 根元素类名. Defaults to None.
        titleStyle (dict, optional): 标题样式. Defaults to None.
        titleClassName (str, optional): 标题类名. Defaults to None.
        descriptionStyle (dict, optional): 描述样式. Defaults to None.
        descriptionClassName (str, optional): 描述类名. Defaults to None.

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
                                    className=titleClassName,
                                    style={
                                        **dict(
                                            fontSize=20,
                                        ),
                                        **(titleStyle or {}),
                                    },
                                ),
                                (
                                    description
                                    and fac.AntdText(
                                        description,
                                        type='secondary',
                                        className=descriptionClassName,
                                        style=descriptionStyle,
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
                html.Div(chart, style=style(height='100%', minHeight=0)),
            ],
            vertical=True,
            gap=0,
            style=style(width='100%', height='100%'),
        ),
        className=rootClassName,
        style={
            **dict(
                height=height,
                padding=20,
                background='#fff',
                borderRadius=8,
                boxSizing='border-box',
                boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            ),
            **(rootStyle or {}),
        },
        **(dict(id=root_id) if root_id else {}),
    )


def index_card(
    index_name: _Component = None,
    index_description: _Component = None,
    index_value: _Component = None,
    extra_content: _Component = None,
    footer_content: _Component = None,
    root_id: Union[str, dict] = None,
    rootStyle: dict = None,
    rootClassName: str = None,
    indexNameStyle: dict = None,
    indexNameClassName: str = None,
    extraContentStyle: dict = None,
    extraContentClassName: str = None,
    footerContentStyle: dict = None,
    footerContentClassName: str = None,
) -> Component:
    """指标卡片

    Args:
        index_name (Component, optional): 指标名称. Defaults to None.
        index_description (Component, optional): 指标描述内容. Defaults to None.
        index_value (Component, optional): 指标值元素. Defaults to None.
        extra_content (Component, optional): 额外元素. Defaults to None.
        footer_content (Component, optional): 底部元素. Defaults to None.
        root_id (Union[str, dict], optional): 根元素id. Defaults to None.
        rootStyle (dict, optional): 根元素样式. Defaults to None.
        rootClassName (str, optional): 根元素类名. Defaults to None.
        indexNameStyle (dict, optional): 指标名称样式. Defaults to None.
        indexNameClassName (str, optional): 指标名称类名. Defaults to None.
        extraContentStyle (dict, optional): 额外元素样式. Defaults to None.
        extraContentClassName (str, optional): 额外元素类名. Defaults to None.
        footerContentStyle (dict, optional): 底部元素样式. Defaults to None.
        footerContentClassName (str, optional): 底部元素类名. Defaults to None.

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
                            className=indexNameClassName,
                            style={
                                **dict(
                                    color='rgba(0, 0, 0, 0.65)', fontSize=16
                                ),
                                **(indexNameStyle or {}),
                            },
                        ),
                        fac.AntdText(index_value, style=style(fontSize=28)),
                    ],
                    vertical=True,
                    justify='space-between',
                    style=style(height=64, overflowY='hidden'),
                ),
                html.Div(
                    html.Div(extra_content, style=style(height='100%')),
                    className=extraContentClassName,
                    style={
                        **dict(
                            height=56,
                            marginBottom=12,
                            overflowX='hidden',
                            overflowY='hidden',
                        ),
                        **(extraContentStyle or {}),
                    },
                ),
                fac.AntdDivider(style=style(marginTop=0, marginBottom=0)),
                html.Div(
                    footer_content,
                    className=footerContentClassName,
                    style={
                        **dict(
                            height=22,
                            paddingTop=9,
                            overflowY='hidden',
                        ),
                        **(footerContentStyle or {}),
                    },
                ),
            ],
            size=0,
            direction='vertical',
            style=style(width='100%'),
        ),
        className=rootClassName,
        style={
            **dict(
                padding='20px 20px 8px',
                background='#fff',
                borderRadius=8,
                boxSizing='border-box',
                boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            ),
            **(rootStyle or {}),
        },
        **(dict(id=root_id) if root_id else {}),
    )
