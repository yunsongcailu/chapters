# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndemo.proto\x12\ndemo_proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2I\n\x07Greeter\x12>\n\x08SayHello\x12\x18.demo_proto.HelloRequest\x1a\x16.demo_proto.HelloReply\"\x00\x42!Z\x1f\x64\x65mo_grpc/demo_proto/gen;demopbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'demo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\037demo_grpc/demo_proto/gen;demopb'
  _HELLOREQUEST._serialized_start=26
  _HELLOREQUEST._serialized_end=54
  _HELLOREPLY._serialized_start=56
  _HELLOREPLY._serialized_end=85
  _GREETER._serialized_start=87
  _GREETER._serialized_end=160
# @@protoc_insertion_point(module_scope)