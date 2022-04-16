import sqlite3
import os

db_file = "database.db"
schema_file = "schema.sql"


def check_db(filename):
    return os.path.exists(filename)

    # if check_db(db_file):
    print("Database already exists.")
    exit(0)


conn = sqlite3.connect("database.db")

c = conn.cursor()

with open(schema_file, "r") as rf:
    schema = rf.read()

with sqlite3.connect(db_file) as conn:
    print("Created the connection!")

    conn.executescript(schema)
    print("Created the table.")

    conn.executescript(
        """
                        insert into tokens (numbers)
                        values
                        (100),
                        (200),
                        (300);
                        """
    )
    print("Inserted the values")

print("Connection closed")
