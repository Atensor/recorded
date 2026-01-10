from nicegui import ui
from components import header
from api_client import get_record, get_tracks


def page():
    @ui.page("/record/{id}")
    def record(id: int):
        header.header()

        record = get_record(id)
        tracks = get_tracks(record["id"])

        with ui.row().style("width: 80%"):
            with ui.element("div"):
                ui.restructured_text(
                    f'''**{record["title"]}**
                            - {record["artist"]}
                            - {record["label"]}
                            - {record["genre"]}
                            - {record["year"]}

                            |

                            |

                            Tracks
                            ''')
                for track in tracks:
                    ui.restructured_text(
                        f"{tracks[track]["nr"]}. {tracks[track]["title"]}")
            ui.image(record["image"]).classes(
                "image").style("height: 544px; width: 544px")
