import sqlite3

db_file = 'database.db'

with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   select * from tokens
                   """)
    for row in cursor.fetchall():
        numbers = row
        print(f'{numbers}')