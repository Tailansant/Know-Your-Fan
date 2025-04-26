# crud.py
from sqlalchemy.orm import Session
from schemas import FanCreate  # Importando FanCreate de schemas
from models import Fan

def get_fans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Fan).offset(skip).limit(limit).all()

def get_fan(db: Session, fan_id: int):
    return db.query(Fan).filter(Fan.id == fan_id).first()

def create_fan(db: Session, fan: FanCreate):
    db_fan = Fan(
        name=fan.name,
        username=fan.username,
        location=fan.location,
        preferences=fan.preferences
    )
    db.add(db_fan)
    db.commit()
    db.refresh(db_fan)
    return db_fan

def update_fan(db: Session, fan_id: int, fan: Fan):
    db_fan = db.query(Fan).filter(Fan.id == fan_id).first()
    if db_fan:
        db_fan.name = fan.name
        db_fan.username = fan.username
        db_fan.location = fan.location
        db_fan.preferences = fan.preferences
        db.commit()
        db.refresh(db_fan)
    return db_fan

def delete_fan(db: Session, fan_id: int):
    db_fan = db.query(Fan).filter(Fan.id == fan_id).first()
    if db_fan:
        db.delete(db_fan)
        db.commit()
    return db_fan
