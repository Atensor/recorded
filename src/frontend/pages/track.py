from nicegui import ui
from components import header
from api_client import get_track, get_record


def page():
    @ui.page("/track/{id}")
    def track(id):
        header.header()

        track = get_track(id)
        record = get_record(track["record"])
        with ui.row().style("width: 80%"):
            with ui.element("div"):
                ui.restructured_text(
                    f'''**{track["title"]}**
                            - {record["artist"]}
                            - {record["label"]}
                            - {record["genre"]}
                            - {record["year"]}''')
            ui.image(record["image"]).classes(
                "image").style("height: 544px; width: 544px")
