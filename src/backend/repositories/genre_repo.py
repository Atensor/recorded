from db.database import get_connection
from models.genre import GenreCreate as Genre


def read_genres():
    con = get_connection()
    return con.execute("""
    select
        id,
        name
    from
        genres
    order by
        name
    """).fetchall()


def read_record_genres(record_id: int):
    con = get_connection()
    return con.execute("""
    select
        genres.id,
        genres.name
    from
        genres
    join
        record_genres
    on
        genres.id = record_genres.genre_id
    where
        record_genres.record_id = ?
    """, [record_id]).fetchall()


def read_genre(id: int):
    con = get_connection()
    return con.execute("""
    select
        id,
        name
    from
        genres
    where
        id = ?
    """, [id]).fetchone()


def insert_genre(genre: Genre):
    con = get_connection()
    con.execute("""
    insert into genres values(
        nextval('seq_gid'),
        ?
    )""", [genre.name])


def add_record_genres(record_id: int, genre_ids: list[int]):
    con = get_connection()
    return con.executemany("""
    insert into record_genres values (
        ?,
        ?
    )""", [(record_id, genre_id) for genre_id in genre_ids])
