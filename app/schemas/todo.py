from sqlmodel import SQLModel
class TodoCreate(SQLModel):
    title:str
    completed:bool=False
class TodoRead(SQLModel):
    id:int 
    title:str 
    completed:bool
class TodoUpdate(SQLModel):
    title:str|None=None
    completed:bool|None=None

