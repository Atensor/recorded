from nicegui import ui
import json
import base64
from datetime import date
from components.header import header
from api.record_client import get_records
from api.cover_art_client import get_cover_art


def page():
    @ui.page("/")
    def home():
        header()
        ui.link(text="Admin Panel", target=("/admin"))  # TEMP
        for record in get_records():
            record_card(record)


def record_card(record):
    with ui.card().on("click", lambda: ui.navigate.to(f"/record/{record["id"]}")).classes("card"):
        with ui.element("div").style("width: 100%"):
            with ui.row().style("width: 100%"):
                cover = get_cover_art(record["id"])
                base64_bytes = f'data:{cover[0]["Content-Type"]};base64,{base64.b64encode(cover[1]).decode("utf-8")}'
                ui.image(base64_bytes).classes("image").style("width:20%")
                with ui.element("div").style("width: 100%"):
                    record_year = record["date"].split("-")[0]
                    genres = ", ".join(genre["name"]
                                       for genre in record["genres"])
                    ui.restructured_text(
                        f'''**{record["title"]}**
                            - Artist: {record["artist"]["name"]}
                            - Label: {record["label"]["name"]}
                            - Release Year: {record_year}
                            - Genres: {genres} ''')
