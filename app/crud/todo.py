from sqlmodel import Session,select
from app.schemas.todo import TodoCreate,TodoUpdate
from app.models.todo import Todo

def get_todo(id:int,session:Session):
    return session.get(Todo,id)

def get_todos(session:Session):
    return session.exec(select(Todo)).all()

def create_todo(todo:TodoCreate,session:Session):
    todo_db=Todo.model_validate(todo)
    session.add(todo_db)
    session.commit()
    session.refresh(todo_db)
    return todo_db

def update_todo(id:int,session:Session,todo:TodoUpdate):
    todo_update_db=session.get(Todo,id)
    if todo_update_db is None:
        return None
    else:
        todo_update_new=todo.model_dump(exclude_unset=True)
        for key, value in todo_update_new.items():
            setattr(todo_update_db,key,value)
        session.commit()
        session.refresh(todo_update_db)
        return todo_update_db
    
def delete_todo(id:int, session:Session):
    delete_todo_db=session.get(Todo,id)
    if delete_todo_db is None:
        return None
    else:
        session.delete(delete_todo_db)
        session.commit()
        return {'message':"Task eliminated"}
