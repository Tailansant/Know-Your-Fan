from sqlalchemy import Column, Integer, String, JSON  # Adicione o JSON aqui
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Fan(Base):
    __tablename__ = 'fans'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    location = Column(String)
    preferences = Column(JSON)  # Altere para o tipo JSON
