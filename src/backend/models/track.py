from pydantic import BaseModel
from models.artist import ArtistRead as Artist
from services.artist_service import get_track_features_service


class TrackBase(BaseModel):
    title: str
    track_nr: int
    duration: int


class TrackCreate(TrackBase):
    feature_ids: list[int]


class TrackRead(TrackBase):
    id: int
    features: list[Artist]

    class config:
        from_attributes = True

    def to_payload(row) -> TrackRead:
        return {
            "id": row[0],
            "title": row[1],
            "track_nr": row[2],
            "duration": row[3],
            "features": get_track_features_service(row[0])
        }


# Lyrics are in the Track but are not needed for every Track

class LyricBase(BaseModel):
    text: str

    class config:
        from_attributes = True


class TrackWithLyricRead(TrackRead):
    lyric: LyricBase | None
