from pydantic import BaseModel


class Todo(BaseModel):
    task: str

class TodoResponse(Todo):
    task_in:int
    completed:int
    create_at:str