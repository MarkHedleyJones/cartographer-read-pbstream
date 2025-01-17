# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/mapping/proto/pose_graph_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cartographer.mapping.proto.pose_graph import constraint_builder_options_pb2 as cartographer_dot_mapping_dot_proto_dot_pose__graph_dot_constraint__builder__options__pb2
from cartographer.mapping.proto.pose_graph import optimization_problem_options_pb2 as cartographer_dot_mapping_dot_proto_dot_pose__graph_dot_optimization__problem__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cartographer/mapping/proto/pose_graph_options.proto',
  package='cartographer.mapping.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3cartographer/mapping/proto/pose_graph_options.proto\x12\x1a\x63\x61rtographer.mapping.proto\x1a\x46\x63\x61rtographer/mapping/proto/pose_graph/constraint_builder_options.proto\x1aHcartographer/mapping/proto/pose_graph/optimization_problem_options.proto\"\xd3\x05\n\x10PoseGraphOptions\x12\x1e\n\x16optimize_every_n_nodes\x18\x01 \x01(\x05\x12\x64\n\x1a\x63onstraint_builder_options\x18\x03 \x01(\x0b\x32@.cartographer.mapping.constraints.proto.ConstraintBuilderOptions\x12\"\n\x1amatcher_translation_weight\x18\x07 \x01(\x01\x12\x1f\n\x17matcher_rotation_weight\x18\x08 \x01(\x01\x12i\n\x1coptimization_problem_options\x18\x04 \x01(\x0b\x32\x43.cartographer.mapping.optimization.proto.OptimizationProblemOptions\x12 \n\x18max_num_final_iterations\x18\x06 \x01(\x05\x12\x1d\n\x15global_sampling_ratio\x18\x05 \x01(\x01\x12\x1f\n\x17log_residual_histograms\x18\t \x01(\x08\x12\x30\n(global_constraint_search_after_n_seconds\x18\n \x01(\x01\x12w\n\x1eoverlapping_submaps_trimmer_2d\x18\x0b \x01(\x0b\x32O.cartographer.mapping.proto.PoseGraphOptions.OverlappingSubmapsTrimmerOptions2D\x1a|\n\"OverlappingSubmapsTrimmerOptions2D\x12\x1b\n\x13\x66resh_submaps_count\x18\x01 \x01(\x05\x12\x18\n\x10min_covered_area\x18\x02 \x01(\x01\x12\x1f\n\x17min_added_submaps_count\x18\x03 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[cartographer_dot_mapping_dot_proto_dot_pose__graph_dot_constraint__builder__options__pb2.DESCRIPTOR,cartographer_dot_mapping_dot_proto_dot_pose__graph_dot_optimization__problem__options__pb2.DESCRIPTOR,])




_POSEGRAPHOPTIONS_OVERLAPPINGSUBMAPSTRIMMEROPTIONS2D = _descriptor.Descriptor(
  name='OverlappingSubmapsTrimmerOptions2D',
  full_name='cartographer.mapping.proto.PoseGraphOptions.OverlappingSubmapsTrimmerOptions2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fresh_submaps_count', full_name='cartographer.mapping.proto.PoseGraphOptions.OverlappingSubmapsTrimmerOptions2D.fresh_submaps_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_covered_area', full_name='cartographer.mapping.proto.PoseGraphOptions.OverlappingSubmapsTrimmerOptions2D.min_covered_area', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_added_submaps_count', full_name='cartographer.mapping.proto.PoseGraphOptions.OverlappingSubmapsTrimmerOptions2D.min_added_submaps_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=829,
  serialized_end=953,
)

_POSEGRAPHOPTIONS = _descriptor.Descriptor(
  name='PoseGraphOptions',
  full_name='cartographer.mapping.proto.PoseGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optimize_every_n_nodes', full_name='cartographer.mapping.proto.PoseGraphOptions.optimize_every_n_nodes', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constraint_builder_options', full_name='cartographer.mapping.proto.PoseGraphOptions.constraint_builder_options', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='matcher_translation_weight', full_name='cartographer.mapping.proto.PoseGraphOptions.matcher_translation_weight', index=2,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='matcher_rotation_weight', full_name='cartographer.mapping.proto.PoseGraphOptions.matcher_rotation_weight', index=3,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimization_problem_options', full_name='cartographer.mapping.proto.PoseGraphOptions.optimization_problem_options', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_num_final_iterations', full_name='cartographer.mapping.proto.PoseGraphOptions.max_num_final_iterations', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_sampling_ratio', full_name='cartographer.mapping.proto.PoseGraphOptions.global_sampling_ratio', index=6,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_residual_histograms', full_name='cartographer.mapping.proto.PoseGraphOptions.log_residual_histograms', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_constraint_search_after_n_seconds', full_name='cartographer.mapping.proto.PoseGraphOptions.global_constraint_search_after_n_seconds', index=8,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlapping_submaps_trimmer_2d', full_name='cartographer.mapping.proto.PoseGraphOptions.overlapping_submaps_trimmer_2d', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POSEGRAPHOPTIONS_OVERLAPPINGSUBMAPSTRIMMEROPTIONS2D, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=953,
)

_POSEGRAPHOPTIONS_OVERLAPPINGSUBMAPSTRIMMEROPTIONS2D.containing_type = _POSEGRAPHOPTIONS
_POSEGRAPHOPTIONS.fields_by_name['constraint_builder_options'].message_type = cartographer_dot_mapping_dot_proto_dot_pose__graph_dot_constraint__builder__options__pb2._CONSTRAINTBUILDEROPTIONS
_POSEGRAPHOPTIONS.fields_by_name['optimization_problem_options'].message_type = cartographer_dot_mapping_dot_proto_dot_pose__graph_dot_optimization__problem__options__pb2._OPTIMIZATIONPROBLEMOPTIONS
_POSEGRAPHOPTIONS.fields_by_name['overlapping_submaps_trimmer_2d'].message_type = _POSEGRAPHOPTIONS_OVERLAPPINGSUBMAPSTRIMMEROPTIONS2D
DESCRIPTOR.message_types_by_name['PoseGraphOptions'] = _POSEGRAPHOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PoseGraphOptions = _reflection.GeneratedProtocolMessageType('PoseGraphOptions', (_message.Message,), dict(

  OverlappingSubmapsTrimmerOptions2D = _reflection.GeneratedProtocolMessageType('OverlappingSubmapsTrimmerOptions2D', (_message.Message,), dict(
    DESCRIPTOR = _POSEGRAPHOPTIONS_OVERLAPPINGSUBMAPSTRIMMEROPTIONS2D,
    __module__ = 'cartographer.mapping.proto.pose_graph_options_pb2'
    # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.PoseGraphOptions.OverlappingSubmapsTrimmerOptions2D)
    ))
  ,
  DESCRIPTOR = _POSEGRAPHOPTIONS,
  __module__ = 'cartographer.mapping.proto.pose_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.PoseGraphOptions)
  ))
_sym_db.RegisterMessage(PoseGraphOptions)
_sym_db.RegisterMessage(PoseGraphOptions.OverlappingSubmapsTrimmerOptions2D)


# @@protoc_insertion_point(module_scope)
