from fastapi import APIRouter, UploadFile, File, Form
from json import loads
from fastapi.responses import FileResponse
from models.record import RecordRead, RecordTracksRead, RecordCreate, RecordReadMin
from models.cover_art import CoverArtCreate
from services.record_service import get_record_service, get_records_service, get_records_min_service, insert_record_service, delete_record_service
from services.cover_art_service import add_art, get_cover_art_service


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


@router.post("/")
def post_record(record: RecordCreate):
    insert_record_service(record)


@router.delete("/{id}")
def delete_record(id: int):
    delete_record_service(id)


@router.get("/{record_id}/art")
def get_cover_art(record_id: int) -> FileResponse:
    return get_cover_art_service(record_id)


@router.put("/{record_id}/art")
async def put_cover_art(record_id: int, file: UploadFile = File(...)):
    content = await file.read()
    filename = file.filename
    add_art(record_id, content, filename)
