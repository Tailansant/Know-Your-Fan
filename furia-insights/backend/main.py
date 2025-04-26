from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login", response_model=schemas.FanOut)
def fake_login(fan: schemas.FanCreate, db: Session = Depends(get_db)):
    db_fan = models.Fan(**fan.dict())
    db.add(db_fan)
    db.commit()
    db.refresh(db_fan)
    return db_fan

@app.get("/fans")
def get_all_fans(db: Session = Depends(get_db)):
    return db.query(models.Fan).all()
