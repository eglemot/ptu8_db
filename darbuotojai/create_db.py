import sqlite3
import os

if not os.path.exists('data'):
    os.mkdir('data')

conn = sqlite3.connect('data/darbuotojai.db')
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS darbuotojai (
            id INTEGER PRIMARY KEY NOT NULL,
            vardas VARCHAR(50) NOT NULL,
            pavarde VARCHAR(100) NOT NULL,
            atlyginimas DECIMAL(10,2)
        )
    """)
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Rokas', 'Molis', 3000.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Egle', 'Motie', 3340.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Airida', 'Juraitis', 3030.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Giedrius', 'Isora', 4450.55);")
    darbuotojai = [
        ("Gediminas", "Zakas", 3423.43),
        ("Ignas", "Rocys", 3533.34),
        ("Kevinas", "Karpus", 3942.43),
    ]
    c.executemany("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES (?, ?, ?)", darbuotojai)