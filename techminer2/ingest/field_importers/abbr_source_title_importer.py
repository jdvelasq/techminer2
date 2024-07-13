# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...refine.fields.fillna_field import _fillna_field


def run_abbr_source_title_importer(root_dir):
    """Run authors importer."""

    _fillna_field(
        fill_field="abbr_source_title",
        with_field="source_title",
        root_dir=root_dir,
    )
