from flask_login import current_user
from invenio_records import Record


class MyRecord(Record):
    """Custom record class."""

    _schema = "jsonschemas/records/record-v1.0.0.json"

    @classmethod
    def create(cls, data, id_=None, **kwargs):
        """Create My custom record."""
        return super(MyRecord, cls).create(data, id_=id_, **kwargs)
