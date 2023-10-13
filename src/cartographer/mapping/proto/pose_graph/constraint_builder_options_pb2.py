# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/mapping/proto/pose_graph/constraint_builder_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cartographer.mapping.proto.scan_matching import ceres_scan_matcher_options_2d_pb2 as cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_ceres__scan__matcher__options__2d__pb2
from cartographer.mapping.proto.scan_matching import ceres_scan_matcher_options_3d_pb2 as cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_ceres__scan__matcher__options__3d__pb2
from cartographer.mapping.proto.scan_matching import fast_correlative_scan_matcher_options_2d_pb2 as cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_fast__correlative__scan__matcher__options__2d__pb2
from cartographer.mapping.proto.scan_matching import fast_correlative_scan_matcher_options_3d_pb2 as cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_fast__correlative__scan__matcher__options__3d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cartographer/mapping/proto/pose_graph/constraint_builder_options.proto',
  package='cartographer.mapping.constraints.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFcartographer/mapping/proto/pose_graph/constraint_builder_options.proto\x12&cartographer.mapping.constraints.proto\x1aLcartographer/mapping/proto/scan_matching/ceres_scan_matcher_options_2d.proto\x1aLcartographer/mapping/proto/scan_matching/ceres_scan_matcher_options_3d.proto\x1aWcartographer/mapping/proto/scan_matching/fast_correlative_scan_matcher_options_2d.proto\x1aWcartographer/mapping/proto/scan_matching/fast_correlative_scan_matcher_options_3d.proto\"\xc5\x05\n\x18\x43onstraintBuilderOptions\x12\x16\n\x0esampling_ratio\x18\x01 \x01(\x01\x12\x1f\n\x17max_constraint_distance\x18\x02 \x01(\x01\x12\x11\n\tmin_score\x18\x04 \x01(\x01\x12%\n\x1dglobal_localization_min_score\x18\x05 \x01(\x01\x12\'\n\x1floop_closure_translation_weight\x18\r \x01(\x01\x12$\n\x1cloop_closure_rotation_weight\x18\x0e \x01(\x01\x12\x13\n\x0blog_matches\x18\x08 \x01(\x08\x12|\n%fast_correlative_scan_matcher_options\x18\t \x01(\x0b\x32M.cartographer.mapping.scan_matching.proto.FastCorrelativeScanMatcherOptions2D\x12g\n\x1a\x63\x65res_scan_matcher_options\x18\x0b \x01(\x0b\x32\x43.cartographer.mapping.scan_matching.proto.CeresScanMatcherOptions2D\x12\x7f\n(fast_correlative_scan_matcher_options_3d\x18\n \x01(\x0b\x32M.cartographer.mapping.scan_matching.proto.FastCorrelativeScanMatcherOptions3D\x12j\n\x1d\x63\x65res_scan_matcher_options_3d\x18\x0c \x01(\x0b\x32\x43.cartographer.mapping.scan_matching.proto.CeresScanMatcherOptions3Db\x06proto3')
  ,
  dependencies=[cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_ceres__scan__matcher__options__2d__pb2.DESCRIPTOR,cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_ceres__scan__matcher__options__3d__pb2.DESCRIPTOR,cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_fast__correlative__scan__matcher__options__2d__pb2.DESCRIPTOR,cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_fast__correlative__scan__matcher__options__3d__pb2.DESCRIPTOR,])




_CONSTRAINTBUILDEROPTIONS = _descriptor.Descriptor(
  name='ConstraintBuilderOptions',
  full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sampling_ratio', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.sampling_ratio', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_constraint_distance', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.max_constraint_distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_score', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.min_score', index=2,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_localization_min_score', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.global_localization_min_score', index=3,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loop_closure_translation_weight', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.loop_closure_translation_weight', index=4,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loop_closure_rotation_weight', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.loop_closure_rotation_weight', index=5,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_matches', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.log_matches', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fast_correlative_scan_matcher_options', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.fast_correlative_scan_matcher_options', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ceres_scan_matcher_options', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.ceres_scan_matcher_options', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fast_correlative_scan_matcher_options_3d', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.fast_correlative_scan_matcher_options_3d', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ceres_scan_matcher_options_3d', full_name='cartographer.mapping.constraints.proto.ConstraintBuilderOptions.ceres_scan_matcher_options_3d', index=10,
      number=12, type=11, cpp_type=10, label=1,
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
  serialized_start=449,
  serialized_end=1158,
)

_CONSTRAINTBUILDEROPTIONS.fields_by_name['fast_correlative_scan_matcher_options'].message_type = cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_fast__correlative__scan__matcher__options__2d__pb2._FASTCORRELATIVESCANMATCHEROPTIONS2D
_CONSTRAINTBUILDEROPTIONS.fields_by_name['ceres_scan_matcher_options'].message_type = cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_ceres__scan__matcher__options__2d__pb2._CERESSCANMATCHEROPTIONS2D
_CONSTRAINTBUILDEROPTIONS.fields_by_name['fast_correlative_scan_matcher_options_3d'].message_type = cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_fast__correlative__scan__matcher__options__3d__pb2._FASTCORRELATIVESCANMATCHEROPTIONS3D
_CONSTRAINTBUILDEROPTIONS.fields_by_name['ceres_scan_matcher_options_3d'].message_type = cartographer_dot_mapping_dot_proto_dot_scan__matching_dot_ceres__scan__matcher__options__3d__pb2._CERESSCANMATCHEROPTIONS3D
DESCRIPTOR.message_types_by_name['ConstraintBuilderOptions'] = _CONSTRAINTBUILDEROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConstraintBuilderOptions = _reflection.GeneratedProtocolMessageType('ConstraintBuilderOptions', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRAINTBUILDEROPTIONS,
  __module__ = 'cartographer.mapping.proto.pose_graph.constraint_builder_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.constraints.proto.ConstraintBuilderOptions)
  ))
_sym_db.RegisterMessage(ConstraintBuilderOptions)


# @@protoc_insertion_point(module_scope)