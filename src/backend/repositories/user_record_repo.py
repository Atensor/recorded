from db.database import get_connection
from models.user_records import User_RecordBase


def read_user_records(user_id: int):
    con = get_connection()
    return con.execute('''
    select
        user_id,
        record_id,
        tag
    from
        user_records
    where
        user_id = ?
    ''', [user_id]).fetchall()


def read_user_record_ids(user_id: int):
    con = get_connection()
    return con.execute('''
    select distinct
        record_id
    from
        user_records
    where
        user_id = ?
    and (
        tag = 'physical'
    or
        tag = 'digital')
    ''', [user_id]).fetchall()


def read_record_users(record_id: int):
    con = get_connection()
    return con.execute('''
    select distinct
        user_id
    from
        user_records
    where
        record_id = ?
    and
        (tag = 'physical' 
    or
        tag = 'digital')
    ''', [record_id]).fetchall()


def insert_user_record(user_record: User_RecordBase):
    con = get_connection()
    con.execute('''
    insert into user_records values (
        ?,
        ?,
        ?
    )''', [user_record.record_id, user_record.user_id, user_record.tag])


def delete_user_record(user_record: User_RecordBase):
    con = get_connection()
    con.execute('''
    delete from
        user_records
    where
        user_id = ?
    and
        record_id = ?
    and
        tag = ?
    ''', [user_record.user_id, user_record.record_id, user_record.tag])
