from grpc import aio
from protos import todo_pb2_grpc, todo_pb2
import logging
from models.todo import ToDo
from models.todo_database import get_todo_session, async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy import select
from google.protobuf.empty_pb2 import Empty



logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class TodoService(todo_pb2_grpc.TodoServiceServicer):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def CreateTodo(self, request, context):
        log.info(
            f"Received request: name={request.name}, completed={request.completed}, day={request.day}"
        )

        async for session in get_todo_session():
            todo = ToDo(name=request.name, completed=request.completed, day=request.day)
            session.add(todo)
            await session.commit()
            log.info("Todo added to the database")

        return todo_pb2.CreateToDoResponse(
            todo=todo_pb2.Todo(
                name=request.name,
                completed=request.completed,
                day=request.day,
            )
        )

    async def GetTodo(self, request, context):
        todos = (
            (await self.session.execute(select(ToDo).order_by(ToDo.date_pub.desc())))
            .scalars()
            .all()
        )

        grpc_todos = [
            todo_pb2.Todo(
                id=todo.id,
                name=todo.name,
                completed=todo.completed,
                day=todo.day,
            )
            for todo in todos
        ]

        for todo in todos:
            log.warn(f"{todo.completed}")

        return todo_pb2.GetToDoResponse(todos=grpc_todos)

    async def GetOneTodo(self, request, context):
        todo = (
            (await self.session.execute(select(ToDo).filter_by(id=request.id)))
            .scalars()
            .first()
        )

        if not todo:
            log.warn("ToDo Not Found")
            raise HTTPException(detail="Not Found", status_code=404)

        return todo_pb2.GetOneToDoResponse(
            todo=todo_pb2.Todo(
                id=todo.id,
                name=todo.name,
                completed=todo.completed,
                day=todo.day,
            )
        )
    


    async def UpdateTodoStatus(self, request, context):
        # Fetch the todo item by id
        todo = (
            (await self.session.execute(select(ToDo).filter_by(id=request.id)))
            .scalars()
            .first()
        )

        if not todo:
            log.info("Todo Not Found")
            raise HTTPException(detail="Not Found", status_code=404)

        todo.completed = request.completed 
        await self.session.commit()

        return Empty()



    async def DeleteTodo(self, request, context):
        todo = (
            (await self.session.execute(select(ToDo).filter_by(id=request.id)))
            .scalars()
            .first()
        )

        if not todo:
            log.warning(f"Todo With id {request.id} not found")
            raise HTTPException(detail="Not Found", status_code=404)

        log.info(f"Todo With id {request.id} deleted succsesfully")

        await self.session.delete(todo)
        await self.session.commit()

        return todo_pb2.DeleteTodoResponse(detail="Deleted Succsesfully")


async def run(addr="localhost:50051"):
    server = aio.server()

    async with async_session_maker() as session:
        todo_service = TodoService(session=session)

        todo_pb2_grpc.add_TodoServiceServicer_to_server(todo_service, server)
        server.add_insecure_port(addr)

        log.info(f"Starting server on {addr}")
        await server.start()
        await server.wait_for_termination()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
