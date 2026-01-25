from fastapi import APIRouter
from models.track import TrackRead, TrackWithLyricRead, TrackCreate
from services.track_service import get_track_service, get_record_tracks_service

router = APIRouter(
    prefix="/tracks",
    tags=["tracks"]
)


@router.get("/record/{id}")
def get_record_tracks(id: int) -> list[TrackRead]:
    return get_record_tracks_service(id)


@router.get("/{id}")
def track(id: int) -> TrackRead:
    return get_track_service(id)
