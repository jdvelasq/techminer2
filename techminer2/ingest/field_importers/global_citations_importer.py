# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...fields.process_field import _process_field


def run_global_citations_importer(root_dir):
    """Run importer."""

    _process_field(
        source="global_citations",
        dest="global_citations",
        func=lambda w: w.fillna(0).astype(int),
        root_dir=root_dir,
    )
