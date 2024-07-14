# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...fields.process_field import _process_field


def run_document_type_importer(root_dir):
    """Run authors importer."""

    _process_field(
        source="raw_document_type",
        dest="document_type",
        func=lambda x: x,
        root_dir=root_dir,
    )
