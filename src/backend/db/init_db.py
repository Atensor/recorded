from pathlib import Path
from database import get_connection
import os
if os.path.exists("data.duckdb"):
    os.remove("data.duckdb")

SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def init_db():
    con = get_connection()
    with open(SCHEMA_PATH, "r") as f:
        con.execute(f.read())

    con.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
