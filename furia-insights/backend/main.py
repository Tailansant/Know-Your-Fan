from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from crud import get_fans, get_fan, create_fan, update_fan, delete_fan
from database import SessionLocal, engine
import schemas
from models import Fan

# Inicializa o aplicativo FastAPI
app = FastAPI()

# Adiciona configuração de CORS
origins = [
    "http://localhost",  # Frontend rodando localmente
    "http://127.0.0.1:8000",  # Backend
    # Adicione outras origens se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode permitir todos os domínios ou ajustar conforme necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def read_root():
    return {"message": "Welcome to the FURIA Insights API!"}


# Endpoint para criar um fã
@app.post("/fans", response_model=schemas.Fan)
def create_fan_route(fan: schemas.FanCreate, db: Session = Depends(get_db)):
    db_fan = create_fan(db, fan)
    return db_fan

# Endpoint para listar todos os fãs
@app.get("/fans", response_model=list[schemas.Fan])
def read_fans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_fans(db, skip=skip, limit=limit)

# Endpoint para obter um fã específico por ID
@app.get("/fans/{fan_id}", response_model=schemas.Fan)
def read_fan(fan_id: int, db: Session = Depends(get_db)):
    db_fan = get_fan(db, fan_id=fan_id)
    if db_fan is None:
        raise HTTPException(status_code=404, detail="Fan not found")
    return db_fan

# Endpoint para atualizar as informações de um fã
@app.put("/fans/{fan_id}", response_model=schemas.Fan)
def update_fan_route(fan_id: int, fan: schemas.FanCreate, db: Session = Depends(get_db)):
    db_fan = update_fan(db, fan_id=fan_id, fan=fan)
    if db_fan is None:
        raise HTTPException(status_code=404, detail="Fan not found")
    return db_fan

# Endpoint para excluir um fã
@app.delete("/fans/{fan_id}", response_model=schemas.Fan)
def delete_fan_route(fan_id: int, db: Session = Depends(get_db)):
    db_fan = delete_fan(db, fan_id=fan_id)
    if db_fan is None:
        raise HTTPException(status_code=404, detail="Fan not found")
    return db_fan
