import grpc
from protos import todo_pb2_grpc

async def grpc_todo_client():
    channel = grpc.aio.insecure_channel("127.0.0.1:50051")
    client = todo_pb2_grpc.TodoServiceStub(channel)
    return client
