from db.database import get_connection
from models.label import LabelCreate as Label


def read_labels():
    con = get_connection()
    return con.execute("""
    select
        id,
        name
    from
        labels
    order by
        name
    """).fetchall()


def read_label(id: int):
    con = get_connection()
    return con.execute("""
    select
        id,
        name
    from
        labels
    where
        id = ?
    """, [id]).fetchone()


def insert_label(label: Label):
    con = get_connection()
    con.execute("""
    insert into labels values(
        nextval('seq_lid'),
        ?
    )""", [label.name])
