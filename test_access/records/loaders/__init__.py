# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# test-access is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Loaders.

This file contains sample loaders that can be used to deserialize input data in
an application level data structure. The marshmallow_loader() method can be
parameterized with different schemas for the record metadata. In the provided
json_v1 instance, it uses the MetadataSchemaV1, defining the
PersistentIdentifier field.
"""

from __future__ import absolute_import, print_function

from invenio_records_rest.loaders.marshmallow import \
    json_patch_loader, marshmallow_loader

from test_access.records.loaders.myrecord import MyRecordSchemaV1
from ..marshmallow import MetadataSchemaV1

#: JSON loader using Marshmallow for data validation.
json_v1 = marshmallow_loader(MetadataSchemaV1)
my_record_loader = marshmallow_loader(MyRecordSchemaV1)

__all__ = (
    'json_v1', 'my_record_loader',
)
