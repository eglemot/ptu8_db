# crud= Create READ UPDATE, DELETE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Project

engine = create_engine('sqlite:///data/projektai.db')
# Session = sessionmaker(bind=engine)
# session = Session()
session = sessionmaker(bind=engine)()

# # naujas_projektas = Project("brangus reikalas", 14000)
# kitas_projektas = Project("geras puslapiukas", 500)
# # session.add(naujas_projektas)
# session.add(kitas_projektas)
# session.commit()

# READ
# projektas1 = session.query(Project).get(2)
# projektas2 = session.query(Project).filter_by(name="kiti reikalai").all()
# # projektai = session.query(Project).all()
# pigus_projektai = session.query(Project).filter(Project.price <= 10000).all()
# print(pigus_projektai)
# reikalai = session.query(Project).filter(Project.name.ilike("%reikala%")).all()
# print(reikalai)
# projektas3 = session.query(Project).filter_by(name="geras puslapiukas").one()

#UPDATE 
# brangus = session.query(Project).filter(Project.price > 13000).first()
# brangus.price = 1000000
# session.commit()
# print(brangus)

#DELETE
projektas3 = session.query(Project).filter_by(name="geras puslapiukas").one()
session.delete(projektas3)
session.commit()
projektai = session.query(Project).all()
print(projektai)