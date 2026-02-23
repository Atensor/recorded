from pydantic import BaseModel
from enum import StrEnum
from models.user import UserRead as User
from models.record import RecordRead as Record


class Tag(StrEnum):
    PHYSICAL = "physical"
    DIGITAL = "digital"
    WANTED = "wanted"
    FAVOURITE = "favourite"


class User_RecordBase(BaseModel):
    user_id: int
    record_id: int
    tag: Tag

    class config:
        from_attributes = True

    def to_payload(row):
        return {
            "user_id": row[0],
            "record_id": row[1],
            "tag": row[2]
        }
