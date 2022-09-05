from dash import Dash, html

from ..data.source import DataSource
from . import (bar_chart, category_dropdown, locale_dropdown, month_dropdown,
               pie_chart, year_dropdown)


class LayoutBuilder():
    def __init__(self, app: Dash, source: DataSource, locale: str) -> None:
        self.app = app
        self.source = source
        self.locale = locale

    def create_layout(self) -> html.Div:
        return html.Div(
            className='app-div',
            children=[
                html.Div(
                    className='dropdown-container',
                    children=[
                        html.H1(self.app.title),
                        locale_dropdown.render(self.app, self.locale)
                    ]
                ),
                html.Hr(),
                html.Div(
                    className='dropdown-container',
                    children=[
                        year_dropdown.render(self.app, self.source),
                        month_dropdown.render(self.app, self.source),
                        category_dropdown.render(self.app, self.source),
                    ],
                ),
                bar_chart.render(self.app, self.source),
                pie_chart.render(self.app, self.source),
            ],
        )
