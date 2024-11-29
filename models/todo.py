from models.todo_database import ToDoBase
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, Boolean


class ToDo(ToDoBase):
    __tablename__ = "todos"

    name: Mapped[str] = mapped_column(String, nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    day: Mapped[int] = mapped_column(Integer, default=0)
