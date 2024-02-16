from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

# Task: é um modelo que herda de Base, representando a tabela da tarefa
class Task(Base):
    __tablename__ = "tasks" # Define o nome da tabela no banco de dados

    # A instancia Column definem as colunas da tabela
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
