from pydantic import BaseModel
from models.record import RecordRead as Record
from models.track import TrackRead as Track


class RatingBase(BaseModel):
    rating: int


class RecordRatingBase(RatingBase):
    record: Record


class TrackRatingBase(RatingBase):
    track: Track
