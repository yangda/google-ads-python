# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/ad_group_extension_setting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import extension_setting_device_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_extension__setting__device__pb2
from google.ads.google_ads.v6.proto.enums import extension_type_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_extension__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/resources/ad_group_extension_setting.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\034AdGroupExtensionSettingProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nBgoogle/ads/googleads/v6/resources/ad_group_extension_setting.proto\x12!google.ads.googleads.v6.resources\x1a<google/ads/googleads/v6/enums/extension_setting_device.proto\x1a\x32google/ads/googleads/v6/enums/extension_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xd0\x04\n\x17\x41\x64GroupExtensionSetting\x12O\n\rresource_name\x18\x01 \x01(\tB8\xe0\x41\x05\xfa\x41\x32\n0googleads.googleapis.com/AdGroupExtensionSetting\x12[\n\x0e\x65xtension_type\x18\x02 \x01(\x0e\x32>.google.ads.googleads.v6.enums.ExtensionTypeEnum.ExtensionTypeB\x03\xe0\x41\x05\x12?\n\x08\x61\x64_group\x18\x06 \x01(\tB(\xe0\x41\x05\xfa\x41\"\n googleads.googleapis.com/AdGroupH\x00\x88\x01\x01\x12M\n\x14\x65xtension_feed_items\x18\x07 \x03(\tB/\xfa\x41,\n*googleads.googleapis.com/ExtensionFeedItem\x12`\n\x06\x64\x65vice\x18\x05 \x01(\x0e\x32P.google.ads.googleads.v6.enums.ExtensionSettingDeviceEnum.ExtensionSettingDevice:\x87\x01\xea\x41\x83\x01\n0googleads.googleapis.com/AdGroupExtensionSetting\x12Ocustomers/{customer_id}/adGroupExtensionSettings/{ad_group_id}~{extension_type}B\x0b\n\t_ad_groupB\x89\x02\n%com.google.ads.googleads.v6.resourcesB\x1c\x41\x64GroupExtensionSettingProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_extension__setting__device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_extension__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPEXTENSIONSETTING = _descriptor.Descriptor(
  name='AdGroupExtensionSetting',
  full_name='google.ads.googleads.v6.resources.AdGroupExtensionSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.AdGroupExtensionSetting.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A2\n0googleads.googleapis.com/AdGroupExtensionSetting', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension_type', full_name='google.ads.googleads.v6.resources.AdGroupExtensionSetting.extension_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v6.resources.AdGroupExtensionSetting.ad_group', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A\"\n googleads.googleapis.com/AdGroup', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension_feed_items', full_name='google.ads.googleads.v6.resources.AdGroupExtensionSetting.extension_feed_items', index=3,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A,\n*googleads.googleapis.com/ExtensionFeedItem', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v6.resources.AdGroupExtensionSetting.device', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\203\001\n0googleads.googleapis.com/AdGroupExtensionSetting\022Ocustomers/{customer_id}/adGroupExtensionSettings/{ad_group_id}~{extension_type}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_ad_group', full_name='google.ads.googleads.v6.resources.AdGroupExtensionSetting._ad_group',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=310,
  serialized_end=902,
)

_ADGROUPEXTENSIONSETTING.fields_by_name['extension_type'].enum_type = google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_extension__type__pb2._EXTENSIONTYPEENUM_EXTENSIONTYPE
_ADGROUPEXTENSIONSETTING.fields_by_name['device'].enum_type = google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_extension__setting__device__pb2._EXTENSIONSETTINGDEVICEENUM_EXTENSIONSETTINGDEVICE
_ADGROUPEXTENSIONSETTING.oneofs_by_name['_ad_group'].fields.append(
  _ADGROUPEXTENSIONSETTING.fields_by_name['ad_group'])
_ADGROUPEXTENSIONSETTING.fields_by_name['ad_group'].containing_oneof = _ADGROUPEXTENSIONSETTING.oneofs_by_name['_ad_group']
DESCRIPTOR.message_types_by_name['AdGroupExtensionSetting'] = _ADGROUPEXTENSIONSETTING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupExtensionSetting = _reflection.GeneratedProtocolMessageType('AdGroupExtensionSetting', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPEXTENSIONSETTING,
  '__module__' : 'google.ads.googleads.v6.resources.ad_group_extension_setting_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.AdGroupExtensionSetting)
  })
_sym_db.RegisterMessage(AdGroupExtensionSetting)


DESCRIPTOR._options = None
_ADGROUPEXTENSIONSETTING.fields_by_name['resource_name']._options = None
_ADGROUPEXTENSIONSETTING.fields_by_name['extension_type']._options = None
_ADGROUPEXTENSIONSETTING.fields_by_name['ad_group']._options = None
_ADGROUPEXTENSIONSETTING.fields_by_name['extension_feed_items']._options = None
_ADGROUPEXTENSIONSETTING._options = None
# @@protoc_insertion_point(module_scope)
