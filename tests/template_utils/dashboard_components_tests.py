import sys

sys.path.append('../..')
import dash
import random
from dash import html
import feffery_antd_charts as fact
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
from feffery_dash_utils.template_utils.dashboard_components import (
    welcome_card,
    simple_chart_card,
)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdRow(
            [
                fac.AntdCol(
                    welcome_card(
                        title='欢迎用户Feffery，又是元气满满的一天',
                        description=fac.AntdText(
                            [
                                '您有8条未处理的消息，点击',
                                html.A('此处'),
                                '查看。',
                            ],
                            type='secondary',
                        ),
                        extra=fac.AntdDescriptions(
                            items=[
                                {
                                    'label': '项目数',
                                    'children': '12',
                                },
                                {
                                    'label': '待办项',
                                    'children': '5 / 17',
                                },
                                {
                                    'label': '消息',
                                    'children': '8',
                                },
                            ],
                            column=1,
                            size='small',
                            style=style(width=125),
                            labelStyle=style(fontSize=16),
                            contentStyle=style(fontSize=16),
                        ),
                    ),
                    span=24,
                ),
                *(
                    [
                        fac.AntdCol(
                            simple_chart_card(
                                title='标题测试',
                                description='辅助描述信息',
                                chart=fact.AntdColumn(
                                    data=[
                                        {
                                            'date': f'2020-0{i}',
                                            'y': random.randint(50, 100),
                                        }
                                        for i in range(1, 10)
                                    ],
                                    xField='date',
                                    yField='y',
                                    color='#1677ff',
                                ),
                                extra=fac.AntdButton('测试', type='link'),
                            ),
                            span=6,
                        )
                    ]
                    * 8
                ),
            ],
            gutter=[18, 18],
        )
    ],
    style=style(
        padding=50,
        background='#f5f5f5',
        minHeight='100vh',
        boxSizing='border-box',
    ),
)

if __name__ == '__main__':
    app.run(debug=True)
