# main.py
from fastapi import FastAPI, Depends, HTTPException
from schemas import FanCreate  
from sqlalchemy.orm import Session
from crud import get_fans, get_fan, create_fan, update_fan, delete_fan
from database import SessionLocal, engine
from models import Fan
import schemas

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/fans", response_model=schemas.Fan)
def create_fan_route(fan: schemas.FanCreate, db: Session = Depends(get_db)):
    db_fan = create_fan(db, fan)
    return db_fan

@app.get("/fans", response_model=list[schemas.Fan])
def read_fans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_fans(db, skip=skip, limit=limit)

@app.get("/fans/{fan_id}", response_model=schemas.Fan)
def read_fan(fan_id: int, db: Session = Depends(get_db)):
    db_fan = get_fan(db, fan_id=fan_id)
    if db_fan is None:
        raise HTTPException(status_code=404, detail="Fan not found")
    return db_fan

@app.put("/fans/{fan_id}", response_model=schemas.Fan)
def update_fan_route(fan_id: int, fan: schemas.FanCreate, db: Session = Depends(get_db)):
    db_fan = update_fan(db, fan_id=fan_id, fan=fan)
    if db_fan is None:
        raise HTTPException(status_code=404, detail="Fan not found")
    return db_fan

@app.delete("/fans/{fan_id}", response_model=schemas.Fan)
def delete_fan_route(fan_id: int, db: Session = Depends(get_db)):
    db_fan = delete_fan(db, fan_id=fan_id)
    if db_fan is None:
        raise HTTPException(status_code=404, detail="Fan not found")
    return db_fan
