from api.base_client import get, put_file


def get_cover_art(record_id: int):
    return get(f"/records/{record_id}/art")


def put_cover_art(record_id: int, files):
    return put_file(f"/records/{record_id}/art", files)
