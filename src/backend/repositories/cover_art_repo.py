from db.database import get_connection


def read_art_path(record_id: int):
    con = get_connection()
    return con.execute("""
    select
        art_path
    from
        records
    where
        id = ?
    """, [record_id]).fetchone()


def add_art_path(record_id: int, path: str):
    con = get_connection()
    con.execute("""
    update
        records
    set
        art_path = ?
    where
        id = ?
    """, [path, record_id])
