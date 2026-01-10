from pydantic import BaseModel
from artist import ArtistRead as Artist
from label import LabelRead as Label
from genre import GenreRead as Genre
from datetime import date as Date
from track import TrackRead as Track


class RecordBase(BaseModel):
    title: str
    artist: Artist
    label: Label
    genres: list[Genre]
    date: Date
    tracks: list[Track]


class RecordCreate(RecordBase):
    pass


class RecordRead(RecordBase):
    id: int

    class config:
        from_attributes = True
