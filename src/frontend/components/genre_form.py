from nicegui import ui
from state.gnere_state import GenreFormState
from api.genre_client import post_genre


def genre_form(genre: GenreFormState):
    ui.label("Genre").classes("text-h4")

    ui.input(
        label="Genre",
        placeholder="Enter Genre Name",
        on_change=lambda e:
            setattr(genre, "name", e.value) or
            update_save_button()
    )

    save_button = ui.button(
        "Save",
        on_click=lambda: post_genre(genre.to_payload())
    )

    def update_save_button():
        save_button.set_enabled(genre.is_valid())

    update_save_button()
