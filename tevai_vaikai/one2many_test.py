from sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

kestutis = Tevas(vardas="Kestutis", pavarde="Januskevicius")
emilija = Vaikas(vardas="Emilija", pavarde="Januskeviciute")
maja = Vaikas(vardas="Maja", pavarde="Januskeviciut")
marco = Vaikas(vardas="Marco", pavarde="Januskevicius")

# marco.tevas = kestutis
# emilija.tevas = kestutis
# maja.tevas = kestutis
# session.add(emilija)
# session.add(maja)
# session.add(marco)

kestutis.vaikai.append(emilija)
kestutis.vaikai.append(maja)
kestutis.vaikai.append(marco)
session.add(kestutis)
#alternatyviai, jeigu nera kitu vaiku:
# kestutis.vaikai = [emilija,maja, marco]
#sitam nereikia add!!
session.commit()


