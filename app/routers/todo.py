from fastapi import APIRouter,Depends
from sqlmodel import Session
from database import get_sessions
from app.crud.todo import get_todos,create_todo,delete_todo,update_todo,get_todo
from app.schemas.todo import TodoRead, TodoCreate, TodoUpdate

router=APIRouter(prefix='/todos')

@router.get('/',response_model=list[TodoRead])
def read_todos(session:Session=Depends(get_sessions)):
    return get_todos(session=session)

#Traer solo 1 endpoint
@router.get('/{id}',response_model=TodoRead)
def read_todos_only_one(id:int,session:Session=Depends(get_sessions)):
    return get_todo(id=id,session=session)

@router.post('/',response_model=TodoRead)
def create(todo:TodoCreate,session:Session=Depends(get_sessions)):
    return create_todo(todo=todo,session=session)

@router.put('/{id}',response_model=TodoRead)
def update(id:int,todo:TodoUpdate,session:Session=Depends(get_sessions)):
    return update_todo(id=id,todo=todo,session=session)

@router.delete('/{id}')
def delete(id:int,session:Session=Depends(get_sessions)):
    return delete_todo(id=id,session=session)




