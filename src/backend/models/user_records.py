from pydantic import BaseModel
from enum import StrEnum
from models.user import UserRead as User
from models.record import RecordRead as Record


class state(StrEnum):
    "physical"
    "digital"
    "wanted"
    "favourite"


class User_ReccordRead(BaseModel):
    user_id: int
    record_id: int
    state: state

    class config:
        from_attributes = True
