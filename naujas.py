import sqlite3

conn = sqlite3.connect('data/paskaitos.db')
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS paskaitos (
            id INTEGER PRIMARY KEY NOT NULL,
            pavadinimas VARCHAR(50) NOT NULL,
            destytojas VARCHAR(100) NOT NULL,
            trukme INT(255)
        )
    """)