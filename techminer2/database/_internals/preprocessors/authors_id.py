# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import sys

import pandas as pd  # type: ignore


def _local_processing_func(text):
    #
    #                                                 1
    # 10040007900; 56255739500; 48361045500; 6506221360
    #                          [No author id available]
    #  58065524100;58065658300;57190620397;55567227600;
    #
    text = text.map(lambda x: pd.NA if isinstance(x, str) and x == "1" else x)
    text = text.map(
        lambda x: (
            pd.NA if isinstance(x, str) and x.startswith("[") and x.endswith("]") else x
        )
    )
    text = text.str.replace(";$", "", regex=True)
    return text


def internal__preprocess_authors_id(root_dir):
    """:meta private:"""

    from techminer2.database.operators.transform import internal__transform

    sys.stderr.write("INFO  Processing 'authors_id' column\n")
    sys.stderr.flush()

    internal__transform(
        field="raw_authors_id",
        other_field="authors_id",
        function=_local_processing_func,
        root_dir=root_dir,
    )


#
