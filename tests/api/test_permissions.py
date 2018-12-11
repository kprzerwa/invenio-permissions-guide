import uuid

import pytest
from flask import current_app
from flask_principal import identity_loaded, AnonymousIdentity, Identity, \
    identity_changed
from flask_security import login_user
from invenio_accounts.models import User

from test_access.records.api import MyRecord
from test_access.records.permissions import RecordPermission


@pytest.mark.parametrize('access,action,is_allowed', [
    ({'foo': 'bar'}, 'read', True),
    ({'foo': 'bar'}, 'update', False),
    ({'foo': 'bar'}, 'delete', False),
])
def test_record_anonymous(app, db, users, access, action, is_allowed):

    with app.test_request_context():
        identity_changed.send(current_app._get_current_object(),
                              identity=AnonymousIdentity())
        identity_loaded.send(current_app, identity=Identity(None))
        id = uuid.uuid4()
        record = MyRecord.create(access, id_=id)
        factory = RecordPermission(record, action)
        assert factory.can() if is_allowed else not factory.can()


@pytest.mark.parametrize('access,action,is_allowed', [
    ({'foo': 'bar'}, 'read', True),
    ({'foo': 'bar'}, 'update', False),
    ({'foo': 'bar'}, 'delete', False),
    ({'_access': {'delete': [1]}}, 'delete', True),
    ({'_access': {'update': [1]}}, 'update', True),
])
def test_record_user_access(db, users, access, action, is_allowed):
    login_user(User.query.get(1))
    id = uuid.uuid4()
    record = MyRecord.create(access, id_=id)
    factory = RecordPermission(record, action)
    assert factory.can() if is_allowed else not factory.can()


@pytest.mark.parametrize('access,action,is_allowed', [
    ({'foo': 'bar'}, 'read', True),
    ({'foo': 'bar'}, 'update', True),
    ({'foo': 'bar'}, 'delete', False),
    ({'_access': {'delete': ['manager']}}, 'delete', True),
])
def test_record_manager_access(db, users, access, action, is_allowed):
    login_user(User.query.get(2))
    id = uuid.uuid4()
    record = MyRecord.create(access, id_=id)
    factory = RecordPermission(record, action)
    assert factory.can() if is_allowed else not factory.can()


@pytest.mark.parametrize('access,action', [
    ({'foo': 'bar'}, 'read'),
    ({'foo': 'bar'}, 'update'),
    ({'foo': 'bar'}, 'delete'),
])
def test_record_admin_acess(db, users, access, action):
    login_user(User.query.get(3))
    id = uuid.uuid4()
    record = MyRecord.create(access, id_=id)
    factory = RecordPermission(record, action)
    assert factory.can()


# def test_create_access(db, users, access, is_allowed):
#     pass
