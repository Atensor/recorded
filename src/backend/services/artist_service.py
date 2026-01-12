from repositories.artist_repo import write_artist, read_artist, read_artists


def get_artists():
    rows = read_artists()
    return [
        {
            "id": row[0],
            "name": row[1]
        } for row in rows
    ]


def get_artist(id: int):
    row = read_artist(id)
    return {
        "id": row[0],
        "name": row[1]
    }


def create_artist(artist):
    write_artist(artist)
