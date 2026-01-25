import pandas as pd  # type: ignore

from techminer2.operations.transform_column import transform_column


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


def normalize_authors(root_dir):
    """Run authors importer."""

    transform_column(
        source="raw_authors",
        target="authors",
        function=_local_processing,
        root_directory=root_dir,
    )
