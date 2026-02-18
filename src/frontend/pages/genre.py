from nicegui import ui
from components.header import header
from components.record_card import record_card
from api.genre_client import get_genre
from api.record_client import get_genre_records


def page():
    @ui.page("/genre/{id}")
    def genre(id: int):
        header()

        genre = get_genre(id)

        if genre is None:
            ui.genre("Genre not Found").classes("text-2xl")
            return

        ui.label("Records in " + genre["name"]).classes("h-1")

        for record in get_genre_records(id):
            record_card(record)
