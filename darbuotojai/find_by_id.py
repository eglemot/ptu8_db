import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
    print("Atskyrimas kableliais, nieko kad iseiti")
    paieska = input("iveskite ID: ")
    if paieska == "":
        break
    else:
        ids = paieska.split(',')
        with conn:
            # c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'")
            query = "SELECT * from darbuotojai WHERE rowid IN ("+', '.join(['?' for x in range(len(ids))]) + ")"
            print(query)
            c.execute(query, ids)
            while True:
                darbuotojas = c.fetchone()
                if darbuotojas:
                    print(darbuotojas)
                else:
                    print("daugiau nieko nera")
                    break

# 'OR 1=1 -- paleidziam sita terminale ir nulauziam