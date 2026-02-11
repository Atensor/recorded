from nicegui import ui
from datetime import date
from components import header
from api.track_client import get_track, get_track_record
from api.cover_art_client import get_cover_art_link

#TODO: Add Lyrics
def page():
    @ui.page("/track/{id}")
    def track(id):
        header.header()

        track = get_track(id)
        record = get_track_record(id)
        
        with ui.row().style("width: 80%"):
            with ui.element("div"):
                record_date = date.fromisoformat(record["date"])
                genres = ", ".join(genre["name"]
                                   for genre in record["genres"])
                ui.restructured_text(
                    f'''**{track["title"]}**
                            - Artist: {record["artist"]["name"]}
                            - Label: {record["label"]["name"]}
                            - Genres: {genres}
                            - Year: {record_date.year}''')
            ui.image(get_cover_art_link(record["artist"]["name"], record["title"])).classes(
                "image").classes("w-128")
