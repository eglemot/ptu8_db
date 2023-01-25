from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///data/uzduotis2.db')
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = 'darbuotojas'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    gimimo_data = Column(Integer)
    pareigos = Column(String)
    atlyginimas = Column(Float)
    nuo_kada_dirba = Column(DateTime, default = datetime.utcnow)

    def __init__(self, vardas, pavarde, gimimo_data, pareigos, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas
    
    def __repr__(self):
        return f"({self.id},{self.vardas},{self.pavarde},{self.gimimo_data},{self.pareigos},{self.atlyginimas},{self.nuo_kada_dirba})"

    def __str__(self):
        return f"(ID: {self.id}, Vardas: {self.vardas}, Pavarde: {self.pavarde}, Gimimo data: {self.gimimo_data}, Pareigos: {self.pareigos}, Atlyginimas: {self.atlyginimas}, Nuo kada dirba: {self.nuo_kada_dirba})"
    
if __name__ == "__main__":
    Base.metadata.create_all(engine)