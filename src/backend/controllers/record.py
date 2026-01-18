from fastapi import APIRouter
from models.record import RecordRead, RecordTracksRead, RecordCreate
from services.record_service import get_record, get_records, create_record

router = APIRouter(
    prefix="/records",
    tags=["records"]
)


@router.get("/")
def records() -> list[RecordRead]:
    return get_records()


@router.get("/{id}")
def record(id: int) -> RecordTracksRead:
    return get_record(id)


@router.post("/")
def post_record(record: RecordCreate):
    return create_record(record)
