# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.operations.process_database_field import fields__process


def preprocessing__isbn(root_dir):
    """Run authors importer."""

    fields__process(
        source="isbn",
        dest="isbn",
        func=lambda x: x,
        root_dir=root_dir,
    )
