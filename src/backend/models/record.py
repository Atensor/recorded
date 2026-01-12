from pydantic import BaseModel
from models.artist import ArtistRead as Artist
from models.label import LabelRead as Label
from models.genre import GenreRead as Genre
from models.track import TrackRead as Track
from datetime import date as Date


class RecordBase(BaseModel):
    title: str
    date: Date
    artist: Artist
    label: Label
    genres: list[Genre]


class RecordTracksBase(RecordBase):
    tracks: list[Track]


class RecordCreate(RecordTracksBase):
    pass


class RecordTracksRead(RecordTracksBase):
    id: int

    class config:
        from_attributes = True


class RecordRead(RecordBase):
    id: int

    class config:
        from_attributes = True
