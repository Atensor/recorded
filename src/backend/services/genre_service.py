from repositories.genre_repo import write_genre, read_record_genres


def get_record_genres(record_id: int):
    rows = read_record_genres(record_id)
    return [
        {
            "id": row[0],
            "name": row[1]
        } for row in rows
    ]


def create_genre(genre):
    write_genre(genre)
