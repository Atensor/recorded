from db.database import get_connection


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
