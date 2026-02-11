from nicegui import ui
from api.cover_art_client import get_cover_art_link


def record_card(record: dict):
    with ui.card().on("click", lambda: ui.navigate.to(f"/record/{record["id"]}")).classes("card"):
        with ui.element("div").style("width: 100%"):
            with ui.row().style("width: 100%"):
                ui.image(get_cover_art_link(record["artist"]["name"], record["title"])).classes(
                    "image").style("width:20%")
                with ui.element("div").style("width: 100%"):
                    record_year = record["date"].split("-")[0]
                    genres = ", ".join(genre["name"]
                                       for genre in record["genres"])
                    ui.restructured_text(
                        f'''**{record["title"]}**
                            - Artist: {record["artist"]["name"]}
                            - Label: {record["label"]["name"]}
                            - Release Year: {record_year}
                            - Genres: {genres} ''').classes("")