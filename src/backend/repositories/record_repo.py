from db.database import get_connection


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
    order by date desc
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


def insert_record(record):
    con = get_connection()
    return con.execute("""
    insert into records values (
        nextval('seq_rid'),
        ?,
        ?,
        ?,
        ?
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
    con.execute("""
    delete from
        records
    where
        id = ?
    """, [id])
