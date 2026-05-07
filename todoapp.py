from fastapi import FastAPI
from uuid import UUID,  uuid4
from pydantic import BaseModel, Field



app=FastAPI()
# starting doing a todo application backend!!

class BaseOut(BaseModel):
    msg : str
    error : str=False

class Todo(BaseModel):
    id: UUID =Field(default_factory=uuid4)
    name : str
    category :  str
    status : bool= False

# local variable for todo
db: list[Todo] =[]


class TodoCreateOut(BaseOut):
    todo : Todo

@app.post(
    "/create",
    response_model=TodoCreateOut
)
def create_todo(todo:Todo) ->TodoCreateOut:
    db.append(todo)
    return TodoCreateOut(todo=todo,msg="successfully created::")

class TodoGetOut(BaseOut):
    todos: list[Todo]


@app.get(
        "/todos",
        response_model=TodoGetOut
)

def fetch_todos():
    return TodoGetOut(todos=db,msg="todos haru fetch vayo::")

# print(db[0])

# fetch todo by id
@app.get(
    "/todo/{user_id}",
    response_model=TodoCreateOut | BaseOut
)

def fetchTodos_by_id(user_id:str) -> TodoCreateOut | BaseOut:
    try:
        user_id=UUID(user_id)
    except Exception as ex:
        return BaseOut(msg="Invalied uuid",error=str(ex))
    
    for todo in db:
        if todo.id==user_id:
            return TodoCreateOut(todo=todo,msg=f"todo is fetched for id {user_id}")
    return BaseOut(msg="no to do found::")
    
