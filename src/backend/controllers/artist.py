from fastapi import APIRouter
from models.artist import ArtistCreate, ArtistRead
from services.artist_service import get_artist_service, get_artists_service, create_artist_service

router = APIRouter(
    prefix="/artists",
    tags=["artists"]
)


@router.get("/")
def artists() -> list[ArtistRead]:
    return get_artists_service()


@router.get("/{id}")
def artist(id: int) -> ArtistRead:
    return get_artist_service(id)


@router.post("/")
def post_artist(artist: ArtistCreate):
    create_artist_service(artist)
