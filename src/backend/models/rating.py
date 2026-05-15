from pydantic import BaseModel
from .record import RecordRead as Record
from .track import TrackRead as Track


class RatingBase(BaseModel):
    rating: int


class RecordRatingBase(RatingBase):
    record_id: int


class TrackRatingBase(RatingBase):
    track_id: int
