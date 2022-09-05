import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids


def render(app: Dash, locale: str) -> html.Div:
    data = ['en', 'pt']

    @app.callback(
        Output(ids.LOCALE_DROPDOWN, 'value'),
        Input(ids.LOCALE_DROPDOWN, 'value'),
    )
    def set_locale(value: str) -> list[str]:
        i18n.set('locale', value)

        return value

    return html.Div(
        id=f'div-{ids.LOCALE_DROPDOWN}',
        children=[
            html.H6(i18n.t('general.locale')),
            dcc.Dropdown(
                id=ids.LOCALE_DROPDOWN,
                options=data,
                value=locale,
                multi=False,
                clearable=False,
                persistence=True,
            ),
        ]
    )
