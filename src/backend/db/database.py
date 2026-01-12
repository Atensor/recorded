import duckdb
from pathlib import Path

DB_PATH = Path(__file__).parent / "data.duckdb"


def get_connection():
    return duckdb.connect(DB_PATH)


def reset_db():
    con = get_connection()

    con.sql('''
    ''')
