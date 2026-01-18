from repositories.record_repo import read_record, insert_record, read_record_list, add_record_genre
from services.artist_service import get_artist
from services.label_service import get_label
from services.genre_service import get_record_genres


def get_records():
    rows = read_record_list()
    return [
        {
            "id": row[0],
            "title": row[1],
            "date": row[2],
            "artist": get_artist(row[3]),
            "label": get_label(row[4]),
            "genres": get_record_genres(row[0])
        } for row in rows
    ]


def get_record(id: int):
    row = read_record(id)
    return {
        "id": row[0],
        "title": row[1],
        "date": row[2],
        "artist": get_artist(row[3]),
        "label": get_label(row[4]),
        "genres": get_record_genres(row[0])
    }


def create_record(record):
    row = insert_record(record)
    for genre_id in record.genre_ids:
        add_record_genre(row[0], genre_id)
    return get_record(row[0])
