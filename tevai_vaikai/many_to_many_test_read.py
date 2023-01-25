from sqlalchemy.orm import sessionmaker
from many_to_many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

print("---tevas su vaikais---")
tevas = session.query(Tevas).filter_by(vardas="Kestutis").one()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print("-", vaikas.vardas, vaikas.pavarde)

print("---mama su vaikais---")
mama = session.query(Tevas).filter_by(vardas="Nicoletta").one()
print(mama.vardas, mama.pavarde)
for vaikas in mama.vaikai:
    print("-", vaikas.vardas, vaikas.pavarde)

# print("------vaikas su tevais-----")
# emilija = session.query(Vaikas).filter_by(vardas="Emilija").one()
# print(emilija. vardas, emilija.pavarde)
# for emilijos_tevas in emilija.tevai:
#     print("-", emilijos_tevas.vardas, emilijos_tevas.pavarde)

print("------vaikas su tevais-----")
vaikai = session.query(Vaikas).all()
for vaikas in vaikai:
    print(vaikas.vardas, vaikas.pavarde)
    for vaiko_tevas in vaikas.tevai:
        print("-", vaiko_tevas.vardas, vaiko_tevas.pavarde)