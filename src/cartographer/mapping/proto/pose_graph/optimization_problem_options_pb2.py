# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/mapping/proto/pose_graph/optimization_problem_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cartographer.common.proto import ceres_solver_options_pb2 as cartographer_dot_common_dot_proto_dot_ceres__solver__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cartographer/mapping/proto/pose_graph/optimization_problem_options.proto',
  package='cartographer.mapping.optimization.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nHcartographer/mapping/proto/pose_graph/optimization_problem_options.proto\x12\'cartographer.mapping.optimization.proto\x1a\x34\x63\x61rtographer/common/proto/ceres_solver_options.proto\"\x93\x05\n\x1aOptimizationProblemOptions\x12\x13\n\x0bhuber_scale\x18\x01 \x01(\x01\x12\x1b\n\x13\x61\x63\x63\x65leration_weight\x18\x08 \x01(\x01\x12\x17\n\x0frotation_weight\x18\t \x01(\x01\x12*\n\"local_slam_pose_translation_weight\x18\x0e \x01(\x01\x12\'\n\x1flocal_slam_pose_rotation_weight\x18\x0f \x01(\x01\x12#\n\x1bodometry_translation_weight\x18\x10 \x01(\x01\x12 \n\x18odometry_rotation_weight\x18\x11 \x01(\x01\x12+\n#fixed_frame_pose_translation_weight\x18\x0b \x01(\x01\x12(\n fixed_frame_pose_rotation_weight\x18\x0c \x01(\x01\x12*\n\"fixed_frame_pose_use_tolerant_loss\x18\x17 \x01(\x08\x12.\n&fixed_frame_pose_tolerant_loss_param_a\x18\x18 \x01(\x01\x12.\n&fixed_frame_pose_tolerant_loss_param_b\x18\x19 \x01(\x01\x12\x13\n\x0b\x66ix_z_in_3d\x18\r \x01(\x08\x12\'\n\x1fuse_online_imu_extrinsics_in_3d\x18\x12 \x01(\x08\x12\x1a\n\x12log_solver_summary\x18\x05 \x01(\x08\x12K\n\x14\x63\x65res_solver_options\x18\x07 \x01(\x0b\x32-.cartographer.common.proto.CeresSolverOptionsJ\x04\x08\x14\x10\x17\x62\x06proto3')
  ,
  dependencies=[cartographer_dot_common_dot_proto_dot_ceres__solver__options__pb2.DESCRIPTOR,])




_OPTIMIZATIONPROBLEMOPTIONS = _descriptor.Descriptor(
  name='OptimizationProblemOptions',
  full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='huber_scale', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.huber_scale', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration_weight', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.acceleration_weight', index=1,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation_weight', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.rotation_weight', index=2,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_slam_pose_translation_weight', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.local_slam_pose_translation_weight', index=3,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_slam_pose_rotation_weight', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.local_slam_pose_rotation_weight', index=4,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='odometry_translation_weight', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.odometry_translation_weight', index=5,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='odometry_rotation_weight', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.odometry_rotation_weight', index=6,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_frame_pose_translation_weight', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.fixed_frame_pose_translation_weight', index=7,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_frame_pose_rotation_weight', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.fixed_frame_pose_rotation_weight', index=8,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_frame_pose_use_tolerant_loss', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.fixed_frame_pose_use_tolerant_loss', index=9,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_frame_pose_tolerant_loss_param_a', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.fixed_frame_pose_tolerant_loss_param_a', index=10,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_frame_pose_tolerant_loss_param_b', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.fixed_frame_pose_tolerant_loss_param_b', index=11,
      number=25, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fix_z_in_3d', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.fix_z_in_3d', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_online_imu_extrinsics_in_3d', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.use_online_imu_extrinsics_in_3d', index=13,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_solver_summary', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.log_solver_summary', index=14,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ceres_solver_options', full_name='cartographer.mapping.optimization.proto.OptimizationProblemOptions.ceres_solver_options', index=15,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=172,
  serialized_end=831,
)

_OPTIMIZATIONPROBLEMOPTIONS.fields_by_name['ceres_solver_options'].message_type = cartographer_dot_common_dot_proto_dot_ceres__solver__options__pb2._CERESSOLVEROPTIONS
DESCRIPTOR.message_types_by_name['OptimizationProblemOptions'] = _OPTIMIZATIONPROBLEMOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OptimizationProblemOptions = _reflection.GeneratedProtocolMessageType('OptimizationProblemOptions', (_message.Message,), dict(
  DESCRIPTOR = _OPTIMIZATIONPROBLEMOPTIONS,
  __module__ = 'cartographer.mapping.proto.pose_graph.optimization_problem_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.optimization.proto.OptimizationProblemOptions)
  ))
_sym_db.RegisterMessage(OptimizationProblemOptions)


# @@protoc_insertion_point(module_scope)
