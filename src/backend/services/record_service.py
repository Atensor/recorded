from repositories.record_repo import read_record, write_record, read_record_list
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
        "label": get_label([row[4]]),
        "genres": get_record_genres(row[0])
    }


def create_record(record):
    write_record(record)
