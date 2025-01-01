# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.operations.process_database_field import fields__process


def preprocessing__global_citations(root_dir):
    """Run importer."""

    fields__process(
        source="global_citations",
        dest="global_citations",
        func=lambda w: w.fillna(0).astype(int),
        root_dir=root_dir,
    )
