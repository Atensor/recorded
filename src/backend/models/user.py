from pydantic import BaseModel
from enum import StrEnum


class Role(StrEnum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    class config:
        from_attributes = True

    def to_payload(row):
        return {
            "id": row[0],
            "username": row[1]
        }


class UserReadAdmin(UserRead):
    role: Role

    def to_payload(row):
        return {
            "id": row[0],
            "username": row[1],
            "role": row[2]
        }


class UserReadDB(UserReadAdmin):
    password_hash: str

    def to_payload(row):
        return {
            "id": row[0],
            "username": row[1],
            "role": row[2],
            "password_hash": row[3]
        }
