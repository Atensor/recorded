from nicegui import ui
from datetime import date
from components import header
from api.record_client import get_record
from api.cover_art_client import get_cover_art_link


def page():
    @ui.page("/record/{id}")
    def record(id: int):
        header.header()

        record = get_record(id)
        with ui.row().style("width: 80%"):
            with ui.element("div"):
                record_date = date.fromisoformat(record["date"])
                genres = ", ".join(genre["name"]
                                   for genre in record["genres"])
                ui.restructured_text(
                    f'''**{record["title"]}**
                            - `Artist: {record["artist"]["name"]} <http://127.0.0.1:8080/artist/{record["artist"]["id"]}>`__
                            - Label: {record["label"]["name"]}
                            - Genres: {genres}
                            - Release Date: {record_date.day}.{record_date.month}.{record_date.year}

                            |

                            |

                            Tracks
                    ''').classes("no-underline text-white")
                for track in record["tracks"]:
                    features = ", ".join(feature["name"]
                                         for feature in track["features"])
                    mod_duration = track["duration"] % 60
                    with ui.row():
                        with ui.row().classes("w-100"):
                            ui.restructured_text(
                                f"{track["track_nr"]}. {track["title"]}")
                            if len(features) > 0:
                                ui.restructured_text(f"feat. {features}").style(
                                    "font-size: 12px")
                        ui.restructured_text(
                            f"{int(track["duration"] / 60)}:{mod_duration if mod_duration >= 10 else f"0{mod_duration}"}")
            ui.image(get_cover_art_link(record["artist"]["name"], record["title"])).classes(
                "image").classes("w-128")
