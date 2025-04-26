import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DB = os.getenv("MYSQL_DB")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

# Criação do engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão de banco de dados
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base para as tabelas
Base = declarative_base()

# Criação das tabelas no banco de dados
def create_database():
    Base.metadata.create_all(bind=engine)

# Chame essa função para criar as tabelas
create_database()
