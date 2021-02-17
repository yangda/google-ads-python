# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/user_list_string_rule_item_operator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/user_list_string_rule_item_operator.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB#UserListStringRuleItemOperatorProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nGgoogle/ads/googleads/v6/enums/user_list_string_rule_item_operator.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\xe9\x01\n\"UserListStringRuleItemOperatorEnum\"\xc2\x01\n\x1eUserListStringRuleItemOperator\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08\x43ONTAINS\x10\x02\x12\n\n\x06\x45QUALS\x10\x03\x12\x0f\n\x0bSTARTS_WITH\x10\x04\x12\r\n\tENDS_WITH\x10\x05\x12\x0e\n\nNOT_EQUALS\x10\x06\x12\x10\n\x0cNOT_CONTAINS\x10\x07\x12\x13\n\x0fNOT_STARTS_WITH\x10\x08\x12\x11\n\rNOT_ENDS_WITH\x10\tB\xf8\x01\n!com.google.ads.googleads.v6.enumsB#UserListStringRuleItemOperatorProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_USERLISTSTRINGRULEITEMOPERATORENUM_USERLISTSTRINGRULEITEMOPERATOR = _descriptor.EnumDescriptor(
  name='UserListStringRuleItemOperator',
  full_name='google.ads.googleads.v6.enums.UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator',
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
      name='CONTAINS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EQUALS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STARTS_WITH', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDS_WITH', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_EQUALS', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_CONTAINS', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_STARTS_WITH', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_ENDS_WITH', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=176,
  serialized_end=370,
)
_sym_db.RegisterEnumDescriptor(_USERLISTSTRINGRULEITEMOPERATORENUM_USERLISTSTRINGRULEITEMOPERATOR)


_USERLISTSTRINGRULEITEMOPERATORENUM = _descriptor.Descriptor(
  name='UserListStringRuleItemOperatorEnum',
  full_name='google.ads.googleads.v6.enums.UserListStringRuleItemOperatorEnum',
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
    _USERLISTSTRINGRULEITEMOPERATORENUM_USERLISTSTRINGRULEITEMOPERATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=370,
)

_USERLISTSTRINGRULEITEMOPERATORENUM_USERLISTSTRINGRULEITEMOPERATOR.containing_type = _USERLISTSTRINGRULEITEMOPERATORENUM
DESCRIPTOR.message_types_by_name['UserListStringRuleItemOperatorEnum'] = _USERLISTSTRINGRULEITEMOPERATORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserListStringRuleItemOperatorEnum = _reflection.GeneratedProtocolMessageType('UserListStringRuleItemOperatorEnum', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTSTRINGRULEITEMOPERATORENUM,
  '__module__' : 'google.ads.googleads.v6.enums.user_list_string_rule_item_operator_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.UserListStringRuleItemOperatorEnum)
  })
_sym_db.RegisterMessage(UserListStringRuleItemOperatorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
