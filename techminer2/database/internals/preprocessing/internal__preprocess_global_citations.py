# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...operations.operations__process_field import internal__process_field


def internal__preprocess_global_citations(root_dir):
    """Run importer."""

    internal__process_field(
        source="global_citations",
        dest="global_citations",
        func=lambda w: w.fillna(0).astype(int),
        root_dir=root_dir,
    )
