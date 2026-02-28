from api.base_client import get, post
from api.auth_client import get_with_auth, post_with_auth, put_with_auth, delete_with_auth
from state.user_sate import UserFormState


def get_users():
    return get("/users/").json()


def get_user_me():
    return get_with_auth("/users/me")


def get_user_me_is_elevated():
    return get_with_auth("/users/me/is_elevated")


def get_user(int: id):
    return get(f"/users/{id}").json()


def get_user_exists(username: str):
    return get(f"/users/{username}/exists").json()


def get_my_records_tags():
    return get_with_auth("/users/me/records/tags")


def get_my_record_tags(record_id: int):
    return get_with_auth(f"/users/me/records/{record_id}/tags")


def post_user(user: UserFormState):
    return post("/users/", user.to_payload())


def post_record_tag(record_id: int, tag: str):
    return post_with_auth(f"/users/me/records/{record_id}/tags", params={"tag": tag})


def put_username(username: str):
    return put_with_auth("/users/me/username", params=username)


def put_password(password: str):
    return put_with_auth("/users/me/password", params=password)


def delete_record_tag(record_id: int, tag: str):
    return delete_with_auth(f"/users/me/records/{record_id}/tags", params={"tag": tag})
