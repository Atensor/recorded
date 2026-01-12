from fastapi import APIRouter
from models.label import LabelRead, LabelCreate
from services.label_service import get_label, create_label

router = APIRouter(
    prefix="/labels",
    tags=["labels"]
)


@router.get("/{id}")
def label(id: int) -> LabelRead:
    return get_label(id)


@router.post("/")
def post_label(label: LabelCreate):
    create_label(label)
