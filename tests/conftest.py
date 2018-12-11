# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# test-access is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Common pytest fixtures and plugins."""

import pytest
from invenio_access.models import ActionRoles
from invenio_access.permissions import superuser_access
from invenio_accounts.models import Role

from test_access.records.permissions import create_records_action


@pytest.fixture()
def users(app, db):
    """Create admin, manager and users."""
    with db.session.begin_nested():
        datastore = app.extensions['security'].datastore
        # create users
        user = datastore.create_user(email='patron1@test.com',
                                     password='123456', active=True)    # ID 1
        manager = datastore.create_user(email='librarian@test.com',
                                        password='123456', active=True)
        admin = datastore.create_user(email='admin@test.com',           # ID 2
                                      password='123456', active=True)   # ID 3
        # Give role to admin
        admin_role = Role(name='admin')
        db.session.add(ActionRoles(action=superuser_access.value,
                                   role=admin_role))
        datastore.add_role_to_user(admin, admin_role)
        # Give role to librarian
        manager_role = Role(name='manager')
        db.session.add(ActionRoles(action=create_records_action.value,
                                   role=manager_role))
        datastore.add_role_to_user(manager, manager_role)
    db.session.commit()

    return {
        'admin': admin,
        'manager': manager,
        'user': user,
    }
