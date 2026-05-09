from nicegui import ui
import json
from datetime import date
from components.header import header
from components.record_card import record_card
from components.toggle_button import TagToggleButton
from api.record_client import get_records


def page():
    @ui.page("/")
    def home():
        header()
        for record in get_records():
            record_card(record)
