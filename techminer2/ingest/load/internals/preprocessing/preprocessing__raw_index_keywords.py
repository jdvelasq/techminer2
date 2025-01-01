# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.operations.process_database_field import fields__process
from .preprocessing__clean_keywords import preprocessing__clean_keywords


def preprocessing__raw_index_keywords(root_dir):
    """Run importer."""

    fields__process(
        source="raw_index_keywords",
        dest="raw_index_keywords",
        func=preprocessing__clean_keywords,
        root_dir=root_dir,
    )
