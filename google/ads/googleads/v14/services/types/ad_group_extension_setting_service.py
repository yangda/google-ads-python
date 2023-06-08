# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableSequence

import proto  # type: ignore

from google.ads.googleads.v14.enums.types import (
    response_content_type as gage_response_content_type,
)
from google.ads.googleads.v14.resources.types import (
    ad_group_extension_setting as gagr_ad_group_extension_setting,
)
from google.protobuf import field_mask_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v14.services",
    marshal="google.ads.googleads.v14",
    manifest={
        "MutateAdGroupExtensionSettingsRequest",
        "AdGroupExtensionSettingOperation",
        "MutateAdGroupExtensionSettingsResponse",
        "MutateAdGroupExtensionSettingResult",
    },
)


class MutateAdGroupExtensionSettingsRequest(proto.Message):
    r"""Request message for
    [AdGroupExtensionSettingService.MutateAdGroupExtensionSettings][google.ads.googleads.v14.services.AdGroupExtensionSettingService.MutateAdGroupExtensionSettings].

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose ad
            group extension settings are being modified.
        operations (MutableSequence[google.ads.googleads.v14.services.types.AdGroupExtensionSettingOperation]):
            Required. The list of operations to perform
            on individual ad group extension settings.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, all operations will be carried
            out in one transaction if and only if they are
            all valid. Default is false.
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
    """

    customer_id: str = proto.Field(
        proto.STRING, number=1,
    )
    operations: MutableSequence[
        "AdGroupExtensionSettingOperation"
    ] = proto.RepeatedField(
        proto.MESSAGE, number=2, message="AdGroupExtensionSettingOperation",
    )
    partial_failure: bool = proto.Field(
        proto.BOOL, number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL, number=4,
    )


class AdGroupExtensionSettingOperation(proto.Message):
    r"""A single operation (create, update, remove) on an ad group
    extension setting.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        response_content_type (google.ads.googleads.v14.enums.types.ResponseContentTypeEnum.ResponseContentType):
            The response content type setting. Determines
            whether the mutable resource or just the
            resource name should be returned post mutation.
        create (google.ads.googleads.v14.resources.types.AdGroupExtensionSetting):
            Create operation: No resource name is
            expected for the new ad group extension setting.

            This field is a member of `oneof`_ ``operation``.
        update (google.ads.googleads.v14.resources.types.AdGroupExtensionSetting):
            Update operation: The ad group extension
            setting is expected to have a valid resource
            name.

            This field is a member of `oneof`_ ``operation``.
        remove (str):
            Remove operation: A resource name for the removed ad group
            extension setting is expected, in this format:

            ``customers/{customer_id}/adGroupExtensionSettings/{ad_group_id}~{extension_type}``

            This field is a member of `oneof`_ ``operation``.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE, number=4, message=field_mask_pb2.FieldMask,
    )
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType = proto.Field(
        proto.ENUM,
        number=5,
        enum=gage_response_content_type.ResponseContentTypeEnum.ResponseContentType,
    )
    create: gagr_ad_group_extension_setting.AdGroupExtensionSetting = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=gagr_ad_group_extension_setting.AdGroupExtensionSetting,
    )
    update: gagr_ad_group_extension_setting.AdGroupExtensionSetting = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="operation",
        message=gagr_ad_group_extension_setting.AdGroupExtensionSetting,
    )
    remove: str = proto.Field(
        proto.STRING, number=3, oneof="operation",
    )


class MutateAdGroupExtensionSettingsResponse(proto.Message):
    r"""Response message for an ad group extension setting mutate.
    Attributes:
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (for example, auth errors), we return
            an RPC level error.
        results (MutableSequence[google.ads.googleads.v14.services.types.MutateAdGroupExtensionSettingResult]):
            All results for the mutate.
    """

    partial_failure_error: status_pb2.Status = proto.Field(
        proto.MESSAGE, number=3, message=status_pb2.Status,
    )
    results: MutableSequence[
        "MutateAdGroupExtensionSettingResult"
    ] = proto.RepeatedField(
        proto.MESSAGE, number=2, message="MutateAdGroupExtensionSettingResult",
    )


class MutateAdGroupExtensionSettingResult(proto.Message):
    r"""The result for the ad group extension setting mutate.
    Attributes:
        resource_name (str):
            Returned for successful operations.
        ad_group_extension_setting (google.ads.googleads.v14.resources.types.AdGroupExtensionSetting):
            The mutated AdGroupExtensionSetting with only mutable fields
            after mutate. The field will only be returned when
            response_content_type is set to "MUTABLE_RESOURCE".
    """

    resource_name: str = proto.Field(
        proto.STRING, number=1,
    )
    ad_group_extension_setting: gagr_ad_group_extension_setting.AdGroupExtensionSetting = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gagr_ad_group_extension_setting.AdGroupExtensionSetting,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
