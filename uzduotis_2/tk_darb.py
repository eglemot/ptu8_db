from pagrindinis import Darbuotojas, engine
from sqlalchemy.orm import sessionmaker
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
from tkinter.font import Font

session = sessionmaker(bind=engine)()

def sukurti_darbuotoja(vardas, pavarde, gimimo_data, pareigos, atlyginimas):
    darbuotojas = Darbuotojas(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
    session.add(darbuotojas)
    session.commit()
    print(f"SUKURTAS naujas darbuotojas: {darbuotojas}")
    status['text'] = f"Sukurtas naujas darbuotojas:{darbuotojas}"
    return(darbuotojas)
    

def skaityti_darbuotoja():
    try: 
        vardas = ivesti_varda_e.get()
        pavarde = ivesti_pavarde_e.get()
        gimimo_data = ivesti_gimimo_data_e.get()
        pareigos = ivesti_pareigas_e.get()
        atlyginimas = float(ivesti_atlyginima_e.get())
    except ValueError:
        print("Atlyginimas ivestas ne skaiciais")
    else:
        return sukurti_darbuotoja(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
    

def parodyti_darbuotojus(query=session.query(Darbuotojas)):
    if query and len(query.all()) > 0:
        for darbuotojas in query.all():
            print(darbuotojas)
    status['text'] = f"Darbuotojai:{darbuotojas}"
    

def pakeisti():
    darbuotojas = session.query(Darbuotojas).get(input("iveskite id:"))
    darbuotojas.vardas = input("ivesk nauja varda: ")
    darbuotojas.pavarde = input("ivesk nauja pavarde: ")
    darbuotojas.gimimo_data = input("ivesk nauja gimimo data: ")
    darbuotojas.pareigos = input("ivesk naujas pareigas: ")
    darbuotojas.atlyginimas = input("ivesk nauja atlyginima: ")
    session.commit()
    print(f"PAKEISTAS DARBUOTOJAS I: {darbuotojas}")

def istrinti_darbuotoja():
    id = input("Iveskite id:")
    darbuotojas = session.query(Darbuotojas).get(id)
    session.delete(darbuotojas)
    session.commit()
    print(f"ISTRTINTAS {darbuotojas}" )



window = Tk()
window.title("DARBUOTOJAI")
window.geometry("400x400")
looks = Font(
    family = 'Helvetica',
    size = 20,
    weight = 'bold',
    slant = 'roman',
)
looks1 = Font(
    family = 'Helvetica',
    size = 14,
    weight = 'normal',
    slant = "italic",
    underline = 1,
)
looks2 = Font(
    family = 'Helvetica',
    size = 14,
    weight = 'bold',
)
ivesti_duomenis = Label(window, text= "SUKURKITE NAUJA DARBUOTOJA", font=looks)
ivesti_varda_l = Label(window, text="Vardas")
ivesti_varda_e = Entry(window)
ivesti_pavarde_l = Label(window, text="Pavarde")
ivesti_pavarde_e = Entry(window, text="Pavarde")
ivesti_gimimo_data_l = Label(window, text="Gimimo data")
ivesti_gimimo_data_e = Entry(window)
ivesti_pareigas_l = Label(window, text="Pareigos")
ivesti_pareigas_e = Entry(window)
ivesti_atlyginima_l = Label(window, text="Atlyginimas")
ivesti_atlyginima_e = Entry(window)
patvirtinti_ivesti = Button(window, text="Ivesti duomenis", command=skaityti_darbuotoja)
parodyti_ivestus_darb = Button(window, text="Parodyti ivestus darbuotojus", command=parodyti_darbuotojus)
status = Label(window, text="Laukiame veiksmu", border=10, font=looks1,)

ivesti_duomenis.grid(row=0, column=0)
ivesti_varda_l.grid(row=1, column=0)
ivesti_varda_e.grid(row=2, column=0)
ivesti_gimimo_data_l.grid(row=3, column=0)
ivesti_gimimo_data_e.grid(row=4, column=0)
ivesti_pareigas_l.grid(row=5, column=0)
ivesti_pareigas_e.grid(row=6, column=0)
ivesti_atlyginima_l.grid(row=7, column=0)
ivesti_atlyginima_e.grid(row=8, column=0)
patvirtinti_ivesti.grid(row=9, column=0)
parodyti_ivestus_darb.grid(row=11, column=0)
status.grid(row=10, column=0)
window.mainloop()