# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/frequency_cap_level.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/frequency_cap_level.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\026FrequencyCapLevelProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7google/ads/googleads/v6/enums/frequency_cap_level.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"w\n\x15\x46requencyCapLevelEnum\"^\n\x11\x46requencyCapLevel\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0b\x41\x44_GROUP_AD\x10\x02\x12\x0c\n\x08\x41\x44_GROUP\x10\x03\x12\x0c\n\x08\x43\x41MPAIGN\x10\x04\x42\xeb\x01\n!com.google.ads.googleads.v6.enumsB\x16\x46requencyCapLevelProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FREQUENCYCAPLEVELENUM_FREQUENCYCAPLEVEL = _descriptor.EnumDescriptor(
  name='FrequencyCapLevel',
  full_name='google.ads.googleads.v6.enums.FrequencyCapLevelEnum.FrequencyCapLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_AD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=145,
  serialized_end=239,
)
_sym_db.RegisterEnumDescriptor(_FREQUENCYCAPLEVELENUM_FREQUENCYCAPLEVEL)


_FREQUENCYCAPLEVELENUM = _descriptor.Descriptor(
  name='FrequencyCapLevelEnum',
  full_name='google.ads.googleads.v6.enums.FrequencyCapLevelEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FREQUENCYCAPLEVELENUM_FREQUENCYCAPLEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=239,
)

_FREQUENCYCAPLEVELENUM_FREQUENCYCAPLEVEL.containing_type = _FREQUENCYCAPLEVELENUM
DESCRIPTOR.message_types_by_name['FrequencyCapLevelEnum'] = _FREQUENCYCAPLEVELENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrequencyCapLevelEnum = _reflection.GeneratedProtocolMessageType('FrequencyCapLevelEnum', (_message.Message,), {
  'DESCRIPTOR' : _FREQUENCYCAPLEVELENUM,
  '__module__' : 'google.ads.googleads.v6.enums.frequency_cap_level_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.FrequencyCapLevelEnum)
  })
_sym_db.RegisterMessage(FrequencyCapLevelEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
