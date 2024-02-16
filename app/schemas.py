"""
Os esquemas Pydantic são usados para validação de dados de entrada e saída da API. 
Eles são úteis para garantir que os dados recebidos e enviados pela API estejam corretos.
"""
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskInDB(TaskBase):
    id: int

    class Config:
        orm_mode = True
