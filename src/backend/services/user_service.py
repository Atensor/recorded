from models.user import UserRead, UserReadDB, UserCreate
from repositories.user_repo import read_users, read_user, read_user_by_name, read_user_db, insert_user, update_username, update_password, update_role
from services.hash_service import hash_password
from services.user_record_service import get_record_user_ids_service, add_record_tag_service, delete_record_tag_service


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
    if row is None:
        return UserRead(id=-1, username="")
    return UserRead(**UserRead.to_payload(row))


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


def change_role_service(id: int, role: str):
    update_role(id, role)


def get_record_users_service(record_id: int) -> list[UserRead]:
    user_ids = get_record_user_ids_service(record_id)
    print(user_ids)
    return [
        get_user_service(id[0]) for id in user_ids
    ]


def is_admin(username: str) -> bool:
    user = UserReadDB(**get_user_db_service(username))
    return user.role == "admin" or user.username == "Admin"


def is_elevated(username: str) -> bool:
    user = UserReadDB(**get_user_db_service(username))
    return not user.role == "user"
