from api.base_client import get, post


def get_track(id):
    return get(f"/tracks/{id}")

def get_track_record(id: int):
    return get(f"/records/tracks/{id}")
