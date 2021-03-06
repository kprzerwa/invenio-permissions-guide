# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# test-access is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration."""

from __future__ import absolute_import, print_function

from invenio_indexer.api import RecordIndexer
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all, check_elasticsearch
from invenio_search import RecordsSearch

from test_access.records.api import MyRecord
from test_access.records.permissions import record_read_permission_factory, \
    record_update_permission_factory, record_delete_permission_factory
from test_access.records.search import MyRecordSearch


def _(x):
    """Identity function for string extraction."""
    return x


RECORDS_REST_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        pid_minter='recid',
        pid_fetcher='recid',
        default_endpoint_prefix=True,
        search_class=MyRecordSearch,
        indexer_class=RecordIndexer,
        record_class=MyRecord,
        search_index='records',
        search_type=None,
        record_serializers={
            "application/json": (
                "invenio_records_rest.serializers:json_v1_response"
            )
        },
        search_serializers={
            "application/json": (
                "invenio_records_rest.serializers:json_v1_search"
            ),
            "application/vnd.ils.refs+json": (
                "invenio_records_rest.serializers:json_v1_response"
            ),
        },
        record_loaders={
            'application/json': ('test_access.records.loaders'
                                 ':my_record_loader'),
        },
        list_route='/records/',
        item_route='/records/<pid(recid):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
        # TODO: Redefine these permissions to cover your auth needs
        create_permission_factory_imp=allow_all,
        read_permission_factory_imp=record_read_permission_factory,
        update_permission_factory_imp=record_update_permission_factory,
        delete_permission_factory_imp=record_delete_permission_factory,
        list_permission_factory_imp=record_read_permission_factory
    ),
)
"""REST API for test-access."""

RECORDS_UI_ENDPOINTS = {
    'recid': {
        'pid_type': 'recid',
        'route': '/records/<pid_value>',
        'template': 'records/record.html',
    },
}
"""Records UI for test-access."""

SEARCH_UI_JSTEMPLATE_RESULTS = 'templates/records/results.html'
"""Result list template."""

PIDSTORE_RECID_FIELD = 'id'

TEST_ACCESS_ENDPOINTS_ENABLED = True
"""Enable/disable automatic endpoint registration."""


RECORDS_REST_FACETS = dict(
    records=dict(
        aggs=dict(
            type=dict(terms=dict(field='type')),
            keywords=dict(terms=dict(field='keywords'))
        ),
        post_filters=dict(
            type=terms_filter('type'),
            keywords=terms_filter('keywords'),
        )
    )
)
"""Introduce searching facets."""


RECORDS_REST_SORT_OPTIONS = dict(
    records=dict(
        bestmatch=dict(
            title=_('Best match'),
            fields=['_score'],
            default_order='desc',
            order=1,
        ),
        mostrecent=dict(
            title=_('Most recent'),
            fields=['-_created'],
            default_order='asc',
            order=2,
        ),
    )
)
"""Setup sorting options."""


RECORDS_REST_DEFAULT_SORT = dict(
    records=dict(
        query='bestmatch',
        noquery='mostrecent',
    )
)
"""Set default sorting options."""
