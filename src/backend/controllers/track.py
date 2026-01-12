from fastapi import APIRouter
from models.track import TrackRead, TrackWithLyricRead, TrackCreate
from services.track_service import get_track, create_track

router = APIRouter(
    prefix="/tracks",
    tags=["tracks"]
)


@router.get("/{id}")
def track(id: int) -> TrackRead:
    return get_track(id)


@router.post("/")
def post_track(track: TrackCreate):
    create_track(track)
