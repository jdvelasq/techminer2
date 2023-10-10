# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...refine.fields.process_field import _process_field


def run_document_title_importer(root_dir):
    """Run importer."""

    _process_field(
        source="raw_document_title",
        dest="document_title",
        func=lambda x: x.str.replace(r"\[.*", "", regex=True)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.lower(),
        root_dir=root_dir,
    )
