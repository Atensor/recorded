from fastapi import APIRouter
from models.label import LabelRead, LabelCreate
from services.label_service import get_labels_service, get_label_service, create_label_service

router = APIRouter(
    prefix="/labels",
    tags=["labels"]
)


@router.get("/")
def labels() -> list[LabelRead]:
    return get_labels_service()


@router.get("/{id}")
def label(id: int) -> LabelRead:
    return get_label_service(id)


@router.post("/")
def post_label(label: LabelCreate):
    create_label_service(label)
