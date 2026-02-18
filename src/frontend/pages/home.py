from nicegui import ui
import json
from datetime import date
from components.header import header
from components.record_card import record_card
from api.record_client import get_records


def page():
    @ui.page("/")
    def home():
        header()
        ui.link(text="Admin Panel", target=("/admin")
                ).classes("clean-link")  # TEMP
        for record in get_records():
            record_card(record)
