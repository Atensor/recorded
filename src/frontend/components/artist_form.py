from nicegui import ui
from src.frontend.state.artist_state import ArtistFormState
from src.frontend.api.artist_client import post_artist


def artist_form(artist: ArtistFormState):
    ui.label("Artist").classes("text-h4")
    ui.input(
        label="Artist",
        placeholder="Enter Artist Name",
        on_change=lambda e:
            setattr(artist, "name", e.value) or
            update_save_button()
    )

    save_button = ui.button(
        "Save",
        on_click=lambda: post_artist(artist.to_payload())
    )

    def update_save_button():
        save_button.set_enabled(artist.is_valid())

    update_save_button()
