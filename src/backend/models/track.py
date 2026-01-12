from pydantic import BaseModel
from models.artist import ArtistRead as Artist


class TrackBase(BaseModel):
    title: str
    tracknr: int
    features: list[Artist]


class TrackCreate(TrackBase):
    record_id: int


class TrackRead(TrackBase):
    id: int

    class config:
        from_attributes = True


# Lyrics are in the Track but are not needed for every Track

class LyricBase(BaseModel):
    text: str

    class config:
        from_attributes = True


class TrackWithLyricRead(TrackRead):
    lyric: LyricBase | None
