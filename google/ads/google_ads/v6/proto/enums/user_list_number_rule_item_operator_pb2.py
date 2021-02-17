# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/user_list_number_rule_item_operator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/user_list_number_rule_item_operator.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB#UserListNumberRuleItemOperatorProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nGgoogle/ads/googleads/v6/enums/user_list_number_rule_item_operator.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\xd5\x01\n\"UserListNumberRuleItemOperatorEnum\"\xae\x01\n\x1eUserListNumberRuleItemOperator\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x10\n\x0cGREATER_THAN\x10\x02\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x03\x12\n\n\x06\x45QUALS\x10\x04\x12\x0e\n\nNOT_EQUALS\x10\x05\x12\r\n\tLESS_THAN\x10\x06\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x07\x42\xf8\x01\n!com.google.ads.googleads.v6.enumsB#UserListNumberRuleItemOperatorProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_USERLISTNUMBERRULEITEMOPERATORENUM_USERLISTNUMBERRULEITEMOPERATOR = _descriptor.EnumDescriptor(
  name='UserListNumberRuleItemOperator',
  full_name='google.ads.googleads.v6.enums.UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator',
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
      name='GREATER_THAN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GREATER_THAN_OR_EQUAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EQUALS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_EQUALS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LESS_THAN', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LESS_THAN_OR_EQUAL', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=176,
  serialized_end=350,
)
_sym_db.RegisterEnumDescriptor(_USERLISTNUMBERRULEITEMOPERATORENUM_USERLISTNUMBERRULEITEMOPERATOR)


_USERLISTNUMBERRULEITEMOPERATORENUM = _descriptor.Descriptor(
  name='UserListNumberRuleItemOperatorEnum',
  full_name='google.ads.googleads.v6.enums.UserListNumberRuleItemOperatorEnum',
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
    _USERLISTNUMBERRULEITEMOPERATORENUM_USERLISTNUMBERRULEITEMOPERATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=350,
)

_USERLISTNUMBERRULEITEMOPERATORENUM_USERLISTNUMBERRULEITEMOPERATOR.containing_type = _USERLISTNUMBERRULEITEMOPERATORENUM
DESCRIPTOR.message_types_by_name['UserListNumberRuleItemOperatorEnum'] = _USERLISTNUMBERRULEITEMOPERATORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserListNumberRuleItemOperatorEnum = _reflection.GeneratedProtocolMessageType('UserListNumberRuleItemOperatorEnum', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTNUMBERRULEITEMOPERATORENUM,
  '__module__' : 'google.ads.googleads.v6.enums.user_list_number_rule_item_operator_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.UserListNumberRuleItemOperatorEnum)
  })
_sym_db.RegisterMessage(UserListNumberRuleItemOperatorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
