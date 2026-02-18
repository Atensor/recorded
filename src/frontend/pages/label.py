from nicegui import ui
from components.header import header
from components.record_card import record_card
from api.label_client import get_label
from api.record_client import get_label_records


def page():
    @ui.page("/label/{id}")
    def label(id: int):
        header()

        label = get_label(id)

        if label is None:
            ui.label("Label not Found").classes("text-2xl")
            return

        ui.label("Records by " + label["name"]).classes("h-1")

        for record in get_label_records(id):
            record_card(record)
