from pydantic import BaseModel
from models.rating import TrackRatingBase, RecordRatingBase as TrackRating, RecordRating


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password_hash: str


class UserRead(UserBase):
    id: int

    class config:
        from_attributes = True


class UserTrackRatingRead(UserRead):
    rating: TrackRating


class UserRecordRatingRead(UserRead):
    rating: RecordRating
