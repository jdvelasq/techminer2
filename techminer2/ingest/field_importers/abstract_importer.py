# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import pandas as pd

from ...fields.process_field import _process_field


def run_abstract_importer(root_dir):
    """Run authors importer."""

    _process_field(
        source="raw_abstract",
        dest="abstract",
        func=lambda x: x.map(
            lambda w: pd.NA if w[0] == "[" and w[-1] == "]" else w, na_action="ignore"
        ).str.replace("-", "_", regex=False)
        # -----------------------------------------------------------------------------
        # remove all html tags
        .str.replace("<.*?>", "", regex=True)
        # -----------------------------------------------------------------------------
        # remove all non-ascii characters
        .str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")
        # -----------------------------------------------------------------------------
        # remove appostrophes
        .str.replace("ʿ", "'", regex=False)
        .str.replace("’", "'", regex=False)
        .str.replace("'", "'", regex=False)
        # -----------------------------------------------------------------------------
        .str.lower(),
        root_dir=root_dir,
    )
