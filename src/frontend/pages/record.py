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

        if record is None:
            ui.label("Record not Found").classes("text-2xl")
            return

        with ui.row().style("width: 80%"):
            with ui.element("div"):
                record_date = date.fromisoformat(record["date"])
                genreList: list[str] = []
                for genre in record["genres"]:
                    genreList.append('<a class="clean-link" href="http://127.0.0.1:8080/genre/' +
                                     str(genre["id"]) + '">' + genre["name"] + '</a>')
                genres = ", ".join(genre
                                   for genre in genreList)
                ui.markdown(
                    f'''**{record["title"]}**

- Artist: <a class="clean-link" href="http://127.0.0.1:8080/artist/{record["artist"]["id"]}">
        {record["artist"]["name"]}
    </a>
                        
- Label: <a class="clean-link" href="http://127.0.0.1:8080/artist/{record["label"]["id"]}">
        {record["label"]["name"]}
    </a>

- Genres: {genres}

- Release Date: {record_date.day}.{record_date.month}.{record_date.year}''')
                ui.markdown("---")
                ui.markdown("**Tracks:**")
                for track in record["tracks"]:
                    features = ", ".join(feature["name"]
                                         for feature in track["features"])
                    mod_duration = track["duration"] % 60
                    with ui.row():
                        with ui.row().classes("w-100"):
                            ui.markdown(
                                f'{track["track_nr"]}. <a class="clean-link" href="http://127.0.0.1:8080/{track["id"]}">{track["title"]}</a>')
                            if len(features) > 0:
                                ui.markdown(f"feat. {features}").style(
                                    "font-size: 12px")
                        ui.markdown(
                            f"{int(track["duration"] / 60)}:{mod_duration if mod_duration >= 10 else f"0{mod_duration}"}")
            ui.image(get_cover_art_link(record["artist"]["name"], record["title"])).classes(
                "image w-128")
