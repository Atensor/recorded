from models.record import RecordCreate, RecordRead, RecordTracksRead, RecordReadMin
from repositories.record_repo import read_record, insert_record, read_record_list, read_record_min, read_record_list_min, read_artist_records, remove_record
from services.track_service import get_track_record_id_service, delete_record_tracks_service, create_record_tracks_service


def get_records_service() -> list[RecordRead]:
    rows = read_record_list()
    return [
        RecordRead.to_payload(row) for row in rows
    ]


def get_records_min_service() -> list[RecordReadMin]:
    rows = read_record_list_min()
    return [
        RecordReadMin.to_payload(row) for row in rows
    ]


def get_record_service(id: int) -> RecordTracksRead:
    row = read_record(id)
    return RecordTracksRead.to_payload(row)


def get_record_min_service(id: int) -> RecordReadMin:
    row = read_record_min(id)
    return RecordReadMin.to_payload(row)


def get_artist_records_service(artist_id: int) -> list[RecordRead]:
    rows = read_artist_records(artist_id)
    return [
        RecordRead.to_payload(row) for row in rows
    ]


def get_track_record_service(track_id: int) -> RecordRead:
    record_id = get_track_record_id_service(track_id)
    return get_record_service(record_id)

def insert_record_service(record: RecordCreate):
    row = insert_record(record)
    add_record_genres_service(row[0], record.genre_ids)
    create_record_tracks_service(record.tracks, row[0])


def delete_record_service(id: int):
    delete_record_tracks_service(id)
    remove_record(id)
