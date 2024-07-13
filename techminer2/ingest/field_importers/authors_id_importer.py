# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd

from ...refine.fields.process_field import _process_field


def run_authors_id_importer(root_dir):
    """Run Authors ID importer."""

    #
    #                                                 1
    # 10040007900; 56255739500; 48361045500; 6506221360
    #                          [No author id available]
    #  58065524100;58065658300;57190620397;55567227600;
    #
    _process_field(
        source="raw_authors_id",
        dest="authors_id",
        func=lambda w: w.map(lambda x: pd.NA if isinstance(x, str) and x == "1" else x)
        .str.replace(";$", "", regex=True)
        .map(
            lambda x: pd.NA if isinstance(x, str) and x.startswith("[") and x.endswith("]") else x
        ),
        root_dir=root_dir,
    )
