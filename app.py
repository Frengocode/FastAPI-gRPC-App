from fastapi import FastAPI
from router.todo import todo_router


app = FastAPI(title="Basic App Using Gprc")


app.include_router(todo_router)
