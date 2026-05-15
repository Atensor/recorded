from src.frontend.api.base_client import get, post
from src.frontend.state.label_state import LabelFormState


def get_labels():
    return get("/labels/").json()


def get_label(id: int):
    return get(f"/labels/{id}").json()


def post_label(payload):
    return post("/labels/", payload)
