# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd

from ...refine.fields.process_field import _process_field


def run_authors_importer(root_dir):
    """Run authors importer."""

    #
    # Chang V.; Chen Y.; (Justin) Zhang Z.; Xu Q.A.; Baudier P.; Liu B.S.C.
    #                 Guo Y., (1); Klink A., (2); Bartolo P., (1); Guo W.G.
    #           Huang (黃新棫) X.-Y.; Chen (陳怡妏) Y.-W.; Yang (楊鏡堂) J.-T.
    #                                            ALSHAREEF M.; Chang, V.-T.
    #                                                                   NaN
    #                                            [No author name available]
    #                                                             Anonymous
    #                                                                  Anon
    #
    _process_field(
        source="raw_authors",
        dest="authors",
        func=lambda x: x.str.replace(r", \(\d\)", "", regex=True)
        .str.replace(", Jr.", " Jr.", regex=False)
        .str.replace("; ", ";", regex=False)
        .str.replace(";", "; ", regex=False)
        #
        # some old database records uses ',' as separator
        .str.replace(", ", ",", regex=False).str.replace(",", "; ", regex=False)
        #
        .str.title()
        .fillna(pd.NA)
        .map(
            lambda x: pd.NA
            if isinstance(x, str) and x.startswith("[") and x.endswith("]")
            else x
        )
        .map(lambda x: pd.NA if isinstance(x, str) and x.lower() == "anonymous" else x)
        .map(lambda x: pd.NA if isinstance(x, str) and x.lower() == "anon" else x),
        root_dir=root_dir,
    )
