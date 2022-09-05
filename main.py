import i18n
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import LayoutBuilder
from src.data.loader import load_transaction_data
from src.data.source import DataSource

LOCALE = 'pt'
DATA_PATH = './data/transactions.csv'


def main() -> None:
    i18n.set('locale', LOCALE)
    i18n.load_path.append('locale')
    data = load_transaction_data(DATA_PATH, locale=LOCALE)
    data = DataSource(data)

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = i18n.t("general.app_title")
    layout_builder = LayoutBuilder(app, data, LOCALE)
    app.layout = layout_builder.create_layout()
    app.run()


if __name__ == "__main__":
    main()
