from nicegui import ui
from api.cover_art_client import get_cover_art_link
from api.user_client import get_my_record_tags
from pages import TAG_STRINGS, ACTIVE_TAG_ICONS, DISABLED_TAG_ICONS, get_tag_states


def record_card(record: dict):

    with ui.card().on("click", lambda: ui.navigate.to(f"/record/{record["id"]}")):
        with ui.element("div").style("width: 100%"):
            with ui.row(wrap=False).style("width: 100%"):
                ui.image(get_cover_art_link(record["artist"]["name"], record["title"])).classes(
                    "image").style("width:35%")
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
                with ui.element("div"):
                    tags = get_my_record_tags(record["id"])
                    if tags.status_code == 200:
                        tag_states: list[bool] = get_tag_states(tags)
                        with ui.column(wrap=False, align_items="center"):
                            for i in range(len(TAG_STRINGS)):
                                create_tag_icon(
                                    ACTIVE_TAG_ICONS[i] if tag_states[i] else DISABLED_TAG_ICONS[i], TAG_STRINGS[i].capitalize())


def create_tag_icon(icon_name: str, tooltip: str):
    with ui.icon(icon_name, color="primary") as icon:
        icon.classes("text-5xl")
        ui.tooltip(tooltip).classes("text-xl")
