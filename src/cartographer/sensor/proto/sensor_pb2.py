# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartographer/sensor/proto/sensor.proto

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
  name='cartographer/sensor/proto/sensor.proto',
  package='cartographer.sensor.proto',
  syntax='proto3',
  serialized_options=_b('B\006Sensor'),
  serialized_pb=_b('\n&cartographer/sensor/proto/sensor.proto\x12\x19\x63\x61rtographer.sensor.proto\x1a,cartographer/transform/proto/transform.proto\"L\n\x10RangefinderPoint\x12\x38\n\x08position\x18\x01 \x01(\x0b\x32&.cartographer.transform.proto.Vector3f\"_\n\x15TimedRangefinderPoint\x12\x38\n\x08position\x18\x01 \x01(\x0b\x32&.cartographer.transform.proto.Vector3f\x12\x0c\n\x04time\x18\x02 \x01(\x02\">\n\x14\x43ompressedPointCloud\x12\x12\n\nnum_points\x18\x01 \x01(\x05\x12\x12\n\npoint_data\x18\x03 \x03(\x05\"\xfe\x01\n\x13TimedPointCloudData\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x36\n\x06origin\x18\x02 \x01(\x0b\x32&.cartographer.transform.proto.Vector3f\x12\x41\n\x11point_data_legacy\x18\x03 \x03(\x0b\x32&.cartographer.transform.proto.Vector4f\x12\x44\n\npoint_data\x18\x04 \x03(\x0b\x32\x30.cartographer.sensor.proto.TimedRangefinderPoint\x12\x13\n\x0bintensities\x18\x05 \x03(\x02\"\xbd\x02\n\tRangeData\x12\x36\n\x06origin\x18\x01 \x01(\x0b\x32&.cartographer.transform.proto.Vector3f\x12>\n\x0ereturns_legacy\x18\x02 \x03(\x0b\x32&.cartographer.transform.proto.Vector3f\x12=\n\rmisses_legacy\x18\x03 \x03(\x0b\x32&.cartographer.transform.proto.Vector3f\x12<\n\x07returns\x18\x04 \x03(\x0b\x32+.cartographer.sensor.proto.RangefinderPoint\x12;\n\x06misses\x18\x05 \x03(\x0b\x32+.cartographer.sensor.proto.RangefinderPoint\"\xa3\x01\n\x07ImuData\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x43\n\x13linear_acceleration\x18\x02 \x01(\x0b\x32&.cartographer.transform.proto.Vector3d\x12@\n\x10\x61ngular_velocity\x18\x03 \x01(\x0b\x32&.cartographer.transform.proto.Vector3d\"V\n\x0cOdometryData\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x33\n\x04pose\x18\x02 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3d\"\\\n\x12\x46ixedFramePoseData\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x33\n\x04pose\x18\x02 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3d\"\xa5\x02\n\x0cLandmarkData\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12Z\n\x15landmark_observations\x18\x02 \x03(\x0b\x32;.cartographer.sensor.proto.LandmarkData.LandmarkObservation\x1a\xa5\x01\n\x13LandmarkObservation\x12\n\n\x02id\x18\x01 \x01(\x0c\x12M\n\x1elandmark_to_tracking_transform\x18\x02 \x01(\x0b\x32%.cartographer.transform.proto.Rigid3d\x12\x1a\n\x12translation_weight\x18\x03 \x01(\x01\x12\x17\n\x0frotation_weight\x18\x04 \x01(\x01\x42\x08\x42\x06Sensorb\x06proto3')
  ,
  dependencies=[cartographer_dot_transform_dot_proto_dot_transform__pb2.DESCRIPTOR,])




_RANGEFINDERPOINT = _descriptor.Descriptor(
  name='RangefinderPoint',
  full_name='cartographer.sensor.proto.RangefinderPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='cartographer.sensor.proto.RangefinderPoint.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=115,
  serialized_end=191,
)


_TIMEDRANGEFINDERPOINT = _descriptor.Descriptor(
  name='TimedRangefinderPoint',
  full_name='cartographer.sensor.proto.TimedRangefinderPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='cartographer.sensor.proto.TimedRangefinderPoint.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='cartographer.sensor.proto.TimedRangefinderPoint.time', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=288,
)


_COMPRESSEDPOINTCLOUD = _descriptor.Descriptor(
  name='CompressedPointCloud',
  full_name='cartographer.sensor.proto.CompressedPointCloud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_points', full_name='cartographer.sensor.proto.CompressedPointCloud.num_points', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_data', full_name='cartographer.sensor.proto.CompressedPointCloud.point_data', index=1,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=290,
  serialized_end=352,
)


_TIMEDPOINTCLOUDDATA = _descriptor.Descriptor(
  name='TimedPointCloudData',
  full_name='cartographer.sensor.proto.TimedPointCloudData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cartographer.sensor.proto.TimedPointCloudData.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='cartographer.sensor.proto.TimedPointCloudData.origin', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_data_legacy', full_name='cartographer.sensor.proto.TimedPointCloudData.point_data_legacy', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_data', full_name='cartographer.sensor.proto.TimedPointCloudData.point_data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intensities', full_name='cartographer.sensor.proto.TimedPointCloudData.intensities', index=4,
      number=5, type=2, cpp_type=6, label=3,
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
  serialized_start=355,
  serialized_end=609,
)


_RANGEDATA = _descriptor.Descriptor(
  name='RangeData',
  full_name='cartographer.sensor.proto.RangeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='cartographer.sensor.proto.RangeData.origin', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returns_legacy', full_name='cartographer.sensor.proto.RangeData.returns_legacy', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='misses_legacy', full_name='cartographer.sensor.proto.RangeData.misses_legacy', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returns', full_name='cartographer.sensor.proto.RangeData.returns', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='misses', full_name='cartographer.sensor.proto.RangeData.misses', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=612,
  serialized_end=929,
)


_IMUDATA = _descriptor.Descriptor(
  name='ImuData',
  full_name='cartographer.sensor.proto.ImuData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cartographer.sensor.proto.ImuData.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='cartographer.sensor.proto.ImuData.linear_acceleration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='cartographer.sensor.proto.ImuData.angular_velocity', index=2,
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
  serialized_start=932,
  serialized_end=1095,
)


_ODOMETRYDATA = _descriptor.Descriptor(
  name='OdometryData',
  full_name='cartographer.sensor.proto.OdometryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cartographer.sensor.proto.OdometryData.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose', full_name='cartographer.sensor.proto.OdometryData.pose', index=1,
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
  serialized_start=1097,
  serialized_end=1183,
)


_FIXEDFRAMEPOSEDATA = _descriptor.Descriptor(
  name='FixedFramePoseData',
  full_name='cartographer.sensor.proto.FixedFramePoseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cartographer.sensor.proto.FixedFramePoseData.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose', full_name='cartographer.sensor.proto.FixedFramePoseData.pose', index=1,
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
  serialized_start=1185,
  serialized_end=1277,
)


_LANDMARKDATA_LANDMARKOBSERVATION = _descriptor.Descriptor(
  name='LandmarkObservation',
  full_name='cartographer.sensor.proto.LandmarkData.LandmarkObservation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cartographer.sensor.proto.LandmarkData.LandmarkObservation.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_to_tracking_transform', full_name='cartographer.sensor.proto.LandmarkData.LandmarkObservation.landmark_to_tracking_transform', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='translation_weight', full_name='cartographer.sensor.proto.LandmarkData.LandmarkObservation.translation_weight', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation_weight', full_name='cartographer.sensor.proto.LandmarkData.LandmarkObservation.rotation_weight', index=3,
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
  serialized_start=1408,
  serialized_end=1573,
)

_LANDMARKDATA = _descriptor.Descriptor(
  name='LandmarkData',
  full_name='cartographer.sensor.proto.LandmarkData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cartographer.sensor.proto.LandmarkData.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_observations', full_name='cartographer.sensor.proto.LandmarkData.landmark_observations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LANDMARKDATA_LANDMARKOBSERVATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1280,
  serialized_end=1573,
)

_RANGEFINDERPOINT.fields_by_name['position'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR3F
_TIMEDRANGEFINDERPOINT.fields_by_name['position'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR3F
_TIMEDPOINTCLOUDDATA.fields_by_name['origin'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR3F
_TIMEDPOINTCLOUDDATA.fields_by_name['point_data_legacy'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR4F
_TIMEDPOINTCLOUDDATA.fields_by_name['point_data'].message_type = _TIMEDRANGEFINDERPOINT
_RANGEDATA.fields_by_name['origin'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR3F
_RANGEDATA.fields_by_name['returns_legacy'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR3F
_RANGEDATA.fields_by_name['misses_legacy'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR3F
_RANGEDATA.fields_by_name['returns'].message_type = _RANGEFINDERPOINT
_RANGEDATA.fields_by_name['misses'].message_type = _RANGEFINDERPOINT
_IMUDATA.fields_by_name['linear_acceleration'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR3D
_IMUDATA.fields_by_name['angular_velocity'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._VECTOR3D
_ODOMETRYDATA.fields_by_name['pose'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_FIXEDFRAMEPOSEDATA.fields_by_name['pose'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_LANDMARKDATA_LANDMARKOBSERVATION.fields_by_name['landmark_to_tracking_transform'].message_type = cartographer_dot_transform_dot_proto_dot_transform__pb2._RIGID3D
_LANDMARKDATA_LANDMARKOBSERVATION.containing_type = _LANDMARKDATA
_LANDMARKDATA.fields_by_name['landmark_observations'].message_type = _LANDMARKDATA_LANDMARKOBSERVATION
DESCRIPTOR.message_types_by_name['RangefinderPoint'] = _RANGEFINDERPOINT
DESCRIPTOR.message_types_by_name['TimedRangefinderPoint'] = _TIMEDRANGEFINDERPOINT
DESCRIPTOR.message_types_by_name['CompressedPointCloud'] = _COMPRESSEDPOINTCLOUD
DESCRIPTOR.message_types_by_name['TimedPointCloudData'] = _TIMEDPOINTCLOUDDATA
DESCRIPTOR.message_types_by_name['RangeData'] = _RANGEDATA
DESCRIPTOR.message_types_by_name['ImuData'] = _IMUDATA
DESCRIPTOR.message_types_by_name['OdometryData'] = _ODOMETRYDATA
DESCRIPTOR.message_types_by_name['FixedFramePoseData'] = _FIXEDFRAMEPOSEDATA
DESCRIPTOR.message_types_by_name['LandmarkData'] = _LANDMARKDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RangefinderPoint = _reflection.GeneratedProtocolMessageType('RangefinderPoint', (_message.Message,), dict(
  DESCRIPTOR = _RANGEFINDERPOINT,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.RangefinderPoint)
  ))
_sym_db.RegisterMessage(RangefinderPoint)

TimedRangefinderPoint = _reflection.GeneratedProtocolMessageType('TimedRangefinderPoint', (_message.Message,), dict(
  DESCRIPTOR = _TIMEDRANGEFINDERPOINT,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.TimedRangefinderPoint)
  ))
_sym_db.RegisterMessage(TimedRangefinderPoint)

CompressedPointCloud = _reflection.GeneratedProtocolMessageType('CompressedPointCloud', (_message.Message,), dict(
  DESCRIPTOR = _COMPRESSEDPOINTCLOUD,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.CompressedPointCloud)
  ))
_sym_db.RegisterMessage(CompressedPointCloud)

TimedPointCloudData = _reflection.GeneratedProtocolMessageType('TimedPointCloudData', (_message.Message,), dict(
  DESCRIPTOR = _TIMEDPOINTCLOUDDATA,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.TimedPointCloudData)
  ))
_sym_db.RegisterMessage(TimedPointCloudData)

RangeData = _reflection.GeneratedProtocolMessageType('RangeData', (_message.Message,), dict(
  DESCRIPTOR = _RANGEDATA,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.RangeData)
  ))
_sym_db.RegisterMessage(RangeData)

ImuData = _reflection.GeneratedProtocolMessageType('ImuData', (_message.Message,), dict(
  DESCRIPTOR = _IMUDATA,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.ImuData)
  ))
_sym_db.RegisterMessage(ImuData)

OdometryData = _reflection.GeneratedProtocolMessageType('OdometryData', (_message.Message,), dict(
  DESCRIPTOR = _ODOMETRYDATA,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.OdometryData)
  ))
_sym_db.RegisterMessage(OdometryData)

FixedFramePoseData = _reflection.GeneratedProtocolMessageType('FixedFramePoseData', (_message.Message,), dict(
  DESCRIPTOR = _FIXEDFRAMEPOSEDATA,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.FixedFramePoseData)
  ))
_sym_db.RegisterMessage(FixedFramePoseData)

LandmarkData = _reflection.GeneratedProtocolMessageType('LandmarkData', (_message.Message,), dict(

  LandmarkObservation = _reflection.GeneratedProtocolMessageType('LandmarkObservation', (_message.Message,), dict(
    DESCRIPTOR = _LANDMARKDATA_LANDMARKOBSERVATION,
    __module__ = 'cartographer.sensor.proto.sensor_pb2'
    # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.LandmarkData.LandmarkObservation)
    ))
  ,
  DESCRIPTOR = _LANDMARKDATA,
  __module__ = 'cartographer.sensor.proto.sensor_pb2'
  # @@protoc_insertion_point(class_scope:cartographer.sensor.proto.LandmarkData)
  ))
_sym_db.RegisterMessage(LandmarkData)
_sym_db.RegisterMessage(LandmarkData.LandmarkObservation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)