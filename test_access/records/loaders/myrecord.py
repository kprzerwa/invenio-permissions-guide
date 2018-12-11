# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# invenio-app-ils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Myrecord schema for marshmallow loader."""
from invenio_records_rest.schemas.fields import PersistentIdentifier
from marshmallow import Schema, fields


class MyRecordSchemaV1(Schema):
    """Internal Location schema."""

    pid = PersistentIdentifier()
    owners = fields.List(fields.Int())
