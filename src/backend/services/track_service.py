from repositories.track_repo import read_record_tracks, read_track, write_track


def get_record_tracks(record_id: int):
    rows = read_record_tracks(record_id)
    return [
        {
            "id": rows[0],
            "title": rows[1],
            "record_id": rows[2],
            "track_nr": rows[3]
        } for row in rows
    ]


def get_track(id: int):
    row = read_track(id)
    return {
        "id": row[0],
        "title": row[1],
        "record_id": row[2]
    }


def create_track(track):
    write_track(track)
