from fastapi import APIRouter
from models.genre import GenreRead, GenreCreate
from services.genre_service import get_genres, get_record_genres, create_genre

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)


@router.get("/")
def genres():
    return get_genres()


@router.get("/record_{id}")
def record_genres(record_id: int) -> list[GenreRead]:
    return get_record_genres(record_id)


@router.post("/")
def post_genre(genre: GenreCreate):
    create_genre(genre)
