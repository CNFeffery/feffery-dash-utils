import sys

sys.path.append('../..')
import dash
import random
from dash import html
import feffery_antd_charts as fact
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
from feffery_dash_utils.template_utils.dashboard_components import (
    simple_chart_card,
)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdRow(
            [
                fac.AntdCol(
                    simple_chart_card(
                        title='标题测试',
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
                            height=180,
                        ),
                        extra=fac.AntdButton('测试', type='link'),
                    ),
                    span=6,
                )
            ]
            * 12,
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
