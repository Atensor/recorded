from models.record import RecordCreate, RecordRead, RecordTracksRead, RecordReadMin
from repositories.record_repo import read_record, insert_record, read_record_list, read_record_min, read_record_list_min, remove_record
from services.artist_service import get_artist_service
from services.label_service import get_label_service
from services.genre_service import get_record_genres_service, add_record_genres_service
from services.track_service import get_record_tracks_service, delete_record_tracks_service, create_record_tracks_service


def get_records_service() -> list[RecordRead]:
    rows = read_record_list()
    return [
        {
            "id": row[0],
            "title": row[1],
            "date": row[2],
            "artist": get_artist_service(row[3]),
            "label": get_label_service(row[4]),
            "genres": get_record_genres_service(row[0])
        } for row in rows
    ]


def get_records_min_service() -> list[RecordReadMin]:
    rows = read_record_list_min()
    return [
        {
            "id": row[0],
            "title": row[1],
            "artist": get_artist_service(row[2])
        } for row in rows
    ]


def get_record_service(id: int) -> RecordTracksRead:
    row = read_record(id)
    return {
        "id": row[0],
        "title": row[1],
        "date": row[2],
        "artist": get_artist_service(row[3]),
        "label": get_label_service(row[4]),
        "genres": get_record_genres_service(row[0]),
        "tracks": get_record_tracks_service(row[0])
    }


def get_record_min_service(id: int) -> RecordReadMin:
    row = read_record_min(id)
    return {
        "id": row[0],
        "title": row[1],
        "artist": get_artist_service(row[2])
    }


def insert_record_service(record: RecordCreate):
    row = insert_record(record)
    add_record_genres_service(row[0], record.genre_ids)
    create_record_tracks_service(record.tracks, row[0])


def delete_record_service(id: int):
    delete_record_tracks_service(id)
    remove_record(id)
