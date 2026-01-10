import duckdb


def get_connection():
    return duckdb.connect("data.duckdb")


def reset_db():
    con = get_connection()

    con.sql('''
    ''')
