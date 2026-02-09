from models.artist import ArtistCreate, ArtistRead
from repositories.artist_repo import write_artist, read_artist, read_artists, read_track_features,  add_track_features


def get_artists_service() -> list[ArtistRead]:
    rows = read_artists()
    return [
        {
            "id": row[0],
            "name": row[1]
        } for row in rows
    ]


def get_artist_service(id: int) -> ArtistRead:
    row = read_artist(id)
    return {
        "id": row[0],
        "name": row[1]
    }


def get_track_features_service(track_id: int) -> list[ArtistRead]:
    rows = read_track_features(track_id)
    return [
        {
            "id": row[0],
            "name": row[1]
        } for row in rows
    ]


def create_artist_service(artist: ArtistCreate):
    write_artist(artist)


def add_track_features_service(track_id: int, artist_ids: list[int]):
    add_track_features(track_id, artist_ids)
