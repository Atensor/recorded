from pydantic import BaseModel
from models.artist import ArtistRead as Artist
from models.label import LabelRead as Label
from models.genre import GenreRead as Genre
from models.track import TrackRead as Track
from datetime import date as Date


class RecordBase(BaseModel):
    title: str
    date: Date
    artist_id: int
    label_id: int
    genre_ids: list[int]


class RecordTracksBase(RecordBase):
    track_ids: list[int]


class RecordCreate(RecordBase):
    pass


class RecordTracksRead(RecordTracksBase):
    id: int

    class config:
        from_attributes = True


class RecordRead(RecordBase):
    id: int

    class config:
        from_attributes = True
