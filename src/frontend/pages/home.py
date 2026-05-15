from nicegui import ui
import json
from datetime import date
from src.frontend.components.header import header
from src.frontend.components.record_card import record_card_grid
from src.frontend.components.toggle_button import TagToggleButton
from src.frontend.api.record_client import get_records


def page():
    @ui.page("/")
    def home():
        header()
        record_card_grid(get_records())
