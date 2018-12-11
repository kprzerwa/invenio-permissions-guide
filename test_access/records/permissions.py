# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# test-access is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Permissions for the records."""
from __future__ import unicode_literals

from flask_principal import UserNeed
from invenio_access import Permission


def record_read_permission_factory(record=None):
    """Record read permission factory."""
    return Permission(*[UserNeed(x) for x in record.get("owners", [])])
