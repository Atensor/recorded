from pydantic import BaseModel
from models.artist import ArtistRead as Artist
from models.label import LabelRead as Label
from models.genre import GenreRead as Genre
from models.track import TrackRead, TrackCreate
from datetime import date as Date


class RecordBase(BaseModel):
    title: str
    date: Date


class RecordCreate(RecordBase):
    artist_id: int
    label_id: int
    genre_ids: list[int]
    tracks: list[TrackCreate]


class RecordRead(RecordBase):
    id: int
    artist: Artist
    label: Label
    genres: list[Genre]

    class config:
        from_attributes = True


class RecordTracksRead(RecordRead):
    tracks: list[TrackRead]

    class config:
        from_attributes = True
