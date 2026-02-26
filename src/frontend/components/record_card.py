from nicegui import ui
from api.cover_art_client import get_cover_art_link
from api.user_client import post_record_tag


def record_card(record: dict):

    with ui.card().on("click", lambda: ui.navigate.to(f"/record/{record["id"]}")):
        with ui.element("div").style("width: 100%"):
            with ui.row().style("width: 100%"):
                ui.image(get_cover_art_link(record["artist"]["name"], record["title"])).classes(
                    "image").style("width:20%")
                with ui.element("div").style("width: 100%"):
                    record_year = record["date"].split("-")[0]
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

- Release Year: {record_year}
                    ''').classes("")
