from api.base_client import get, post
from api.auth_client import get_with_auth, put_with_auth
from state.user_sate import UserFormState


def get_users():
    return get("/users/").json()


def get_user_me():
    return get_with_auth("/users/me/")


def get_user(int: id):
    return get(f"/users/{id}").json()


def get_user_exists(username: str):
    return get(f"/users/{username}/exists").json()


def post_user(user: UserFormState):
    return post("/users/", user.to_payload())


def put_username(username: str):
    return put_with_auth("users/me/username", username)


def put_password(password: str):
    return put_with_auth("users/me/password", password)
