from api.base_client import get, post


def get_artists():
    return get("/artists/").json()


def get_artist(id: int):
    return get(f"/artists/{id}").json()


def post_artist(payload):
    return post("/artists/", payload)
