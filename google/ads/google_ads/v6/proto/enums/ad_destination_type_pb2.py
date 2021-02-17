# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/ad_destination_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/ad_destination_type.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\026AdDestinationTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7google/ads/googleads/v6/enums/ad_destination_type.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\x90\x02\n\x15\x41\x64\x44\x65stinationTypeEnum\"\xf6\x01\n\x11\x41\x64\x44\x65stinationType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x12\n\x0eNOT_APPLICABLE\x10\x02\x12\x0b\n\x07WEBSITE\x10\x03\x12\x11\n\rAPP_DEEP_LINK\x10\x04\x12\r\n\tAPP_STORE\x10\x05\x12\x0e\n\nPHONE_CALL\x10\x06\x12\x12\n\x0eMAP_DIRECTIONS\x10\x07\x12\x14\n\x10LOCATION_LISTING\x10\x08\x12\x0b\n\x07MESSAGE\x10\t\x12\r\n\tLEAD_FORM\x10\n\x12\x0b\n\x07YOUTUBE\x10\x0b\x12\x1d\n\x19UNMODELED_FOR_CONVERSIONS\x10\x0c\x42\xeb\x01\n!com.google.ads.googleads.v6.enumsB\x16\x41\x64\x44\x65stinationTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ADDESTINATIONTYPEENUM_ADDESTINATIONTYPE = _descriptor.EnumDescriptor(
  name='AdDestinationType',
  full_name='google.ads.googleads.v6.enums.AdDestinationTypeEnum.AdDestinationType',
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
      name='NOT_APPLICABLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEBSITE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APP_DEEP_LINK', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APP_STORE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PHONE_CALL', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAP_DIRECTIONS', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_LISTING', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LEAD_FORM', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNMODELED_FOR_CONVERSIONS', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=147,
  serialized_end=393,
)
_sym_db.RegisterEnumDescriptor(_ADDESTINATIONTYPEENUM_ADDESTINATIONTYPE)


_ADDESTINATIONTYPEENUM = _descriptor.Descriptor(
  name='AdDestinationTypeEnum',
  full_name='google.ads.googleads.v6.enums.AdDestinationTypeEnum',
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
    _ADDESTINATIONTYPEENUM_ADDESTINATIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=393,
)

_ADDESTINATIONTYPEENUM_ADDESTINATIONTYPE.containing_type = _ADDESTINATIONTYPEENUM
DESCRIPTOR.message_types_by_name['AdDestinationTypeEnum'] = _ADDESTINATIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdDestinationTypeEnum = _reflection.GeneratedProtocolMessageType('AdDestinationTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _ADDESTINATIONTYPEENUM,
  '__module__' : 'google.ads.googleads.v6.enums.ad_destination_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.AdDestinationTypeEnum)
  })
_sym_db.RegisterMessage(AdDestinationTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
