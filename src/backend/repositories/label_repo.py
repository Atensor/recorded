from db.database import get_connection
from models.label import LabelCreate as Label


def read_label(id: int):
    con = get_connection()
    return con.execute(f"""
    select
        id,
        name
    from
        lables
    where
        id = {id}
    """).fetchone()


def write_label(label: Label):
    con = get_connection()
    con.execute(f"""
    insert into labels values(
        nextval('seq_lid'),
        '{label.name}'
    )""")
