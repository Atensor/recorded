from db.database import get_connection
from models.artist import ArtistCreate as Artist


def read_artists():
    con = get_connection()
    return con.execute("""
    select
        id,
        name
    from
        artists
    order by
    name
    """).fetchall()


def read_artist(id: int):
    con = get_connection()
    return con.execute("""
    select
        id,
        name
    from
        artists
    where
        id = ?
    """, [id]).fetchone()


def read_track_features(track_id: int):
    con = get_connection()
    return con.execute("""
    select
        artists.id,
        artists.name
    from
        artists
    join
        track_features
    on
        artists.id = track_features.artist_id
    where
        track_features.track_id = ?
    """, [track_id]).fetchall()


def write_artist(artist: Artist):
    con = get_connection()
    con.execute("""
    insert into artists values(
        nextval('seq_aid'),
        ?
    )""", [artist.name])


def add_track_features(track_id: int, artist_ids: list[int]):
    con = get_connection()
    con.executemany("""
    insert into track_features values (
        ?,
        ?
    )""", [(track_id, artist_id) for artist_id in artist_ids])
