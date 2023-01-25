from sqlalchemy.orm import sessionmaker
from many_to_many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

# kestutis = Tevas(vardas="Kestutis", pavarde="Januskevicius")
# emilija = Vaikas(vardas="Emilija", pavarde="Januskeviciute")
# kestutis.vaikai.append(emilija)
# session.add(kestutis)
# session.commit()

# mama = Tevas(vardas="Nicoletta", pavarde="Januskeviciene")
# emilija = session.query(Vaikas).filter_by(vardas="Emilija").one()
# if emilija:
#     mama.vaikai.append(emilija)
# session.add(mama)
# session.commit()

# tevai = session.query(Tevas).filter(Tevas.pavarde.ilike("Janus%")).all()
# maja = Vaikas(vardas="Maja", pavarde="Januskeviciute", tevai=tevai)
# session.add(maja)
# session.commit()
# tevai = session.query(Tevas).filter(Tevas.pavarde.ilike("Janus%")).all()
# marco = Vaikas(vardas="Marco", pavarde="Januskevicius", tevai=tevai)
# session.add(marco)
# session.commit()