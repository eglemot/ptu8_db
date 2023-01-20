import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c =  conn.cursor()

with conn:
    # c.execute("UPDATE darbuotojai SET vardas='Sandra', pavarde='Krisiunaite' where id=3;")
    # c.execute("DELETE FROM darbuotojai where id=4")
    c.execute("SELECT * FROM darbuotojai;")
    # darbuotojai = c.fetchall()
    while True:
        darbuotojas = c.fetchone()
        if darbuotojas:
            print(darbuotojas)
        else:
            break


# if darbuotojai:
#     print(darbuotojai)
