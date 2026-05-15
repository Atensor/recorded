from src.backend.db.database import get_connection
from src.backend.models.list_data import ListDataFull


def read_users_list_data(user_id: int):
    con = get_connection()
    return con.execute('''
    select
        id,
        title,
        user_id
    from
        lists
    where
        user_id = ?
    ''', [user_id]).fetchall()


def read_list_data(id: int):
    con = get_connection()
    return con.execute('''
    select
        id,
        title,
        description,
        user_id,
        last_updated
    from
        lists
    where
        id = ?
    ''', [id]).fetchone()


def insert_list_data(list_data: ListDataFull):
    con = get_connection()
    con.execute('''
    insert into lists values (
        nextval('seq_lsid'),
        ?,
        ?,
        ?,
        ?,
    )''', [list_data.title, list_data.description, list_data.last_updated, list_data.user_id])


def add_list_record(list_id: int, record_id: int):
    con = get_connection()
    con.execute('''
    insert into list_records values (
        ?,
        ?
    )''', [list_id, record_id])


def remove_list(id: int):
    con = get_connection()
    con.execute('''
    delete from
        list_records
    where
        list_id = ?;
    ''', [id])
    con.execute('''
    delete from
        lists
    where
        id = ?;
    ''', [id])
