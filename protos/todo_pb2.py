# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/todo.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'protos/todo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/todo.proto\x12\x04todo\x1a\x1bgoogle/protobuf/empty.proto\"@\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tcompleted\x18\x03 \x01(\x08\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x04\"A\n\x11\x43reateToDoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tcompleted\x18\x02 \x01(\x08\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x04\".\n\x12\x43reateToDoResponse\x12\x18\n\x04todo\x18\x01 \x01(\x0b\x32\n.todo.Todo\",\n\x0fGetToDoResponse\x12\x19\n\x05todos\x18\x01 \x03(\x0b\x32\n.todo.Todo\"\x1f\n\x11GetOneTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x04\".\n\x12GetOneToDoResponse\x12\x18\n\x04todo\x18\x01 \x01(\x0b\x32\n.todo.Todo\"8\n\x17UpdateTodoStatusRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tcompleted\x18\x02 \x01(\x08\"\x1f\n\x11\x44\x65leteTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"$\n\x12\x44\x65leteTodoResponse\x12\x0e\n\x06\x64\x65tail\x18\x01 \x01(\t2\xd5\x02\n\x0bTodoService\x12?\n\nCreateTodo\x12\x17.todo.CreateToDoRequest\x1a\x18.todo.CreateToDoResponse\x12\x38\n\x07GetTodo\x12\x16.google.protobuf.Empty\x1a\x15.todo.GetToDoResponse\x12?\n\nGetOneTodo\x12\x17.todo.GetOneTodoRequest\x1a\x18.todo.GetOneToDoResponse\x12I\n\x10UpdateTodoStatus\x12\x1d.todo.UpdateTodoStatusRequest\x1a\x16.google.protobuf.Empty\x12?\n\nDeleteTodo\x12\x17.todo.DeleteTodoRequest\x1a\x18.todo.DeleteTodoResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.todo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TODO']._serialized_start=56
  _globals['_TODO']._serialized_end=120
  _globals['_CREATETODOREQUEST']._serialized_start=122
  _globals['_CREATETODOREQUEST']._serialized_end=187
  _globals['_CREATETODORESPONSE']._serialized_start=189
  _globals['_CREATETODORESPONSE']._serialized_end=235
  _globals['_GETTODORESPONSE']._serialized_start=237
  _globals['_GETTODORESPONSE']._serialized_end=281
  _globals['_GETONETODOREQUEST']._serialized_start=283
  _globals['_GETONETODOREQUEST']._serialized_end=314
  _globals['_GETONETODORESPONSE']._serialized_start=316
  _globals['_GETONETODORESPONSE']._serialized_end=362
  _globals['_UPDATETODOSTATUSREQUEST']._serialized_start=364
  _globals['_UPDATETODOSTATUSREQUEST']._serialized_end=420
  _globals['_DELETETODOREQUEST']._serialized_start=422
  _globals['_DELETETODOREQUEST']._serialized_end=453
  _globals['_DELETETODORESPONSE']._serialized_start=455
  _globals['_DELETETODORESPONSE']._serialized_end=491
  _globals['_TODOSERVICE']._serialized_start=494
  _globals['_TODOSERVICE']._serialized_end=835
# @@protoc_insertion_point(module_scope)
