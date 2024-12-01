from fastapi import APIRouter, Depends
from client import grpc_todo_client
from protos import todo_pb2, todo_pb2_grpc
from google.protobuf.json_format import MessageToDict
from typing import Annotated
from scheme.todo_scheme import CreateTodoSchema, UpdateTodoRequest

todo_router = APIRouter(tags=["Todo Service"])


@todo_router.post("/create-todo/")
async def create_todo(
    request: CreateTodoSchema,
    client: todo_pb2_grpc.TodoServiceStub = Depends(grpc_todo_client),
):
    response = await client.CreateTodo(
        todo_pb2.CreateToDoRequest(
            name=request.name, completed=request.completed, day=request.day
        )
    )
    return MessageToDict(response.todo)


@todo_router.get("/get-all-todo/")
async def get_all_todo(
    client: Annotated[todo_pb2_grpc.TodoServiceStub, Depends(grpc_todo_client)],
):
    response = await client.GetTodo(todo_pb2.GetToDoResponse())
    return MessageToDict(response)


@todo_router.get("/get-todo/{id}/")
async def get_todo(
    id: int, client: Annotated[todo_pb2_grpc.TodoServiceStub, Depends(grpc_todo_client)]
):
    response = await client.GetOneTodo(todo_pb2.GetOneTodoRequest(id=id))

    return MessageToDict(response)


@todo_router.patch("/update-todo-status/")
async def update_todo_status(
    request: UpdateTodoRequest,
    client: Annotated[todo_pb2_grpc.TodoServiceStub, Depends(grpc_todo_client)],
):
    # Call the gRPC method to update the todo status
    await client.UpdateTodoStatus(
        todo_pb2.UpdateTodoStatusRequest(id=request.id, completed=request.completed)
    )
    # No return here, as the service doesn't return anything
    return {"message": "Todo status updated successfully"}


@todo_router.delete("/delete-todo/{id}/")
async def delete_todo(
    id: int, client: Annotated[todo_pb2_grpc.TodoServiceStub, Depends(grpc_todo_client)]
):
    response = await client.DeleteTodo(todo_pb2.DeleteTodoRequest(id=id))

    return MessageToDict(response)
