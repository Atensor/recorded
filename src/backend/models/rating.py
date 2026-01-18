from pydantic import BaseModel
from models.record import RecordRead as Record
from models.track import TrackRead as Track


class RatingBase(BaseModel):
    rating: int


class RecordRatingBase(RatingBase):
    record_id: int


class TrackRatingBase(RatingBase):
    track_id: int
