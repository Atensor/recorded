from models.genre import GenreCreate, GenreRead
from repositories.genre_repo import insert_genre, read_record_genres, read_genres, read_genre, add_record_genres


def get_genres_service() -> list[GenreRead]:
    rows = read_genres()
    return [
        GenreRead.to_payload(row) for row in rows
    ]


def get_record_genres_service(record_id: int) -> list[GenreRead]:
    rows = read_record_genres(record_id)
    return [
        GenreRead.to_payload(row) for row in rows
    ]


def get_genre_service(id: int) -> GenreRead:
    row = read_genre(id)
    return GenreRead.to_payload(row)


def add_record_genres_service(record_id: int, genre_ids: list[int]):
    add_record_genres(record_id, genre_ids)


def create_genre_service(genre: GenreCreate):
    insert_genre(genre)
