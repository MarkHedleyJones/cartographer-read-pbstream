# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/ground_truth/proto/relations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cartographer.transform.proto import transform_pb2 as cartographer_dot_transform_dot_proto_dot_transform__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cartographer/ground_truth/proto/relations.proto',
  package='cartographer.ground_truth.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/cartographer/ground_truth/proto/relations.proto\x12\x1f\x63\x61rtographer.ground_truth.proto\x1a,cartographer/transform/proto/transform.proto\"\x85\x01\n\x08Relation\x12\x12\n\ntimestamp1\x18\x01 \x01(\x03\x12\x12\n\ntimestamp2\x18\x02 \x01(\x03\x12\x37\n\x08\x65xpected\x18\x03 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3d\x12\x18\n\x10\x63overed_distance\x18\x04 \x01(\x01\"J\n\x0bGroundTruth\x12;\n\x08relation\x18\x01 \x03(\x0b\x32).cartographer.ground_truth.proto.Relationb\x06proto3')
  ,
  dependencies=[cartographer_dot_transform_dot_proto_dot_transform__pb2.DESCRIPTOR,])




_RELATION = _descriptor.Descriptor(
  name='Relation',
  full_name='cartographer.ground_truth.proto.Relation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp1', full_name='cartographer.ground_truth.proto.Relation.timestamp1', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp2', full_name='cartographer.ground_truth.proto.Relation.timestamp2', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected', full_name='cartographer.ground_truth.proto.Relation.expected', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='covered_distance', full_name='cartographer.ground_truth.proto.Relation.covered_distance', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=264,
)


_GROUNDTRUTH = _descriptor.Descriptor(
  name='GroundTruth',
  full_name='cartographer.ground_truth.proto.GroundTruth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='cartographer.ground_truth.proto.GroundTruth.relation', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=340,
)

_RELATION.fields_by_name['expected'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_GROUNDTRUTH.fields_by_name['relation'].message_type = _RELATION
DESCRIPTOR.message_types_by_name['Relation'] = _RELATION
DESCRIPTOR.message_types_by_name['GroundTruth'] = _GROUNDTRUTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Relation = _reflection.GeneratedProtocolMessageType('Relation', (_message.Message,), dict(
  DESCRIPTOR = _RELATION,
  __module__ = 'cartographer.ground_truth.proto.relations_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.ground_truth.proto.Relation)
  ))
_sym_db.RegisterMessage(Relation)

GroundTruth = _reflection.GeneratedProtocolMessageType('GroundTruth', (_message.Message,), dict(
  DESCRIPTOR = _GROUNDTRUTH,
  __module__ = 'cartographer.ground_truth.proto.relations_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.ground_truth.proto.GroundTruth)
  ))
_sym_db.RegisterMessage(GroundTruth)


# @@protoc_insertion_point(module_scope)