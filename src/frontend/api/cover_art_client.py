from api.base_client import put_file, BASE_URL


def get_cover_art_link(artist: str, title: str):
    return BASE_URL + f"/cover_art/{artist}/{title}.jpeg"


def put_cover_art(record_id: int, files):
    return put_file(f"/records/{record_id}/art", files)
