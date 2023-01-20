import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
    print("Iveskite nieko, akad iseiti")
    paieska = input("Ko ieskom?: ")
    if paieska == "":
        break
    else:
        paieska = f"%{paieska}%"
        with conn:
            # c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'")
            c.execute("SELECT * from darbuotojai WHERE pavarde LIKE ? OR vardas LIKE ?", (paieska, paieska))
            while True:
                darbuotojas = c.fetchone()
                if darbuotojas:
                    print(darbuotojas)
                else:
                    print("daugiau nieko nera")
                    break

# 'OR 1=1 -- paleidziam sita terminale ir nulauziam
