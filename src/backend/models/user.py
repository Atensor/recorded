from pydantic import BaseModel


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


class UserReadDB(UserRead):
    password_hash: str

    def to_payload(row):
        return {
            "id": row[0],
            "username": row[1],
            "password_hash": row[2]
        }
