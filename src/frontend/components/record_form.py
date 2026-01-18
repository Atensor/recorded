from nicegui import ui
from state.record_state import RecordFormState
from state.track_state import TrackFormState
from components.track_form import track_form
from api.record_client import post_record
from api.artist_client import get_artists
from api.label_client import get_labels
from api.genre_client import get_genres


def record_form(record: RecordFormState):
    ui.label('Record').classes('text-h4')
    ui.input(label="Title",
             placeholder="enter title",
             on_change=lambda e:
             setattr(record, "title", e.value) or
             update_save_button())
    ui.date_input(label='Date',
                  placeholder="Set release Date",
                  on_change=lambda e:
                  setattr(record, "date", e.value) or
                  update_save_button())
    ui.select(
        {a["id"]: a["name"] for a in get_artists()},
        label="Select Artist",
        on_change=lambda e:
            setattr(record, "artist_id", e.value) or
            update_save_button())
    ui.select(
        {l["id"]: l["name"] for l in get_labels()},
        label="Select Label",
        on_change=lambda e:
            setattr(record, "label_id", e.value) or
            update_save_button())
    ui.select(
        {g["id"]: g["name"] for g in get_genres()},
        multiple=True,
        label="Select Genres",
        on_change=lambda e:
            setattr(record, "genre_ids", e.value) or
            update_save_button())

    ui.number(
        label="Num Tracks",
        value=9,
        min=0,
        on_change=lambda e:
            update_tracks(int(e.value) or
                          update_save_button())
    )

    track_container = ui.column()

    def update_save_button():
        save_button.set_enabled(record.is_valid())

    def update_tracks(n: int):
        if n > len(record.tracks):
            for i in range(len(record.tracks), n):
                record.tracks.append(TrackFormState(i + 1))
        else:
            record.tracks = record.tracks[:n]

        track_container.clear()
        with track_container:
            for track in record.tracks:
                track_form(track, update_save_button)

    update_tracks(9)

    save_button = ui.button(
        "Save",
        on_click=lambda:
        post_record(record.to_payload()) or
        update_save_button()
    )

    update_save_button()
