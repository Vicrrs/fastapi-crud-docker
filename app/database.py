from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://password@db:5432/todo_db"

# create_engine: Cria a conexão com o banco de dados PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal: é uma fabrica de sessões que permite transações com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: é uma classe para todos os modelos declarativos
Base = declarative_base()
