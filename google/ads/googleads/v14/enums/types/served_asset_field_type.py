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


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v14.enums",
    marshal="google.ads.googleads.v14",
    manifest={"ServedAssetFieldTypeEnum",},
)


class ServedAssetFieldTypeEnum(proto.Message):
    r"""Container for enum describing possible asset field types.
    """

    class ServedAssetFieldType(proto.Enum):
        r"""The possible asset field types."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        HEADLINE_1 = 2
        HEADLINE_2 = 3
        HEADLINE_3 = 4
        DESCRIPTION_1 = 5
        DESCRIPTION_2 = 6
        SITELINK = 22
        CALL = 23
        MOBILE_APP = 24
        CALLOUT = 25
        STRUCTURED_SNIPPET = 26
        PRICE = 27
        PROMOTION = 28
        AD_IMAGE = 29
        LEAD_FORM = 30
        BUSINESS_LOGO = 31


__all__ = tuple(sorted(__protobuf__.manifest))
