from sqlalchemy.orm import sessionmaker
from pagrindinis import Asmuo, Bankas, Saskaita, engine

session = sessionmaker(bind=engine)()

def meniu():
    print("===[ ATIDARYK SASKAITA ]===")
    print("1 Ivesti asmeni:")
    print("2 Ivesti banka")
    print("3 Ivesti saskaita")
    print("4 Valdyti saskaitos balansa")
    print("5 Perziureti savo saskaitas ir ju informacija")
    print("6 Perziureti viska")
    print("0 Iseiti is programos")
    choice = input("Pasirinkite: ")
    return choice

def ivesti_asmeni():
    ivesti_a = Asmuo(vardas=input("Iveskite varda: "), pavarde=input("Iveskite pavarde: "), asmens_kodas=int(input("Iveskite asmens koda: ")), tel_numeris=int(input("Iveskite tel.nr: ")))
    session.add(ivesti_a)
    session.commit()

def ivesti_banka():
    ivesti_b = Bankas(pavadinimas=input("Iveskite pavadinima: "), adresas=input("Iveskite adresa: ") , banko_kodas=int(input("Iveskite banko koda: ")), swift=input("Iveskite swift koda: "))
    session.add(ivesti_b)
    session.commit()

def ivesti_saskaita():
    asmenys = session.query(Asmuo).all()
    for asmuo in asmenys:
        print(asmuo.id, asmuo.vardas, asmuo.pavarde, asmuo.asmens_kodas)
    asmens_id = int(input("Pasirinkite asmens ID prie kurio pridesite saskaita: "))
    bankai = session.query(Bankas).all()
    for bankas in bankai:
        print(bankas.id, bankas.pavadinimas)
    bankas_id = int(input("Pasirinkite banko ID, kuriame yra saskaita: "))
    saskaita_i = Saskaita(saskaitos_numeris=input("iveskite sask. numeri: "), balansas=input("iveskite balansa:"), asmuo_id=asmens_id, bankas_id=bankas_id)
    session.add(saskaita_i)
    session.commit()

def valdyti_saskaitos_balansa():
    asmenys = session.query(Asmuo).all()
    for asmuo in asmenys:
        print(asmuo.id, asmuo.vardas, asmuo.pavarde, asmuo.asmens_kodas)
    asmens_id_ = int(input("Pasirinkite asmens ID, i kurio saskaita noresite prideti pajamu: "))
    saskaitos = session.query(Saskaita).filter(Saskaita.asmuo_id==asmens_id_)
    for saskaita in saskaitos:
        print(f"{saskaita.id},{saskaita.saskaitos_numeris}, balansas: {saskaita.balansas}")
    saskaita_id = float(input("pasirinkite saskaitos id, i kuria norite prideti pajamu: "))
    saskaitos = session.query(Saskaita).get(saskaita_id)
    prideti_pajamas = float(input("iveskite, kiek norite prideti pajamu, jei norite atimti, pajamas veskite su minuso zenklu: "))
    saskaitos.balansas += prideti_pajamas
    print(f"dabartinis balansas = {saskaitos.balansas}")
    session.commit()

def perziureti_savo_saskaitas():
    asmenys = session.query(Asmuo).all()
    for asmuo in asmenys:
        print(asmuo.id, asmuo.vardas, asmuo.pavarde, asmuo.asmens_kodas)
    asmens_id_ = int(input("Pasirinkite asmens ID, kurio saskaitas norite perziureti: "))
    saskaitos = session.query(Saskaita).filter(Saskaita.asmuo_id==asmens_id_)
    for saskaita in saskaitos:
        print(f"{saskaita.id},{saskaita.saskaitos_numeris}, balansas: {saskaita.balansas}")

def perziureti_viska():
    print("-----ASMENYS-----")
    asmenys = session.query(Asmuo).all()
    for asmuo in asmenys:
        print(asmuo.id, asmuo.vardas, asmuo.pavarde, asmuo.asmens_kodas)
    print("-----BANKAI-----")
    bankai = session.query(Bankas).all()
    for bankas in bankai:
        print(bankas.id, bankas.pavadinimas, bankas.adresas, bankas.banko_kodas, bankas.swift)
    print("-----SASKAITOS-----")
    saskaitos = session.query(Saskaita).all()
    for saskaita in saskaitos:
        print(f"{saskaita.id},{saskaita.saskaitos_numeris}, balansas: {saskaita.balansas}, asmens ID: {saskaita.asmuo_id}, banko ID:{saskaita.bankas_id}")
    

while True:
    choice = meniu()
    if choice == "0" or choice == "":
        break
    elif choice == "1":
        ivesti_asmeni()
    elif choice == "2":
        ivesti_banka()
    elif choice == "3":
        ivesti_saskaita()
    elif choice == "4":
        valdyti_saskaitos_balansa()
    elif choice == "5":
        perziureti_savo_saskaitas()
    elif choice == "6":
        perziureti_viska()