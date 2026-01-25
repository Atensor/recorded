from nicegui import ui
from api.artist_client import get_artists
from state.track_state import TrackFormState
from state.record_state import RecordFormState


def track_form(track: TrackFormState, update_save_button, artists: dict):
    ui.label(f"Track {track.track_nr}")
    with ui.row():
        ui.input(label="title",
                 placeholder="enter Track title",
                 on_change=lambda e:
                 setattr(track, "title", e.value) or
                 update_save_button())
        ui.select({a["id"]: a["name"] for a in artists},
                  label="Features",
                  multiple=True,
                  on_change=lambda e:
                  setattr(track, "feature_ids", e.value) or
                  update_save_button())
    with ui.row():
        minutes = ui.number(label="Minutes",
                            min=0,
                            value=0,
                            on_change=lambda e:
                                setattr(track, "minutes", int(e.value or 0)) or
                                update_save_button())
        seconds = ui.number(label="Seconds",
                            min=0,
                            max=59,
                            value=0,
                            on_change=lambda e:
                                setattr(track, "seconds", int(e.value or 0)) or
                                update_save_button())
