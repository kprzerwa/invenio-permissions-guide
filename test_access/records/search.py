from elasticsearch_dsl import Q
from flask import g
from flask_principal import Permission
from invenio_access import superuser_access
from invenio_search import RecordsSearch
from invenio_search.api import DefaultFilter


def get_user_provides():
    """Extract the user's provides from g."""
    provides = []
    for need in g.identity.provides:
        try:
            provides.append(need.value.lower())
        except AttributeError:
            # Add the user ID (integer) to the list
            provides.append(need.value)
    return provides


def search_permission_filter():
    """Filter list of results."""
    # Send empty query for admins
    if Permission(superuser_access).allows(g.identity):
        return Q()

    provides = get_user_provides()

    # Filter for restricted records, that the user has access to
    read_restricted = Q('terms', **{'owners': provides})

    return Q('bool', filter=[read_restricted])


class MyRecordSearch(RecordsSearch):
    """My Record search class."""

    class Meta:
        """Configuration for CERN search."""

        index = 'records'
        doc_types = None
        fields = ('*',)
        default_filter = DefaultFilter(search_permission_filter)
