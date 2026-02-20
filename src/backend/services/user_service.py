from models.user import UserRead, UserReadDB, UserCreate
from repositories.user_repo import read_users, read_user, read_user_by_name, read_user_db, insert_user, update_username, update_password
from services.hash_service import hash_password


def get_users_service() -> list[UserRead]:
    rows = read_users()
    return [
        UserRead.to_payload(row) for row in rows
    ]


def get_user_service(id: int) -> UserRead:
    row = read_user(id)
    return UserRead.to_payload(row)


def get_user_by_name_service(username: str) -> UserRead:
    row = read_user_by_name(username)
    return UserRead.to_payload(row)


def get_user_db_service(username: str) -> UserReadDB or None:
    row = read_user_db(username)
    try:
        return UserReadDB.to_payload(row)
    except KeyError:
        return None


def create_user_service(user: UserCreate):
    user.password = hash_password(user.password)
    insert_user(user)


def change_username_service(id: int, username: str):
    update_username(id, username)


def change_password_service(id: int, password: str):
    update_password(id, hash_password(password))
