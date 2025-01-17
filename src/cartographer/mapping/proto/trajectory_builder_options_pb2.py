# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/mapping/proto/trajectory_builder_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cartographer.transform.proto import transform_pb2 as cartographer_dot_transform_dot_proto_dot_transform__pb2
from cartographer.mapping.proto import motion_filter_options_pb2 as cartographer_dot_mapping_dot_proto_dot_motion__filter__options__pb2
from cartographer.mapping.proto import local_trajectory_builder_options_2d_pb2 as cartographer_dot_mapping_dot_proto_dot_local__trajectory__builder__options__2d__pb2
from cartographer.mapping.proto import local_trajectory_builder_options_3d_pb2 as cartographer_dot_mapping_dot_proto_dot_local__trajectory__builder__options__3d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cartographer/mapping/proto/trajectory_builder_options.proto',
  package='cartographer.mapping.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;cartographer/mapping/proto/trajectory_builder_options.proto\x12\x1a\x63\x61rtographer.mapping.proto\x1a,cartographer/transform/proto/transform.proto\x1a\x36\x63\x61rtographer/mapping/proto/motion_filter_options.proto\x1a\x44\x63\x61rtographer/mapping/proto/local_trajectory_builder_options_2d.proto\x1a\x44\x63\x61rtographer/mapping/proto/local_trajectory_builder_options_3d.proto\"\x82\x01\n\x15InitialTrajectoryPose\x12<\n\rrelative_pose\x18\x01 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3d\x12\x18\n\x10to_trajectory_id\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"\xa6\x05\n\x18TrajectoryBuilderOptions\x12\x62\n\x1dtrajectory_builder_2d_options\x18\x01 \x01(\x0b\x32;.cartographer.mapping.proto.LocalTrajectoryBuilderOptions2D\x12\x62\n\x1dtrajectory_builder_3d_options\x18\x02 \x01(\x0b\x32;.cartographer.mapping.proto.LocalTrajectoryBuilderOptions3D\x12R\n\x17initial_trajectory_pose\x18\x04 \x01(\x0b\x32\x31.cartographer.mapping.proto.InitialTrajectoryPose\x12\x1d\n\x11pure_localization\x18\x03 \x01(\x08\x42\x02\x18\x01\x12v\n\x19pure_localization_trimmer\x18\x06 \x01(\x0b\x32S.cartographer.mapping.proto.TrajectoryBuilderOptions.PureLocalizationTrimmerOptions\x12\x1b\n\x13\x63ollate_fixed_frame\x18\x07 \x01(\x08\x12\x19\n\x11\x63ollate_landmarks\x18\x08 \x01(\x08\x12Z\n!pose_graph_odometry_motion_filter\x18\t \x01(\x0b\x32/.cartographer.mapping.proto.MotionFilterOptions\x1a=\n\x1ePureLocalizationTrimmerOptions\x12\x1b\n\x13max_submaps_to_keep\x18\x01 \x01(\x05J\x04\x08\x05\x10\x06\"\xc0\x01\n\x08SensorId\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.cartographer.mapping.proto.SensorId.SensorType\x12\n\n\x02id\x18\x02 \x01(\t\"i\n\nSensorType\x12\t\n\x05RANGE\x10\x00\x12\x07\n\x03IMU\x10\x01\x12\x0c\n\x08ODOMETRY\x10\x02\x12\x14\n\x10\x46IXED_FRAME_POSE\x10\x03\x12\x0c\n\x08LANDMARK\x10\x04\x12\x15\n\x11LOCAL_SLAM_RESULT\x10\x05\"\xba\x01\n%TrajectoryBuilderOptionsWithSensorIds\x12\x37\n\tsensor_id\x18\x01 \x03(\x0b\x32$.cartographer.mapping.proto.SensorId\x12X\n\x1atrajectory_builder_options\x18\x02 \x01(\x0b\x32\x34.cartographer.mapping.proto.TrajectoryBuilderOptions\"\x81\x01\n\x1b\x41llTrajectoryBuilderOptions\x12\x62\n\x17options_with_sensor_ids\x18\x01 \x03(\x0b\x32\x41.cartographer.mapping.proto.TrajectoryBuilderOptionsWithSensorIdsb\x06proto3')
  ,
  dependencies=[cartographer_dot_transform_dot_proto_dot_transform__pb2.DESCRIPTOR,cartographer_dot_mapping_dot_proto_dot_motion__filter__options__pb2.DESCRIPTOR,cartographer_dot_mapping_dot_proto_dot_local__trajectory__builder__options__2d__pb2.DESCRIPTOR,cartographer_dot_mapping_dot_proto_dot_local__trajectory__builder__options__3d__pb2.DESCRIPTOR,])



_SENSORID_SENSORTYPE = _descriptor.EnumDescriptor(
  name='SensorType',
  full_name='cartographer.mapping.proto.SensorId.SensorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RANGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ODOMETRY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIXED_FRAME_POSE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LANDMARK', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL_SLAM_RESULT', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1235,
  serialized_end=1340,
)
_sym_db.RegisterEnumDescriptor(_SENSORID_SENSORTYPE)


_INITIALTRAJECTORYPOSE = _descriptor.Descriptor(
  name='InitialTrajectoryPose',
  full_name='cartographer.mapping.proto.InitialTrajectoryPose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relative_pose', full_name='cartographer.mapping.proto.InitialTrajectoryPose.relative_pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_trajectory_id', full_name='cartographer.mapping.proto.InitialTrajectoryPose.to_trajectory_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cartographer.mapping.proto.InitialTrajectoryPose.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=334,
  serialized_end=464,
)


_TRAJECTORYBUILDEROPTIONS_PURELOCALIZATIONTRIMMEROPTIONS = _descriptor.Descriptor(
  name='PureLocalizationTrimmerOptions',
  full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.PureLocalizationTrimmerOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_submaps_to_keep', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.PureLocalizationTrimmerOptions.max_submaps_to_keep', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1078,
  serialized_end=1139,
)

_TRAJECTORYBUILDEROPTIONS = _descriptor.Descriptor(
  name='TrajectoryBuilderOptions',
  full_name='cartographer.mapping.proto.TrajectoryBuilderOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trajectory_builder_2d_options', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.trajectory_builder_2d_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trajectory_builder_3d_options', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.trajectory_builder_3d_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_trajectory_pose', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.initial_trajectory_pose', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pure_localization', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.pure_localization', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pure_localization_trimmer', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.pure_localization_trimmer', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collate_fixed_frame', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.collate_fixed_frame', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collate_landmarks', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.collate_landmarks', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose_graph_odometry_motion_filter', full_name='cartographer.mapping.proto.TrajectoryBuilderOptions.pose_graph_odometry_motion_filter', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRAJECTORYBUILDEROPTIONS_PURELOCALIZATIONTRIMMEROPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=1145,
)


_SENSORID = _descriptor.Descriptor(
  name='SensorId',
  full_name='cartographer.mapping.proto.SensorId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='cartographer.mapping.proto.SensorId.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='cartographer.mapping.proto.SensorId.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SENSORID_SENSORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1148,
  serialized_end=1340,
)


_TRAJECTORYBUILDEROPTIONSWITHSENSORIDS = _descriptor.Descriptor(
  name='TrajectoryBuilderOptionsWithSensorIds',
  full_name='cartographer.mapping.proto.TrajectoryBuilderOptionsWithSensorIds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='cartographer.mapping.proto.TrajectoryBuilderOptionsWithSensorIds.sensor_id', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trajectory_builder_options', full_name='cartographer.mapping.proto.TrajectoryBuilderOptionsWithSensorIds.trajectory_builder_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1343,
  serialized_end=1529,
)


_ALLTRAJECTORYBUILDEROPTIONS = _descriptor.Descriptor(
  name='AllTrajectoryBuilderOptions',
  full_name='cartographer.mapping.proto.AllTrajectoryBuilderOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options_with_sensor_ids', full_name='cartographer.mapping.proto.AllTrajectoryBuilderOptions.options_with_sensor_ids', index=0,
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
  serialized_start=1532,
  serialized_end=1661,
)

_INITIALTRAJECTORYPOSE.fields_by_name['relative_pose'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_TRAJECTORYBUILDEROPTIONS_PURELOCALIZATIONTRIMMEROPTIONS.containing_type = _TRAJECTORYBUILDEROPTIONS
_TRAJECTORYBUILDEROPTIONS.fields_by_name['trajectory_builder_2d_options'].message_type = cartographer_dot_mapping_dot_proto_dot_local__trajectory__builder__options__2d__pb2._LOCALTRAJECTORYBUILDEROPTIONS2D
_TRAJECTORYBUILDEROPTIONS.fields_by_name['trajectory_builder_3d_options'].message_type = cartographer_dot_mapping_dot_proto_dot_local__trajectory__builder__options__3d__pb2._LOCALTRAJECTORYBUILDEROPTIONS3D
_TRAJECTORYBUILDEROPTIONS.fields_by_name['initial_trajectory_pose'].message_type = _INITIALTRAJECTORYPOSE
_TRAJECTORYBUILDEROPTIONS.fields_by_name['pure_localization_trimmer'].message_type = _TRAJECTORYBUILDEROPTIONS_PURELOCALIZATIONTRIMMEROPTIONS
_TRAJECTORYBUILDEROPTIONS.fields_by_name['pose_graph_odometry_motion_filter'].message_type = cartographer_dot_mapping_dot_proto_dot_motion__filter__options__pb2._MOTIONFILTEROPTIONS
_SENSORID.fields_by_name['type'].enum_type = _SENSORID_SENSORTYPE
_SENSORID_SENSORTYPE.containing_type = _SENSORID
_TRAJECTORYBUILDEROPTIONSWITHSENSORIDS.fields_by_name['sensor_id'].message_type = _SENSORID
_TRAJECTORYBUILDEROPTIONSWITHSENSORIDS.fields_by_name['trajectory_builder_options'].message_type = _TRAJECTORYBUILDEROPTIONS
_ALLTRAJECTORYBUILDEROPTIONS.fields_by_name['options_with_sensor_ids'].message_type = _TRAJECTORYBUILDEROPTIONSWITHSENSORIDS
DESCRIPTOR.message_types_by_name['InitialTrajectoryPose'] = _INITIALTRAJECTORYPOSE
DESCRIPTOR.message_types_by_name['TrajectoryBuilderOptions'] = _TRAJECTORYBUILDEROPTIONS
DESCRIPTOR.message_types_by_name['SensorId'] = _SENSORID
DESCRIPTOR.message_types_by_name['TrajectoryBuilderOptionsWithSensorIds'] = _TRAJECTORYBUILDEROPTIONSWITHSENSORIDS
DESCRIPTOR.message_types_by_name['AllTrajectoryBuilderOptions'] = _ALLTRAJECTORYBUILDEROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitialTrajectoryPose = _reflection.GeneratedProtocolMessageType('InitialTrajectoryPose', (_message.Message,), dict(
  DESCRIPTOR = _INITIALTRAJECTORYPOSE,
  __module__ = 'cartographer.mapping.proto.trajectory_builder_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.InitialTrajectoryPose)
  ))
_sym_db.RegisterMessage(InitialTrajectoryPose)

TrajectoryBuilderOptions = _reflection.GeneratedProtocolMessageType('TrajectoryBuilderOptions', (_message.Message,), dict(

  PureLocalizationTrimmerOptions = _reflection.GeneratedProtocolMessageType('PureLocalizationTrimmerOptions', (_message.Message,), dict(
    DESCRIPTOR = _TRAJECTORYBUILDEROPTIONS_PURELOCALIZATIONTRIMMEROPTIONS,
    __module__ = 'cartographer.mapping.proto.trajectory_builder_options_pb2'
    # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.TrajectoryBuilderOptions.PureLocalizationTrimmerOptions)
    ))
  ,
  DESCRIPTOR = _TRAJECTORYBUILDEROPTIONS,
  __module__ = 'cartographer.mapping.proto.trajectory_builder_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.TrajectoryBuilderOptions)
  ))
_sym_db.RegisterMessage(TrajectoryBuilderOptions)
_sym_db.RegisterMessage(TrajectoryBuilderOptions.PureLocalizationTrimmerOptions)

SensorId = _reflection.GeneratedProtocolMessageType('SensorId', (_message.Message,), dict(
  DESCRIPTOR = _SENSORID,
  __module__ = 'cartographer.mapping.proto.trajectory_builder_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.SensorId)
  ))
_sym_db.RegisterMessage(SensorId)

TrajectoryBuilderOptionsWithSensorIds = _reflection.GeneratedProtocolMessageType('TrajectoryBuilderOptionsWithSensorIds', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORYBUILDEROPTIONSWITHSENSORIDS,
  __module__ = 'cartographer.mapping.proto.trajectory_builder_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.TrajectoryBuilderOptionsWithSensorIds)
  ))
_sym_db.RegisterMessage(TrajectoryBuilderOptionsWithSensorIds)

AllTrajectoryBuilderOptions = _reflection.GeneratedProtocolMessageType('AllTrajectoryBuilderOptions', (_message.Message,), dict(
  DESCRIPTOR = _ALLTRAJECTORYBUILDEROPTIONS,
  __module__ = 'cartographer.mapping.proto.trajectory_builder_options_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.mapping.proto.AllTrajectoryBuilderOptions)
  ))
_sym_db.RegisterMessage(AllTrajectoryBuilderOptions)


_TRAJECTORYBUILDEROPTIONS.fields_by_name['pure_localization']._options = None
# @@protoc_insertion_point(module_scope)
