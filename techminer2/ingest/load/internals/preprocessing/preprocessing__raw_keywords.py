# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.operations.merge_database_fields import fields__merge


def preprocessing__raw_keywords(root_dir):

    fields__merge(
        sources=["raw_author_keywords", "raw_index_keywords"],
        dest="raw_keywords",
        root_dir=root_dir,
    )
