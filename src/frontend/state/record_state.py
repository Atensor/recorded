from state.track_state import TrackFormState
from state.artist_state import ArtistState as Artist


class RecordFormState:
    title: str | None
    date: str | None
    artist_id: int | None
    label_id: int | None
    genre_ids: list[int]
    tracks: list[TrackFormState]

    def __init__(self):
        self.title = None
        self.date = None
        self.artist_id = None
        self.label_id = None
        self.genre_ids = []
        self.tracks = []

    def to_payload(self):
        return {
            "title": self.title,
            "date": self.date,
            "artist_id": self.artist_id,
            "label_id": self.label_id,
            "genre_ids": self.genre_ids,
            "tracks": [
                track.to_payload() for track in self.tracks
            ]
        }

    def is_valid(self) -> bool:
        tracks_valid = True
        for track in self.tracks:
            tracks_valid = tracks_valid and track.is_valid()
        return bool(
            self.title and
            self.date and
            self.artist_id and
            self.label_id and
            self.genre_ids and
            tracks_valid
        )


class RecordMinState:
    id: int | None
    title: str | None
    artist: Artist | None

    def __init__(self):
        self.id = None
        self.title = None
        self.artist = Artist({"id": None, "name": None})

    def to_payload(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist.to_payload()
        }

    def is_valid(self) -> bool:
        return bool(self.id and self.title and self.artist.is_valid())
