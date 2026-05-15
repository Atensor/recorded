from nicegui import ui
from datetime import date
from src.frontend.components import header, toggle_button
from src.frontend.api.record_client import get_record
from src.frontend.api.cover_art_client import get_cover_art_link
from src.frontend.api.user_client import get_my_record_tags, post_record_tag, delete_record_tag
from src.frontend.pages import TAG_STRINGS, ACTIVE_TAG_ICONS, DISABLED_TAG_ICONS, get_tag_states


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
                with ui.row(align_items="stretch"):
                    ui.markdown("**Tracks:**").classes("w-100")
                    total_duration = total_runtime(record["tracks"])
                    mod_duration = total_duration % 60
                    ui.markdown(
                        f"{int(total_duration / 60)}:{mod_duration}")
                ui.separator()
                for track in record["tracks"]:
                    features = ", ".join(feature["name"]
                                         for feature in track["features"])
                    mod_duration = track["duration"] % 60
                    with ui.row():
                        with ui.row().classes("w-100"):
                            ui.markdown(
                                f'{track["track_nr"]}. <a class="clean-link" href="http://127.0.0.1:8080/track/{track["id"]}">{track["title"]}</a>')
                            if len(features) > 0:
                                ui.markdown(f"feat. {features}").style(
                                    "font-size: 12px")
                        ui.markdown(
                            f"{int(track["duration"] / 60)}:{mod_duration if mod_duration >= 10 else f"0{mod_duration}"}")
            ui.image(get_cover_art_link(record["artist"]["name"], record["title"])).classes(
                "image w-128")
        tags = get_my_record_tags(id)
        if tags.status_code == 401:
            ui.markdown("*Sign in to Rate and Tag Records*")
        else:
            with ui.button_group().props("rounded") as button_group:
                if tags.status_code == 200:
                    tag_states: list[bool] = get_tag_states(tags)
                    for i in range(len(TAG_STRINGS)):
                        toggle_button.TagToggleButton(
                            record_id=id, tag_index=i, state=tag_states[i], icon=ACTIVE_TAG_ICONS[i] if tag_states[i] else DISABLED_TAG_ICONS[i])
                elif tags.status_code == 401:
                    button_group.props()


def total_runtime(tracks: dict) -> int:
    sum: int = 0
    for track in tracks:
        sum += track["duration"]
    return sum
