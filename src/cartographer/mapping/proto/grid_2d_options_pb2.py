# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/mapping/proto/grid_2d_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cartographer/mapping/proto/grid_2d_options.proto',
  package='cartographer.mapping.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0cartographer/mapping/proto/grid_2d_options.proto\x12\x1a\x63\x61rtographer.mapping.proto\"\xa8\x01\n\rGridOptions2D\x12\x45\n\tgrid_type\x18\x01 \x01(\x0e\x32\x32.cartographer.mapping.proto.GridOptions2D.GridType\x12\x12\n\nresolution\x18\x02 \x01(\x02\"<\n\x08GridType\x12\x10\n\x0cINVALID_GRID\x10\x00\x12\x14\n\x10PROBABILITY_GRID\x10\x01\x12\x08\n\x04TSDF\x10\x02\x62\x06proto3')
)



_GRIDOPTIONS2D_GRIDTYPE = _descriptor.EnumDescriptor(
  name='GridType',
  full_name='cartographer.mapping.proto.GridOptions2D.GridType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_GRID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROBABILITY_GRID', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TSDF', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=189,
  serialized_end=249,
)
_sym_db.RegisterEnumDescriptor(_GRIDOPTIONS2D_GRIDTYPE)


_GRIDOPTIONS2D = _descriptor.Descriptor(
  name='GridOptions2D',
  full_name='cartographer.mapping.proto.GridOptions2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grid_type', full_name='cartographer.mapping.proto.GridOptions2D.grid_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='cartographer.mapping.proto.GridOptions2D.resolution', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GRIDOPTIONS2D_GRIDTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=249,
)

_GRIDOPTIONS2D.fields_by_name['grid_type'].enum_type = _GRIDOPTIONS2D_GRIDTYPE
_GRIDOPTIONS2D_GRIDTYPE.containing_type = _GRIDOPTIONS2D
DESCRIPTOR.message_types_by_name['GridOptions2D'] = _GRIDOPTIONS2D
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GridOptions2D = _reflection.GeneratedProtocolMessageType('GridOptions2D', (_message.Message,), dict(
  DESCRIPTOR = _GRIDOPTIONS2D,
  __module__ = 'cartographer.mapping.proto.grid_2d_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.GridOptions2D)
  ))
_sym_db.RegisterMessage(GridOptions2D)


# @@protoc_insertion_point(module_scope)
