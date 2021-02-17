# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/batch_job.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import batch_job_status_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_batch__job__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/resources/batch_job.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\rBatchJobProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1google/ads/googleads/v6/resources/batch_job.proto\x12!google.ads.googleads.v6.resources\x1a\x34google/ads/googleads/v6/enums/batch_job_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x92\x07\n\x08\x42\x61tchJob\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0\x41\x05\xfa\x41#\n!googleads.googleapis.com/BatchJob\x12\x14\n\x02id\x18\x07 \x01(\x03\x42\x03\xe0\x41\x03H\x00\x88\x01\x01\x12)\n\x17next_add_sequence_token\x18\x08 \x01(\tB\x03\xe0\x41\x03H\x01\x88\x01\x01\x12S\n\x08metadata\x18\x04 \x01(\x0b\x32<.google.ads.googleads.v6.resources.BatchJob.BatchJobMetadataB\x03\xe0\x41\x03\x12U\n\x06status\x18\x05 \x01(\x0e\x32@.google.ads.googleads.v6.enums.BatchJobStatusEnum.BatchJobStatusB\x03\xe0\x41\x03\x12(\n\x16long_running_operation\x18\t \x01(\tB\x03\xe0\x41\x03H\x02\x88\x01\x01\x1a\x94\x03\n\x10\x42\x61tchJobMetadata\x12$\n\x12\x63reation_date_time\x18\x08 \x01(\tB\x03\xe0\x41\x03H\x00\x88\x01\x01\x12!\n\x0fstart_date_time\x18\x07 \x01(\tB\x03\xe0\x41\x03H\x01\x88\x01\x01\x12&\n\x14\x63ompletion_date_time\x18\t \x01(\tB\x03\xe0\x41\x03H\x02\x88\x01\x01\x12,\n\x1a\x65stimated_completion_ratio\x18\n \x01(\x01\x42\x03\xe0\x41\x03H\x03\x88\x01\x01\x12!\n\x0foperation_count\x18\x0b \x01(\x03\x42\x03\xe0\x41\x03H\x04\x88\x01\x01\x12*\n\x18\x65xecuted_operation_count\x18\x0c \x01(\x03\x42\x03\xe0\x41\x03H\x05\x88\x01\x01\x42\x15\n\x13_creation_date_timeB\x12\n\x10_start_date_timeB\x17\n\x15_completion_date_timeB\x1d\n\x1b_estimated_completion_ratioB\x12\n\x10_operation_countB\x1b\n\x19_executed_operation_count:X\xea\x41U\n!googleads.googleapis.com/BatchJob\x12\x30\x63ustomers/{customer_id}/batchJobs/{batch_job_id}B\x05\n\x03_idB\x1a\n\x18_next_add_sequence_tokenB\x19\n\x17_long_running_operationB\xfa\x01\n%com.google.ads.googleads.v6.resourcesB\rBatchJobProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_batch__job__status__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_BATCHJOB_BATCHJOBMETADATA = _descriptor.Descriptor(
  name='BatchJobMetadata',
  full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='creation_date_time', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata.creation_date_time', index=0,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date_time', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata.start_date_time', index=1,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completion_date_time', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata.completion_date_time', index=2,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='estimated_completion_ratio', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata.estimated_completion_ratio', index=3,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_count', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata.operation_count', index=4,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='executed_operation_count', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata.executed_operation_count', index=5,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_creation_date_time', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata._creation_date_time',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_start_date_time', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata._start_date_time',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_completion_date_time', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata._completion_date_time',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_estimated_completion_ratio', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata._estimated_completion_ratio',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_operation_count', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata._operation_count',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_executed_operation_count', full_name='google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata._executed_operation_count',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=591,
  serialized_end=995,
)

_BATCHJOB = _descriptor.Descriptor(
  name='BatchJob',
  full_name='google.ads.googleads.v6.resources.BatchJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.BatchJob.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A#\n!googleads.googleapis.com/BatchJob', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v6.resources.BatchJob.id', index=1,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_add_sequence_token', full_name='google.ads.googleads.v6.resources.BatchJob.next_add_sequence_token', index=2,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.ads.googleads.v6.resources.BatchJob.metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v6.resources.BatchJob.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='long_running_operation', full_name='google.ads.googleads.v6.resources.BatchJob.long_running_operation', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BATCHJOB_BATCHJOBMETADATA, ],
  enum_types=[
  ],
  serialized_options=b'\352AU\n!googleads.googleapis.com/BatchJob\0220customers/{customer_id}/batchJobs/{batch_job_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_id', full_name='google.ads.googleads.v6.resources.BatchJob._id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_next_add_sequence_token', full_name='google.ads.googleads.v6.resources.BatchJob._next_add_sequence_token',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_long_running_operation', full_name='google.ads.googleads.v6.resources.BatchJob._long_running_operation',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=233,
  serialized_end=1147,
)

_BATCHJOB_BATCHJOBMETADATA.containing_type = _BATCHJOB
_BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_creation_date_time'].fields.append(
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['creation_date_time'])
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['creation_date_time'].containing_oneof = _BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_creation_date_time']
_BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_start_date_time'].fields.append(
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['start_date_time'])
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['start_date_time'].containing_oneof = _BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_start_date_time']
_BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_completion_date_time'].fields.append(
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['completion_date_time'])
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['completion_date_time'].containing_oneof = _BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_completion_date_time']
_BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_estimated_completion_ratio'].fields.append(
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['estimated_completion_ratio'])
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['estimated_completion_ratio'].containing_oneof = _BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_estimated_completion_ratio']
_BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_operation_count'].fields.append(
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['operation_count'])
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['operation_count'].containing_oneof = _BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_operation_count']
_BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_executed_operation_count'].fields.append(
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['executed_operation_count'])
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['executed_operation_count'].containing_oneof = _BATCHJOB_BATCHJOBMETADATA.oneofs_by_name['_executed_operation_count']
_BATCHJOB.fields_by_name['metadata'].message_type = _BATCHJOB_BATCHJOBMETADATA
_BATCHJOB.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_batch__job__status__pb2._BATCHJOBSTATUSENUM_BATCHJOBSTATUS
_BATCHJOB.oneofs_by_name['_id'].fields.append(
  _BATCHJOB.fields_by_name['id'])
_BATCHJOB.fields_by_name['id'].containing_oneof = _BATCHJOB.oneofs_by_name['_id']
_BATCHJOB.oneofs_by_name['_next_add_sequence_token'].fields.append(
  _BATCHJOB.fields_by_name['next_add_sequence_token'])
_BATCHJOB.fields_by_name['next_add_sequence_token'].containing_oneof = _BATCHJOB.oneofs_by_name['_next_add_sequence_token']
_BATCHJOB.oneofs_by_name['_long_running_operation'].fields.append(
  _BATCHJOB.fields_by_name['long_running_operation'])
_BATCHJOB.fields_by_name['long_running_operation'].containing_oneof = _BATCHJOB.oneofs_by_name['_long_running_operation']
DESCRIPTOR.message_types_by_name['BatchJob'] = _BATCHJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchJob = _reflection.GeneratedProtocolMessageType('BatchJob', (_message.Message,), {

  'BatchJobMetadata' : _reflection.GeneratedProtocolMessageType('BatchJobMetadata', (_message.Message,), {
    'DESCRIPTOR' : _BATCHJOB_BATCHJOBMETADATA,
    '__module__' : 'google.ads.googleads.v6.resources.batch_job_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.BatchJob.BatchJobMetadata)
    })
  ,
  'DESCRIPTOR' : _BATCHJOB,
  '__module__' : 'google.ads.googleads.v6.resources.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.BatchJob)
  })
_sym_db.RegisterMessage(BatchJob)
_sym_db.RegisterMessage(BatchJob.BatchJobMetadata)


DESCRIPTOR._options = None
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['creation_date_time']._options = None
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['start_date_time']._options = None
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['completion_date_time']._options = None
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['estimated_completion_ratio']._options = None
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['operation_count']._options = None
_BATCHJOB_BATCHJOBMETADATA.fields_by_name['executed_operation_count']._options = None
_BATCHJOB.fields_by_name['resource_name']._options = None
_BATCHJOB.fields_by_name['id']._options = None
_BATCHJOB.fields_by_name['next_add_sequence_token']._options = None
_BATCHJOB.fields_by_name['metadata']._options = None
_BATCHJOB.fields_by_name['status']._options = None
_BATCHJOB.fields_by_name['long_running_operation']._options = None
_BATCHJOB._options = None
# @@protoc_insertion_point(module_scope)
