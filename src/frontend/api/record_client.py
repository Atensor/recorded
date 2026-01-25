from api.base_client import get, post


def get_records():
    return get("/records/")


def get_record(id: int):
    return get(f"/records/{id}")


def post_record(payload):
    print(payload)
    record = post("/records/", payload).json()
