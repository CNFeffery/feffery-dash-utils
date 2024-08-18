import os
import sys
import dash
from dash import html
from flask import request
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

sys.path.append(os.path.abspath('.'))

from feffery_dash_utils.i18n_utils import Translator

app = dash.Dash(__name__, suppress_callback_exceptions=True)

translator = Translator(
    translations='./tests/i18n_utils/locales.json'
)

app.layout = lambda: html.Div(
    [
        fuc.FefferyCookie(
            id='current-locale',
            cookieKey=translator.cookie_name,
            expires=3600 * 24 * 365,
        ),
        fuc.FefferyReload(id='page-reload'),
        html.Div(id='page-container'),
    ],
    style={'padding': 50},
)


@app.callback(
    Output('page-container', 'children'),
    Input('page-container', 'id'),
)
def render(_):
    current_locale = request.cookies.get(
        translator.cookie_name
    )
    current_locale = current_locale or 'zh-cn'

    return fac.AntdSpace(
        [
            fac.AntdButton(
                (
                    '切换到英语'
                    if current_locale == 'zh-cn'
                    else 'switch to japanese'
                    if current_locale == 'en-us'
                    else '中国語を切り替えます'
                ),
                type='primary',
                clickExecuteJsString="""
window.dash_clientside.set_props(
    'current-locale',
    {
        value: '%s'
    }
)
window.dash_clientside.set_props(
    'page-reload',
    {
        reload: true
    }
)
"""
                % (
                    'en-us'
                    if current_locale == 'zh-cn'
                    else 'jp'
                    if current_locale == 'en-us'
                    else 'zh-cn'
                ),
            ),
            fac.AntdAlert(
                type='info',
                showIcon=True,
                message=translator.t('示例警告消息'),
                description=translator.t('示例警告描述'),
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )


if __name__ == '__main__':
    app.run(debug=True)
