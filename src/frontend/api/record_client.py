from api.base_client import get, post


def get_records():
    return get("/records/")


def get_record(id: int):
    return get(f"/records/{id}")


def get_records_min():
    return get(f"/records/min")


def get_artist_records(artist_id: int):
    return get(f"/records/artists/{artist_id}")


def get_label_records(label_id: int):
    return get(f"/records/labels/{label_id}")


def get_genre_records(genre_id: int):
    return get(f"/records/genres/{genre_id}")


def post_record(payload):
    record = post("/records/", payload).json()
