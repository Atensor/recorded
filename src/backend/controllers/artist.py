from fastapi import APIRouter
from models.artist import ArtistCreate, ArtistRead
from services.artist_service import get_artist, get_artists, create_artist

router = APIRouter(
    prefix="/artists",
    tags=["artists"]
)


@router.get("/")
def artists() -> list[ArtistRead]:
    return get_artists()


@router.get("/{id}")
def artist(id: int) -> ArtistRead:
    return get_artist(id)


@router.post("/")
def post_artist(artist: ArtistCreate):
    create_artist(artist)
