from pydantic import BaseModel


class CreateTodoSchema(BaseModel):
    name: str
    completed: bool
    day: int


class UpdateTodoRequest(BaseModel):
    id: int
    completed: bool