from pydantic import BaseModel
from record import RecordRead as Record
from track import TrackRead as Track


class RatingBase(BaseModel):
    rating: int


class RecordRatingBase(RatingBase):
    record: Record


class TrackRatingBase(RatingBase):
    track: Track
