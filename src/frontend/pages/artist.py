from nicegui import ui
from components.header import header
from components.record_card import record_card
from api.artist_client import get_artist
from api.record_client import get_artist_records



def page():
    @ui.page("/artist/{id}")
    def artist(id:int):
        header()

        artist = get_artist(id)
        
        ui.label("Records by " + artist["name"]).classes("h-1")
        
        for record in get_artist_records(id):
            record_card(record)
        
