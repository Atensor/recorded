from fastapi import APIRouter, Depends
from models.user import UserRead, UserCreate
from services.auth_service import get_current_user
from services.user_service import get_users_service, get_user_service, create_user_service, change_username_service, change_password_service


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


@router.get("/{id}")
def user(id: int) -> UserRead:
    return get_user_service(id)


@router.post("/")
def post_user(user: UserCreate):
    return create_user_service(user)


# TODO: get new Token after name Change, throw exeption for invalid name
@router.put("/username")
async def put_username(current_user: UserRead = Depends(get_current_user), username: str = None):
    if username is None:
        return
    return change_username_service(current_user["id"], username)


@router.put("/{id}/password")
async def put_password(current_user: UserRead = Depends(get_current_user), password: str = None):
    if password is None:
        return
    return change_password_service(current_user["id"], password)
