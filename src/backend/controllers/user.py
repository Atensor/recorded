from fastapi import APIRouter, Depends, HTTPException, status
from models.user import UserRead, UserCreate
from models.user_records import User_RecordBase
from services.auth_service import get_current_user
from services.user_service import get_users_service, get_user_service, get_user_by_name_service, get_record_users_service, create_user_service, change_username_service, change_password_service, change_role_service, is_admin, is_elevated
from services.user_record_service import get_user_records_service, get_user_record_tags_service, add_record_tag_service, delete_record_tag_service


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/")
def users() -> list[UserRead]:
    return get_users_service()


@router.get("/me")
async def user_me(current_user: UserRead = Depends(get_current_user)) -> UserRead:
    return current_user


@router.get("/me/is_elevated")
async def user_me_is_elevated(current_user: UserRead = Depends(get_current_user)) -> bool:
    return is_elevated(current_user.username)


@router.get("/{id}")
def user(id: int) -> UserRead:
    return get_user_service(id)


@router.get("/{username}/exists")
def user_exists(username: str):
    if get_user_by_name_service(username).id == -1:
        return False
    return True


@router.get("/me/records/tags")
async def get_my_records_tags(current_user: UserRead = Depends(get_current_user)) -> list[User_RecordBase]:
    return get_user_records_service(current_user.id)


@router.get("/me/records/{record_id}/tags")
async def get_my_record_tags(current_user: UserRead = Depends(get_current_user), record_id: int = 0) -> list[User_RecordBase]:
    return get_user_record_tags_service(current_user.id, record_id)


@router.get("/records/{record_id}")
def get_record_users(record_id) -> list[UserRead]:
    return get_record_users_service(record_id)


@router.post("/")
def post_user(user: UserCreate):
    return create_user_service(user)


@router.post("/me/records/{record_id}/tags")
async def post_record_tag(record_id: int, current_user: UserRead = Depends(get_current_user), tag: str = ""):
    if tag == "":
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail={
                            "type": "missing", "loc": ["body", "tag"], "msg": "Field Required"})
    return add_record_tag_service(User_RecordBase(**{"record_id": record_id, "user_id": current_user.id, "tag": tag}))


@router.delete("/me/records/{record_id}/tags")
async def delete_record_tag(record_id: int, current_user: UserRead = Depends(get_current_user), tag: str = None):
    if tag is None:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail={
                            "type": "missing", "loc": ["body", "tag"], "msg": "Field Required"})
    return delete_record_tag_service(User_RecordBase(**{"record_id": record_id, "user_id": current_user.id, "tag": tag}))


# TODO: get new Token after name Change, throw exeption for invalid name
@router.put("/me/username")
async def put_username(current_user: UserRead = Depends(get_current_user), username: str = None):
    if username is None:
        return
    return change_username_service(current_user.id, username)


@router.put("/me/password")
async def put_password(current_user: UserRead = Depends(get_current_user), password: str = None):
    if password is None:
        return
    return change_password_service(current_user.id, password)


@router.put("/{user_id}/role")
async def put_role(current_user: UserRead = Depends(get_current_user), user_id: int = 0, role: str = ""):
    if is_admin(current_user.username):
        change_role_service(user_id, role)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            headers={"WWW-Authenticate": "Bearer"})
