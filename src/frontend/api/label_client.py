from api.base_client import get, post
from state.label_state import LabelFormState


def get_labels():
    return get("/labels/")


def get_label(id: int):
    return get(f"/labels/{id}")


def post_label(payload):
    return post("/labels/", payload)
