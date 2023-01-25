from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/bankai.db')
Base = declarative_base()

class Asmuo(Base):
    __tablename__="asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    asmens_kodas = Column(Integer)
    tel_numeris = Column(Integer)
    saskaitos = relationship("Saskaita", back_populates="zmogus")

class Bankas(Base):
    __tablename__="bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    adresas = Column(String)
    banko_kodas = Column(Integer)
    swift = Column(String)
    saskaitos = relationship("Saskaita", back_populates="bankas")

class Saskaita(Base):
    __tablename__="saskaita"
    id = Column(Integer, primary_key=True)
    saskaitos_numeris = Column(String)
    balansas = Column(Float)
    asmuo_id = Column(Integer, ForeignKey('asmuo.id'))
    zmogus = relationship("Asmuo", back_populates="saskaitos")
    bankas_id = Column(Integer, ForeignKey('bankas.id'))
    bankas = relationship("Bankas", back_populates="saskaitos")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    

