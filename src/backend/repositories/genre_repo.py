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
    """).fetchall()


def read_record_genres(record_id: int):
    con = get_connection()
    return con.execute(f"""
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
        record_genres.record_id = {record_id}
    """).fetchall()


def insert_genre(genre: Genre):
    con = get_connection()
    con.execute(f"""
    insert into genres values(
        nextval('seq_gid'),
        '{genre.name}'
    )""")
