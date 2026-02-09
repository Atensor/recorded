from api.base_client import get, post


def get_records():
    return get("/records/")


def get_record(id: int):
    return get(f"/records/{id}")


def get_records_min():
    return get(f"/records/min")


def post_record(payload):
    record = post("/records/", payload).json()
