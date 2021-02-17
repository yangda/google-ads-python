# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/errors/third_party_app_analytics_link_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/errors/third_party_app_analytics_link_error.proto',
  package='google.ads.googleads.v6.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v6.errorsB$ThirdPartyAppAnalyticsLinkErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V6.Errors\312\002\036Google\\Ads\\GoogleAds\\V6\\Errors\352\002\"Google::Ads::GoogleAds::V6::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nIgoogle/ads/googleads/v6/errors/third_party_app_analytics_link_error.proto\x12\x1egoogle.ads.googleads.v6.errors\x1a\x1cgoogle/api/annotations.proto\"\xfe\x01\n#ThirdPartyAppAnalyticsLinkErrorEnum\"\xd6\x01\n\x1fThirdPartyAppAnalyticsLinkError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12!\n\x1dINVALID_ANALYTICS_PROVIDER_ID\x10\x02\x12\x19\n\x15INVALID_MOBILE_APP_ID\x10\x03\x12\x1d\n\x19MOBILE_APP_IS_NOT_ENABLED\x10\x04\x12\x38\n4CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK\x10\x05\x42\xff\x01\n\"com.google.ads.googleads.v6.errorsB$ThirdPartyAppAnalyticsLinkErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V6.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V6\\Errors\xea\x02\"Google::Ads::GoogleAds::V6::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_THIRDPARTYAPPANALYTICSLINKERRORENUM_THIRDPARTYAPPANALYTICSLINKERROR = _descriptor.EnumDescriptor(
  name='ThirdPartyAppAnalyticsLinkError',
  full_name='google.ads.googleads.v6.errors.ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError',
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
      name='INVALID_ANALYTICS_PROVIDER_ID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MOBILE_APP_ID', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOBILE_APP_IS_NOT_ENABLED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=180,
  serialized_end=394,
)
_sym_db.RegisterEnumDescriptor(_THIRDPARTYAPPANALYTICSLINKERRORENUM_THIRDPARTYAPPANALYTICSLINKERROR)


_THIRDPARTYAPPANALYTICSLINKERRORENUM = _descriptor.Descriptor(
  name='ThirdPartyAppAnalyticsLinkErrorEnum',
  full_name='google.ads.googleads.v6.errors.ThirdPartyAppAnalyticsLinkErrorEnum',
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
    _THIRDPARTYAPPANALYTICSLINKERRORENUM_THIRDPARTYAPPANALYTICSLINKERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=394,
)

_THIRDPARTYAPPANALYTICSLINKERRORENUM_THIRDPARTYAPPANALYTICSLINKERROR.containing_type = _THIRDPARTYAPPANALYTICSLINKERRORENUM
DESCRIPTOR.message_types_by_name['ThirdPartyAppAnalyticsLinkErrorEnum'] = _THIRDPARTYAPPANALYTICSLINKERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThirdPartyAppAnalyticsLinkErrorEnum = _reflection.GeneratedProtocolMessageType('ThirdPartyAppAnalyticsLinkErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _THIRDPARTYAPPANALYTICSLINKERRORENUM,
  '__module__' : 'google.ads.googleads.v6.errors.third_party_app_analytics_link_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.errors.ThirdPartyAppAnalyticsLinkErrorEnum)
  })
_sym_db.RegisterMessage(ThirdPartyAppAnalyticsLinkErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
