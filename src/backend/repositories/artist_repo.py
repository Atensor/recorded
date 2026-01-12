from db.database import get_connection
from models.artist import ArtistCreate as Artist


def read_artists():
    con = get_connection()
    return con.execute(f"""
    select
        id,
        name
    from
        artists
    """).fetchall()


def read_artist(id: int):
    con = get_connection()
    return con.execute(f"""
    select
        id,
        name
    from
        artists
    where
        id = {id}
    """).fetchone()


def write_artist(artist: Artist):
    con = get_connection()
    con.execute(f"""
    insert into artists values(
        nextval('seq_aid'),
        '{artist.name}'
    )""")
