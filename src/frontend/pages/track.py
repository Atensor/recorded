from nicegui import ui
from datetime import date
from components import header
from api.track_client import get_track, get_track_record
from api.cover_art_client import get_cover_art_link

# TODO: Add Lyrics


def page():
    @ui.page("/track/{id}")
    def track(id):
        header.header()

        track = get_track(id)
        record = get_track_record(id)

        if track is None:
            ui.label("Track not Found").classes("text-2xl")
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
                    f'''**{track["title"]}**

- Artist: <a class="clean-link" href="http://127.0.0.1:8080/artist/{record["label"]["id"]}">
        {record["label"]["name"]}
    </a>

- Label: <a class="clean-link" href="http://127.0.0.1:8080/artist/{record["label"]["id"]}">
        {record["label"]["name"]}
    </a>

- Genres: {genres}

- Year: {record_date.year}''')
            ui.image(get_cover_art_link(
                record["artist"]["name"], record["title"])).classes("image w-128")
