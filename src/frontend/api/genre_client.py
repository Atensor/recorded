from api.base_client import get, post
from state.gnere_state import GenreFormState


def get_genres():
    return get("/genres/")


def get_genre(id: int):
    return get(f"/genres/{id}")


def post_genre(payload):
    return post("/genres/", payload)
