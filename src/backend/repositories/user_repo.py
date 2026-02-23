from db.database import get_connection
from models.user import UserCreate


def read_users():
    con = get_connection()
    return con.execute('''
    slect
        id,
        username
    from
        users
    ''').fetchall()


def read_user(id: int):
    con = get_connection()
    return con.execute('''
    select
        id,
        username
    from
        users
    where
        id = ?
    ''', [id]).fetchone()


def read_user_by_name(username: str):
    con = get_connection()
    return con.execute('''
    select
        id,
        username
    from
        users
    where
        username = ?
    ''', [username]).fetchone()


def read_user_db(username: str):
    con = get_connection()
    return con.execute('''
    select
        id,
        username,
        password_hash,
        role
    from
        users
    where
        username = ?
    ''', [username]).fetchone()


def insert_user(user: UserCreate):
    con = get_connection()
    con.execute('''
    insert into users values (
        nextval('seq_uid'),
        ?,
        ?,
        'user'
    )
    ''', [user.username, user.password])


def update_password(id: int, password_hash: str):
    con = get_connection()
    print(type(password_hash), password_hash)
    con.execute('''
    update
        users
    set
        password_hash = ?
    where
        id = ?
    ''', [password_hash, id])


def update_username(id: int, username: str):
    con = get_connection()
    con.execute('''
    update
        users
    set
        username = ?
    where
        id = ?
    ''', [username, id])


def update_role(id: int, role: str):
    con = get_connection()
    con.execute('''
    update
        users
    set
        role = ?
    where
        id = ?
    ''', [role, id])
