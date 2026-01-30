"""
Smoke test:
    >>> from pprint import pprint
    >>> import pandas as pd
    >>> from techminer2.io._internals.citation_information.normalize_raw_authors import _process
    >>> data = pd.Series([
    ...     "Chang, V.; Chen, Y.; (Justin) Zhang, Z.; Xu, Q.A.; Baudier, P.; Liu. B.S.C.",
    ...     "Guo Y., (1); Klink A., (2); Bartolo P., (1); Guo W.G.",
    ...     "Huang (黃新棫) X.-Y.; Chen (陳怡妏) Y.-W.; Yang (楊鏡堂) J.-T.",
    ...     "ALSHAREEF M., Jr.; Chang, V.-T.",
    ...     None,
    ...     "[No author name available]",
    ...     "Anonymous",
    ...     "Anon",
    ... ])
    >>> pprint(_process(data).tolist())
    ['Chang V.; Chen Y.; (Justin) Zhang Z.; Xu Q.A.; Baudier P.; Liu. B.S.C.',
     'Guo Y.; Klink A.; Bartolo P.; Guo W.G.',
     'Huang (黃新棫) X.-Y.; Chen (陳怡妏) Y.-W.; Yang (楊鏡堂) J.-T.',
     'Alshareef M., Jr.; Chang V.-T.',
     <NA>,
     <NA>,
     <NA>,
     <NA>]



"""

import pandas as pd  # type: ignore

from techminer2 import Field
from techminer2.operations.transform_column import transform_column


def _process(text):
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

    #

    text = text.str.replace(",", "", regex=False)
    text = text.str.replace("; ", ";", regex=False)
    text = text.str.replace(";", "; ", regex=False)
    text = text.str.replace(" Jr.", ", Jr.", regex=False)
    #
    # some old database records uses ',' as separator
    # text = text.str.replace(", ", ",", regex=False).str.replace(",", "; ", regex=False)

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


def normalize_raw_authors(root_directory, file: str) -> int:
    """Run authors importer."""

    return transform_column(
        source=Field.AUTH_RAW,
        target=Field.AUTH_NORM,
        function=_process,
        root_directory=root_directory,
        file=file,
    )
