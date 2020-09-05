# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommend.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='recommend.proto',
  package='recommend',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0frecommend.proto\x12\trecommend\"\xa0\x01\n\x07userReq\x12\x10\n\x08ug_level\x18\x01 \x01(\t\x12\x10\n\x08ug_major\x18\x02 \x01(\t\x12\x18\n\x10intended_country\x18\x03 \x01(\t\x12\x0e\n\x06ug_gpa\x18\x04 \x01(\x02\x12\x0b\n\x03gre\x18\x05 \x01(\x02\x12\x0c\n\x04gmat\x18\x06 \x01(\x02\x12\r\n\x05toefl\x18\x07 \x01(\x02\x12\r\n\x05ielts\x18\x08 \x01(\x02\x12\x0e\n\x06marker\x18\t \x01(\t\"2\n\x05ratio\x12\x14\n\x0cpartly_ratio\x18\x01 \x01(\x02\x12\x13\n\x0btotal_ratio\x18\x02 \x01(\x02\"\x95\x01\n\nsysReponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12-\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x1f.recommend.sysReponse.DataEntry\x1a=\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.recommend.ratio:\x02\x38\x01\x32G\n\x0bRecommender\x12\x38\n\trecommend\x12\x12.recommend.userReq\x1a\x15.recommend.sysReponse\"\x00\x62\x06proto3'
)




_USERREQ = _descriptor.Descriptor(
  name='userReq',
  full_name='recommend.userReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ug_level', full_name='recommend.userReq.ug_level', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ug_major', full_name='recommend.userReq.ug_major', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='intended_country', full_name='recommend.userReq.intended_country', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ug_gpa', full_name='recommend.userReq.ug_gpa', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gre', full_name='recommend.userReq.gre', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gmat', full_name='recommend.userReq.gmat', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='toefl', full_name='recommend.userReq.toefl', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ielts', full_name='recommend.userReq.ielts', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='marker', full_name='recommend.userReq.marker', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=31,
  serialized_end=191,
)


_RATIO = _descriptor.Descriptor(
  name='ratio',
  full_name='recommend.ratio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partly_ratio', full_name='recommend.ratio.partly_ratio', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_ratio', full_name='recommend.ratio.total_ratio', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=243,
)


_SYSREPONSE_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='recommend.sysReponse.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='recommend.sysReponse.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='recommend.sysReponse.DataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=395,
)

_SYSREPONSE = _descriptor.Descriptor(
  name='sysReponse',
  full_name='recommend.sysReponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='recommend.sysReponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='recommend.sysReponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='recommend.sysReponse.data', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SYSREPONSE_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=395,
)

_SYSREPONSE_DATAENTRY.fields_by_name['value'].message_type = _RATIO
_SYSREPONSE_DATAENTRY.containing_type = _SYSREPONSE
_SYSREPONSE.fields_by_name['data'].message_type = _SYSREPONSE_DATAENTRY
DESCRIPTOR.message_types_by_name['userReq'] = _USERREQ
DESCRIPTOR.message_types_by_name['ratio'] = _RATIO
DESCRIPTOR.message_types_by_name['sysReponse'] = _SYSREPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

userReq = _reflection.GeneratedProtocolMessageType('userReq', (_message.Message,), {
  'DESCRIPTOR' : _USERREQ,
  '__module__' : 'recommend_pb2'
  # @@protoc_insertion_point(class_scope:recommend.userReq)
  })
_sym_db.RegisterMessage(userReq)

ratio = _reflection.GeneratedProtocolMessageType('ratio', (_message.Message,), {
  'DESCRIPTOR' : _RATIO,
  '__module__' : 'recommend_pb2'
  # @@protoc_insertion_point(class_scope:recommend.ratio)
  })
_sym_db.RegisterMessage(ratio)

sysReponse = _reflection.GeneratedProtocolMessageType('sysReponse', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYSREPONSE_DATAENTRY,
    '__module__' : 'recommend_pb2'
    # @@protoc_insertion_point(class_scope:recommend.sysReponse.DataEntry)
    })
  ,
  'DESCRIPTOR' : _SYSREPONSE,
  '__module__' : 'recommend_pb2'
  # @@protoc_insertion_point(class_scope:recommend.sysReponse)
  })
_sym_db.RegisterMessage(sysReponse)
_sym_db.RegisterMessage(sysReponse.DataEntry)


_SYSREPONSE_DATAENTRY._options = None

_RECOMMENDER = _descriptor.ServiceDescriptor(
  name='Recommender',
  full_name='recommend.Recommender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=397,
  serialized_end=468,
  methods=[
  _descriptor.MethodDescriptor(
    name='recommend',
    full_name='recommend.Recommender.recommend',
    index=0,
    containing_service=None,
    input_type=_USERREQ,
    output_type=_SYSREPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDER)

DESCRIPTOR.services_by_name['Recommender'] = _RECOMMENDER

# @@protoc_insertion_point(module_scope)