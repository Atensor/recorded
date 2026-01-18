from nicegui import ui
from api.artist_client import get_artists
from state.track_state import TrackFormState
from state.record_state import RecordFormState


def track_form(track: TrackFormState, update_save_button):
    ui.label(f"Track {track.tracknr}")
    ui.input(label="title",
             placeholder="enter Track title",
             on_change=lambda e:
             setattr(track, "title", e.value) or
             update_save_button())
    ui.select({g["id"]: g["name"] for g in get_artists()},
              label="Features",
              multiple=True,
              on_change=lambda e:
              setattr(track, "feature_ids", e.value) or
              update_save_button())
