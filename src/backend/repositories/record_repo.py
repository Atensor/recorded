from db.database import get_connection
from models.record import RecordCreate


def read_record_list():
    con = get_connection()
    return con.execute("""
    select
        id,
        title,
        date,
        artist_id,
        label_id
    from
        records
    order by title
    """).fetchall()


def read_record_list_min():
    con = get_connection()
    return con.execute("""
    select
        id,
        title,
        artist_id
    from
        records
    order by title
    """).fetchall()


def read_record(id: int):
    con = get_connection()
    return con.execute("""
    select
        id,
        title,
        date,
        artist_id,
        label_id
    from
        records
    where
        id = ?
    """, [id]).fetchone()


def read_record_min(id: int):
    con = get_connection()
    return con.execute("""
    select
        id,
        title,
        artist_id
    from
        records
    where
        id = ?
    """, [id]).fetchone()


def read_artist_records(artist_id: int):
    con = get_connection()
    return con.execute("""
    select
        id,
        title,
        date,
        artist_id,
        label_id
    from
        records
    where
        artist_id = ?
    """, [artist_id]).fetchall()


def read_label_records(label_id: int):
    con = get_connection()
    return con.execute("""
    select
        id,
        title,
        date,
        artist_id,
        label_id
    from
        records
    where
        label_id = ?
    """, [label_id]).fetchall()


def read_genre_records(genre_id: int):
    con = get_connection()
    return con.execute("""
    select
        id,
        title,
        date,
        artist_id,
        label_id
    from
        records
    join
        record_genres
    on
        records.id = record_genres.record_id
    where
        record_genres.genre_id = ?
    """, [genre_id]).fetchall()


def insert_record(record: RecordCreate):
    con = get_connection()
    return con.execute("""
    insert into records values (
        nextval('seq_rid'),
        ?,
        ?,
        ?,
        ?,
        NULL
    )
    returning
        id
    """, [
        record.title,
        record.artist_id,
        record.label_id,
        record.date
    ]).fetchone()


def remove_record(id: int):
    con = get_connection()
    con.execute("""
    delete from
        record_genres
    where
        record_id = ?;
    """, [id])
    con.execute('''
    delete from
        user_records
    where
        record_id = ?
    ''', [id])
    con.execute("""
    delete from
        records
    where
        id = ?
    """, [id])
