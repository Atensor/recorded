from fastapi import APIRouter, UploadFile, File
from json import loads
from models.record import RecordRead, RecordTracksRead, RecordCreate, RecordReadMin
from models.cover_art import CoverArtCreate
from services.record_service import get_record_service, get_records_service, get_records_min_service, get_artist_records_service, get_label_records_service, get_genre_records_service, get_track_record_service, insert_record_service, delete_record_service
from services.cover_art_service import add_art_service

router = APIRouter(
    prefix="/records",
    tags=["records"]
)


@router.get("/")
def records() -> list[RecordRead]:
    return get_records_service()


@router.get("/min")
def records_min() -> list[RecordReadMin]:
    return get_records_min_service()


@router.get("/{id}")
def record(id: int) -> RecordTracksRead:
    return get_record_service(id)


@router.get("/artists/{artist_id}")
def artist_records(artist_id: int) -> list[RecordRead]:
    return get_artist_records_service(artist_id)


@router.get("/labels/{label_id}")
def label_records(label_id: int) -> list[RecordRead]:
    return get_label_records_service(label_id)


@router.get("/genres/{genre_id}")
def genre_records(genre_id: int) -> list[RecordRead]:
    return get_genre_records_service(genre_id)


@router.get("/tracks/{track_id}")
def get_track_record(track_id) -> RecordRead:
    return get_track_record_service(track_id)


@router.post("/")
def post_record(record: RecordCreate):
    insert_record_service(record)


@router.delete("/{id}")
def delete_record(id: int):
    delete_record_service(id)


@router.put("/{record_id}/art")
async def put_cover_art(record_id: int, file: UploadFile = File(...)):
    content = await file.read()
    filename = file.filename
    add_art_service(record_id, content, filename)
