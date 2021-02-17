# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/errors/payments_account_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/errors/payments_account_error.proto',
  package='google.ads.googleads.v6.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v6.errorsB\031PaymentsAccountErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V6.Errors\312\002\036Google\\Ads\\GoogleAds\\V6\\Errors\352\002\"Google::Ads::GoogleAds::V6::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/ads/googleads/v6/errors/payments_account_error.proto\x12\x1egoogle.ads.googleads.v6.errors\x1a\x1cgoogle/api/annotations.proto\"x\n\x18PaymentsAccountErrorEnum\"\\\n\x14PaymentsAccountError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12&\n\"NOT_SUPPORTED_FOR_MANAGER_CUSTOMER\x10\x02\x42\xf4\x01\n\"com.google.ads.googleads.v6.errorsB\x19PaymentsAccountErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V6.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V6\\Errors\xea\x02\"Google::Ads::GoogleAds::V6::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PAYMENTSACCOUNTERRORENUM_PAYMENTSACCOUNTERROR = _descriptor.EnumDescriptor(
  name='PaymentsAccountError',
  full_name='google.ads.googleads.v6.errors.PaymentsAccountErrorEnum.PaymentsAccountError',
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
      name='NOT_SUPPORTED_FOR_MANAGER_CUSTOMER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=245,
)
_sym_db.RegisterEnumDescriptor(_PAYMENTSACCOUNTERRORENUM_PAYMENTSACCOUNTERROR)


_PAYMENTSACCOUNTERRORENUM = _descriptor.Descriptor(
  name='PaymentsAccountErrorEnum',
  full_name='google.ads.googleads.v6.errors.PaymentsAccountErrorEnum',
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
    _PAYMENTSACCOUNTERRORENUM_PAYMENTSACCOUNTERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=245,
)

_PAYMENTSACCOUNTERRORENUM_PAYMENTSACCOUNTERROR.containing_type = _PAYMENTSACCOUNTERRORENUM
DESCRIPTOR.message_types_by_name['PaymentsAccountErrorEnum'] = _PAYMENTSACCOUNTERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaymentsAccountErrorEnum = _reflection.GeneratedProtocolMessageType('PaymentsAccountErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENTSACCOUNTERRORENUM,
  '__module__' : 'google.ads.googleads.v6.errors.payments_account_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.errors.PaymentsAccountErrorEnum)
  })
_sym_db.RegisterMessage(PaymentsAccountErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
