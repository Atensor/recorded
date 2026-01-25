from api.base_client import get, post


def get_track(id):
    return get(f"/tracks/{id}")
