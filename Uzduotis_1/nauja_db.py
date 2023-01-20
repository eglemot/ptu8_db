import sqlite3

conn = sqlite3.connect('data/uzduotis1.db')
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE customer (
            id INTEGER PRIMARY KEY NOT NULL,
            f_name VARCHAR(50) NOT NULL,
            l_name VARCHAR(50) NOT NULL,
            email VARCHAR(50) UNIQUE
        )
    """)