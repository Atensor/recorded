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
    return con.execute(f"""
    select
        id, 
        title, 
        date, 
        artist_id, 
        label_id
    from 
        records
    where
        id = {id}
    """).fetchone()


def insert_record(record):
    con = get_connection()
    return con.execute(f"""
    insert into records values (
        nextval('seq_rid'), 
        '{record.title}', 
        {record.artist_id}, 
        {record.label_id}, 
        '{record.date}'
    )
    returning
        id
    """).fetchone()


def add_record_genre(record_id: int, genre_id: int):
    con = get_connection()
    return con.execute(f"""
    insert into record_genres values (
        {record_id},
        {genre_id}
    )""")
