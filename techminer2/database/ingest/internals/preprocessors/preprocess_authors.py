# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd  # type: ignore

from .....internals.log_message import internal__log_message
from ....field_operators.transform_field_operator import internal__transform_field


def _local_processing(text):
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
    text = text.str.replace(r", \(\d\)", "", regex=True)

    text = text.str.replace(", Jr.", " Jr.", regex=False)
    text = text.str.replace("; ", ";", regex=False)
    text = text.str.replace(";", "; ", regex=False)
    #
    # some old database records uses ',' as separator
    text = text.str.replace(", ", ",", regex=False).str.replace(",", "; ", regex=False)

    text = text.str.title()
    text = text.fillna(pd.NA)
    text = text.map(
        lambda x: (
            pd.NA if isinstance(x, str) and x.startswith("[") and x.endswith("]") else x
        )
    )
    text = text.map(
        lambda x: pd.NA if isinstance(x, str) and x.lower() == "anonymous" else x
    )
    text = text.map(
        lambda x: pd.NA if isinstance(x, str) and x.lower() == "anon" else x
    )

    return text


def internal__preprocess_authors(root_dir):
    """Run authors importer."""

    internal__log_message(
        msgs="Processing 'authors' column.",
        prompt_flag=True,
    )

    internal__transform_field(
        field="raw_authors",
        other_field="authors",
        function=_local_processing,
        root_dir=root_dir,
    )
