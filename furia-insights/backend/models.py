from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Fan(Base):
    __tablename__ = "fans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    location = Column(String)
    preferences = Column(JSON)
