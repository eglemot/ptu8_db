from pagrindinis import Darbuotojas, engine
from sqlalchemy.orm import sessionmaker
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
from tkinter.font import Font

session = sessionmaker(bind=engine)()

def meniu():
    print("===[ Darbuotojo programa ]===")
    print("1 Prideti darbuotoja:")
    print("2 Perziureti sarasa")
    print("3 Atnaujinti")
    print("4 Istrinti darbuotoja")
    print("0 Iseiti is programos")
    choice = input("Pasirinkite: ")
    return choice

def sukurti_darbuotoja(vardas, pavarde, gimimo_data, pareigos, atlyginimas):
    darbuotojas = Darbuotojas(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
    session.add(darbuotojas)
    session.commit()
    print(f"SUKURTAS naujas darbuotojas: {darbuotojas}")
    return(darbuotojas)

def skaityti_darbuotoja():
    try: 
        vardas = input("Vardas:")
        pavarde = input("Pavarde:")
        gimimo_data = input("Gimimo data")
        pareigos = input("Pareigos")
        atlyginimas = float(input("Atlyginimas:"))
    except ValueError:
        print("Atlyginimas ivestas ne skaiciais")
    else:
        return sukurti_darbuotoja(vardas, pavarde, gimimo_data, pareigos, atlyginimas)

def parodyti_darbuotojus(query=session.query(Darbuotojas)):
    if query and len(query.all()) > 0:
        for darbuotojas in query.all():
            print(darbuotojas)
    else:
        print("Nieko nera")

def pakeisti():
    darbuotojas = session.query(Darbuotojas).get(input("iveskite id:"))
    vardas_ivestis = input("ivesk nauja varda: ")
    pavarde_ivestis = input("ivesk nauja pavarde: ")
    gimimo_data_ivestis = input("ivesk nauja gimimo data: ")
    pareigos_ivestis = input("ivesk naujas pareigas: ")
    atlyginimas_ivestis = input("ivesk nauja atlyginima: ")
    if len(vardas_ivestis) > 0:
        darbuotojas.vardas = vardas_ivestis
    elif len(pavarde_ivestis) > 0:
        darbuotojas.pavarde = pavarde_ivestis
    elif len(gimimo_data_ivestis) > 0:
        darbuotojas.gimimo_data = gimimo_data_ivestis
    elif len(pareigos_ivestis) > 0:
        darbuotojas.pareigos = pareigos_ivestis
    elif len(atlyginimas_ivestis) > 0:
        darbuotojas.atlyginimas = atlyginimas_ivestis
    else:
        print("kazkas ne to")
    print(darbuotojas)
    session.commit()

def istrinti_darbuotoja():
    id = input("Iveskite id:")
    darbuotojas = session.query(Darbuotojas).get(id)
    session.delete(darbuotojas)
    session.commit()
    print(f"ISTRTINTAS {darbuotojas}" )







while True:
    choice = meniu()
    if choice == "0" or choice == "":
        break
    elif choice == "1":
        skaityti_darbuotoja()
    elif choice == "2":
        parodyti_darbuotojus()
    elif choice == "3":
        pakeisti()
    elif choice == "4":
        istrinti_darbuotoja()
    else:
        print("Error: Blogas pasirinkimas {choice}")


