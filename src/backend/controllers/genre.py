from fastapi import APIRouter
from models.genre import GenreRead, GenreCreate
from services.genre_service import get_genres_service, get_record_genres_service, get_genre_service, create_genre_service

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)


@router.get("/")
def genres() -> list[GenreRead]:
    return get_genres_service()


@router.get("/{id}")
def genre(id) -> GenreRead:
    return get_genre_service(id)


@router.get("/{record_id}")
def record_genres(record_id: int) -> list[GenreRead]:
    return get_record_genres_service(record_id)


@router.post("/")
def post_genre(genre: GenreCreate):
    create_genre_service(genre)
