# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.operations.fillna_database_field import fields__fillna


def preprocessing__abbr_source_title(root_dir):
    """Run authors importer."""

    fields__fillna(
        fill_field="abbr_source_title",
        with_field="source_title",
        root_dir=root_dir,
    )
