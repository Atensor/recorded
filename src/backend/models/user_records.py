from pydantic import BaseModel
from enum import StrEnum
from user import UserRead as User
from record import RecordRead as Record


class state(StrEnum):
    "physical"
    "digital"
    "wanted"
    "favourite"


class User_ReccordRead(BaseModel):
    user: User
    record: Record
    state: state

    class config:
        from_attributes = True
