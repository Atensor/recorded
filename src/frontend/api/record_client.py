from api.base_client import get, post
from api.track_client import post_track


def get_records():
    return get("/records/")


def get_record(id: int):
    return get(f"/records/{id}")


def post_record(payload):
    record_id = post("/records/", payload)["id"]
    for track in payload["tracks"]:
        track["record_id"] = record_id
        post_track(track)
