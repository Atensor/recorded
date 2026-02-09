import json
from nicegui import ui
from components import header, record_form, artist_form, genre_form, label_form, cover_art_form


def page():
    @ui.page("/admin")
    def admin():
        header.header()

        with ui.splitter(value=30).classes('w-full') as splitter:
            with splitter.before:
                with ui.tabs().props('vertical').classes('w-full') as tabs:
                    record = ui.tab('Record')
                    artist = ui.tab('Artist')
                    genre = ui.tab('Genre')
                    label = ui.tab('Label')
                    cover_art = ui.tab('Cover Artwork')
            with splitter.after:
                with ui.tab_panels(tabs, value=record).props('vertical').classes('w-full h-full'):
                    with ui.tab_panel(record):
                        record_state = record_form.RecordFormState()
                        record_form.record_form(record_state)
                    with ui.tab_panel(artist):
                        artist_state = artist_form.ArtistFormState()
                        artist_form.artist_form(artist_state)
                    with ui.tab_panel(genre):
                        genre_state = genre_form.GenreFormState()
                        genre_form.genre_form(genre_state)
                    with ui.tab_panel(label):
                        label_state = label_form.LabelFormState()
                        label_form.label_form(label_state)
                    with ui.tab_panel(cover_art):
                        cover_art_state = cover_art_form.RecordMinState()
                        cover_art_form.cover_art_form(cover_art_state)
