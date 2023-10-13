# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/mapping/proto/submap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cartographer.mapping.proto import grid_2d_pb2 as cartographer_dot_mapping_dot_proto_dot_grid__2d__pb2
from cartographer.mapping.proto import hybrid_grid_pb2 as cartographer_dot_mapping_dot_proto_dot_hybrid__grid__pb2
from cartographer.transform.proto import transform_pb2 as cartographer_dot_transform_dot_proto_dot_transform__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cartographer/mapping/proto/submap.proto',
  package='cartographer.mapping.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'cartographer/mapping/proto/submap.proto\x12\x1a\x63\x61rtographer.mapping.proto\x1a(cartographer/mapping/proto/grid_2d.proto\x1a,cartographer/mapping/proto/hybrid_grid.proto\x1a,cartographer/transform/proto/transform.proto\"\xa1\x01\n\x08Submap2D\x12\x39\n\nlocal_pose\x18\x01 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3d\x12\x16\n\x0enum_range_data\x18\x02 \x01(\x05\x12\x10\n\x08\x66inished\x18\x03 \x01(\x08\x12\x30\n\x04grid\x18\x04 \x01(\x0b\x32\".cartographer.mapping.proto.Grid2D\"\xb3\x02\n\x08Submap3D\x12\x39\n\nlocal_pose\x18\x01 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3d\x12\x16\n\x0enum_range_data\x18\x02 \x01(\x05\x12\x10\n\x08\x66inished\x18\x03 \x01(\x08\x12K\n\x1bhigh_resolution_hybrid_grid\x18\x04 \x01(\x0b\x32&.cartographer.mapping.proto.HybridGrid\x12J\n\x1alow_resolution_hybrid_grid\x18\x05 \x01(\x0b\x32&.cartographer.mapping.proto.HybridGrid\x12)\n!rotational_scan_matcher_histogram\x18\x06 \x03(\x02\x62\x06proto3')
  ,
  dependencies=[cartographer_dot_mapping_dot_proto_dot_grid__2d__pb2.DESCRIPTOR,cartographer_dot_mapping_dot_proto_dot_hybrid__grid__pb2.DESCRIPTOR,cartographer_dot_transform_dot_proto_dot_transform__pb2.DESCRIPTOR,])




_SUBMAP2D = _descriptor.Descriptor(
  name='Submap2D',
  full_name='cartographer.mapping.proto.Submap2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_pose', full_name='cartographer.mapping.proto.Submap2D.local_pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_range_data', full_name='cartographer.mapping.proto.Submap2D.num_range_data', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished', full_name='cartographer.mapping.proto.Submap2D.finished', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grid', full_name='cartographer.mapping.proto.Submap2D.grid', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=206,
  serialized_end=367,
)


_SUBMAP3D = _descriptor.Descriptor(
  name='Submap3D',
  full_name='cartographer.mapping.proto.Submap3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_pose', full_name='cartographer.mapping.proto.Submap3D.local_pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_range_data', full_name='cartographer.mapping.proto.Submap3D.num_range_data', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished', full_name='cartographer.mapping.proto.Submap3D.finished', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_resolution_hybrid_grid', full_name='cartographer.mapping.proto.Submap3D.high_resolution_hybrid_grid', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low_resolution_hybrid_grid', full_name='cartographer.mapping.proto.Submap3D.low_resolution_hybrid_grid', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotational_scan_matcher_histogram', full_name='cartographer.mapping.proto.Submap3D.rotational_scan_matcher_histogram', index=5,
      number=6, type=2, cpp_type=6, label=3,
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
  serialized_start=370,
  serialized_end=677,
)

_SUBMAP2D.fields_by_name['local_pose'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_SUBMAP2D.fields_by_name['grid'].message_type = cartographer_dot_mapping_dot_proto_dot_grid__2d__pb2._GRID2D
_SUBMAP3D.fields_by_name['local_pose'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_SUBMAP3D.fields_by_name['high_resolution_hybrid_grid'].message_type = cartographer_dot_mapping_dot_proto_dot_hybrid__grid__pb2._HYBRIDGRID
_SUBMAP3D.fields_by_name['low_resolution_hybrid_grid'].message_type = cartographer_dot_mapping_dot_proto_dot_hybrid__grid__pb2._HYBRIDGRID
DESCRIPTOR.message_types_by_name['Submap2D'] = _SUBMAP2D
DESCRIPTOR.message_types_by_name['Submap3D'] = _SUBMAP3D
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Submap2D = _reflection.GeneratedProtocolMessageType('Submap2D', (_message.Message,), dict(
  DESCRIPTOR = _SUBMAP2D,
  __module__ = 'cartographer.mapping.proto.submap_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.Submap2D)
  ))
_sym_db.RegisterMessage(Submap2D)

Submap3D = _reflection.GeneratedProtocolMessageType('Submap3D', (_message.Message,), dict(
  DESCRIPTOR = _SUBMAP3D,
  __module__ = 'cartographer.mapping.proto.submap_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.Submap3D)
  ))
_sym_db.RegisterMessage(Submap3D)


# @@protoc_insertion_point(module_scope)