from fastapi import APIRouter
from models.record import RecordRead, RecordTracksRead, RecordCreate
from services.record_service import get_record_service, get_records_service, insert_record_service, delete_record_service

router = APIRouter(
    prefix="/records",
    tags=["records"]
)


@router.get("/")
def records() -> list[RecordRead]:
    return get_records_service()


@router.get("/{id}")
def record(id: int) -> RecordTracksRead:
    return get_record_service(id)


@router.post("/")
def post_record(record: RecordCreate):
    insert_record_service(record)


@router.delete("/{id}")
def delete_record(id: int):
    delete_record_service(id)
