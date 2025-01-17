# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/mapping/proto/submap_visualization.proto

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
  name='cartographer/mapping/proto/submap_visualization.proto',
  package='cartographer.mapping.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5cartographer/mapping/proto/submap_visualization.proto\x12\x1a\x63\x61rtographer.mapping.proto\x1a,cartographer/transform/proto/transform.proto\"\x95\x02\n\nSubmapList\x12O\n\ntrajectory\x18\x02 \x03(\x0b\x32;.cartographer.mapping.proto.SubmapList.TrajectorySubmapList\x1aZ\n\x0bSubmapEntry\x12\x16\n\x0esubmap_version\x18\x01 \x01(\x05\x12\x33\n\x04pose\x18\x03 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3d\x1aZ\n\x14TrajectorySubmapList\x12\x42\n\x06submap\x18\x01 \x03(\x0b\x32\x32.cartographer.mapping.proto.SubmapList.SubmapEntry\"\xe8\x03\n\x0bSubmapQuery\x12@\n\x07request\x18\x01 \x01(\x0b\x32/.cartographer.mapping.proto.SubmapQuery.Request\x12\x42\n\x08response\x18\x02 \x01(\x0b\x32\x30.cartographer.mapping.proto.SubmapQuery.Response\x1a\x36\n\x07Request\x12\x14\n\x0csubmap_index\x18\x01 \x01(\x05\x12\x15\n\rtrajectory_id\x18\x02 \x01(\x05\x1a\x9a\x02\n\x08Response\x12\x16\n\x0esubmap_version\x18\x02 \x01(\x05\x12P\n\x08textures\x18\n \x03(\x0b\x32>.cartographer.mapping.proto.SubmapQuery.Response.SubmapTexture\x12\x15\n\rerror_message\x18\x08 \x01(\t\x1a\x8c\x01\n\rSubmapTexture\x12\r\n\x05\x63\x65lls\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x12\n\nresolution\x18\x04 \x01(\x01\x12\x39\n\nslice_pose\x18\x05 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3db\x06proto3')
  ,
  dependencies=[cartographer_dot_transform_dot_proto_dot_transform__pb2.DESCRIPTOR,])




_SUBMAPLIST_SUBMAPENTRY = _descriptor.Descriptor(
  name='SubmapEntry',
  full_name='cartographer.mapping.proto.SubmapList.SubmapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='submap_version', full_name='cartographer.mapping.proto.SubmapList.SubmapEntry.submap_version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose', full_name='cartographer.mapping.proto.SubmapList.SubmapEntry.pose', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=227,
  serialized_end=317,
)

_SUBMAPLIST_TRAJECTORYSUBMAPLIST = _descriptor.Descriptor(
  name='TrajectorySubmapList',
  full_name='cartographer.mapping.proto.SubmapList.TrajectorySubmapList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='submap', full_name='cartographer.mapping.proto.SubmapList.TrajectorySubmapList.submap', index=0,
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
  serialized_start=319,
  serialized_end=409,
)

_SUBMAPLIST = _descriptor.Descriptor(
  name='SubmapList',
  full_name='cartographer.mapping.proto.SubmapList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trajectory', full_name='cartographer.mapping.proto.SubmapList.trajectory', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUBMAPLIST_SUBMAPENTRY, _SUBMAPLIST_TRAJECTORYSUBMAPLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=409,
)


_SUBMAPQUERY_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='cartographer.mapping.proto.SubmapQuery.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='submap_index', full_name='cartographer.mapping.proto.SubmapQuery.Request.submap_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trajectory_id', full_name='cartographer.mapping.proto.SubmapQuery.Request.trajectory_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=561,
  serialized_end=615,
)

_SUBMAPQUERY_RESPONSE_SUBMAPTEXTURE = _descriptor.Descriptor(
  name='SubmapTexture',
  full_name='cartographer.mapping.proto.SubmapQuery.Response.SubmapTexture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='cartographer.mapping.proto.SubmapQuery.Response.SubmapTexture.cells', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='cartographer.mapping.proto.SubmapQuery.Response.SubmapTexture.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='cartographer.mapping.proto.SubmapQuery.Response.SubmapTexture.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='cartographer.mapping.proto.SubmapQuery.Response.SubmapTexture.resolution', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slice_pose', full_name='cartographer.mapping.proto.SubmapQuery.Response.SubmapTexture.slice_pose', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=760,
  serialized_end=900,
)

_SUBMAPQUERY_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='cartographer.mapping.proto.SubmapQuery.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='submap_version', full_name='cartographer.mapping.proto.SubmapQuery.Response.submap_version', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='textures', full_name='cartographer.mapping.proto.SubmapQuery.Response.textures', index=1,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='cartographer.mapping.proto.SubmapQuery.Response.error_message', index=2,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUBMAPQUERY_RESPONSE_SUBMAPTEXTURE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=618,
  serialized_end=900,
)

_SUBMAPQUERY = _descriptor.Descriptor(
  name='SubmapQuery',
  full_name='cartographer.mapping.proto.SubmapQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='cartographer.mapping.proto.SubmapQuery.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='cartographer.mapping.proto.SubmapQuery.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUBMAPQUERY_REQUEST, _SUBMAPQUERY_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=900,
)

_SUBMAPLIST_SUBMAPENTRY.fields_by_name['pose'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_SUBMAPLIST_SUBMAPENTRY.containing_type = _SUBMAPLIST
_SUBMAPLIST_TRAJECTORYSUBMAPLIST.fields_by_name['submap'].message_type = _SUBMAPLIST_SUBMAPENTRY
_SUBMAPLIST_TRAJECTORYSUBMAPLIST.containing_type = _SUBMAPLIST
_SUBMAPLIST.fields_by_name['trajectory'].message_type = _SUBMAPLIST_TRAJECTORYSUBMAPLIST
_SUBMAPQUERY_REQUEST.containing_type = _SUBMAPQUERY
_SUBMAPQUERY_RESPONSE_SUBMAPTEXTURE.fields_by_name['slice_pose'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_SUBMAPQUERY_RESPONSE_SUBMAPTEXTURE.containing_type = _SUBMAPQUERY_RESPONSE
_SUBMAPQUERY_RESPONSE.fields_by_name['textures'].message_type = _SUBMAPQUERY_RESPONSE_SUBMAPTEXTURE
_SUBMAPQUERY_RESPONSE.containing_type = _SUBMAPQUERY
_SUBMAPQUERY.fields_by_name['request'].message_type = _SUBMAPQUERY_REQUEST
_SUBMAPQUERY.fields_by_name['response'].message_type = _SUBMAPQUERY_RESPONSE
DESCRIPTOR.message_types_by_name['SubmapList'] = _SUBMAPLIST
DESCRIPTOR.message_types_by_name['SubmapQuery'] = _SUBMAPQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmapList = _reflection.GeneratedProtocolMessageType('SubmapList', (_message.Message,), dict(

  SubmapEntry = _reflection.GeneratedProtocolMessageType('SubmapEntry', (_message.Message,), dict(
    DESCRIPTOR = _SUBMAPLIST_SUBMAPENTRY,
    __module__ = 'cartographer.mapping.proto.submap_visualization_pb2'
    # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.SubmapList.SubmapEntry)
    ))
  ,

  TrajectorySubmapList = _reflection.GeneratedProtocolMessageType('TrajectorySubmapList', (_message.Message,), dict(
    DESCRIPTOR = _SUBMAPLIST_TRAJECTORYSUBMAPLIST,
    __module__ = 'cartographer.mapping.proto.submap_visualization_pb2'
    # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.SubmapList.TrajectorySubmapList)
    ))
  ,
  DESCRIPTOR = _SUBMAPLIST,
  __module__ = 'cartographer.mapping.proto.submap_visualization_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.SubmapList)
  ))
_sym_db.RegisterMessage(SubmapList)
_sym_db.RegisterMessage(SubmapList.SubmapEntry)
_sym_db.RegisterMessage(SubmapList.TrajectorySubmapList)

SubmapQuery = _reflection.GeneratedProtocolMessageType('SubmapQuery', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _SUBMAPQUERY_REQUEST,
    __module__ = 'cartographer.mapping.proto.submap_visualization_pb2'
    # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.SubmapQuery.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

    SubmapTexture = _reflection.GeneratedProtocolMessageType('SubmapTexture', (_message.Message,), dict(
      DESCRIPTOR = _SUBMAPQUERY_RESPONSE_SUBMAPTEXTURE,
      __module__ = 'cartographer.mapping.proto.submap_visualization_pb2'
      # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.SubmapQuery.Response.SubmapTexture)
      ))
    ,
    DESCRIPTOR = _SUBMAPQUERY_RESPONSE,
    __module__ = 'cartographer.mapping.proto.submap_visualization_pb2'
    # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.SubmapQuery.Response)
    ))
  ,
  DESCRIPTOR = _SUBMAPQUERY,
  __module__ = 'cartographer.mapping.proto.submap_visualization_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.SubmapQuery)
  ))
_sym_db.RegisterMessage(SubmapQuery)
_sym_db.RegisterMessage(SubmapQuery.Request)
_sym_db.RegisterMessage(SubmapQuery.Response)
_sym_db.RegisterMessage(SubmapQuery.Response.SubmapTexture)


# @@protoc_insertion_point(module_scope)
