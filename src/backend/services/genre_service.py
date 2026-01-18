from repositories.genre_repo import insert_genre, read_record_genres, read_genres


def get_genres():
    rows = read_genres()
    return [
        {
            "id": row[0],
            "name": row[1]
        } for row in rows
    ]


def get_record_genres(record_id: int):
    rows = read_record_genres(record_id)
    return [
        {
            "id": row[0],
            "name": row[1]
        } for row in rows
    ]


def create_genre(genre):
    insert_genre(genre)
