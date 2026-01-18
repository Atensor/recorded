from nicegui import ui
import json
from components.header import header
from api_client import get_records


def page():
    @ui.page("/")
    def home():
        header()
        ui.link(text="Admin Panel", target=("/admin"))
        for record in get_records():
            record_card(record)


def record_card(record: json):
    with ui.card().on("click", lambda: ui.navigate.to(f"/record/{record["id"]}")).classes("card"):
        with ui.element("div").style("width: 100%"):
            with ui.row().style("width: 100%"):
                ui.image(
                    record["image"]).classes("image").style("width:20%")
                ui.restructured_text(
                    f'''**{record["title"]}**
                        - {record["artist"]}
                        - {record["label"]}
                        - {record["genre"]}
                        - {record["year"]}''')
