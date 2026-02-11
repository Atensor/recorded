from pydantic import BaseModel
from models.artist import ArtistRead as Artist
from models.label import LabelRead as Label
from models.genre import GenreRead as Genre
from models.track import TrackRead, TrackCreate
from services.artist_service import get_artist_service
from services.label_service import get_label_service
from services.genre_service import get_record_genres_service, add_record_genres_service
from services.track_service import get_record_tracks_service
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

    def to_payload(row) -> RecordRead:
        return {
            "id": row[0],
            "title": row[1],
            "date": row[2],
            "artist": get_artist_service(row[3]),
            "label": get_label_service(row[4]),
            "genres": get_record_genres_service(row[0])
        }


class RecordTracksRead(RecordRead):
    tracks: list[TrackRead]

    class config:
        from_attributes = True

    def to_payload(row):
        record = RecordRead.to_payload(row)
        record["tracks"] = get_record_tracks_service(record["id"])
        return record


class RecordReadMin(BaseModel):
    id: int
    title: str
    artist: Artist

    def to_payload(row) -> RecordReadMin:
        return {
            "id": row[0],
            "title": row[1],
            "artist": get_artist_service(row[2])
        }
