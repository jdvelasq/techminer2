"""
Document indicators
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> document_indicators(n_top=5, directory=directory)
                                     authors  ...  global_citations
0  Gomber P; Kauffman RJ; Parker C; Weber BW  ...               220
1                          Gabor D; Brooks S  ...               146
2                                Schueffel P  ...               106
3     Leong C; Tan B; Xiao X; Tan FTC; Sun Y  ...               101
4                         Haddad C; Hornuf L  ...                97
<BLANKLINE>
[5 rows x 8 columns]

>>> document_indicators(n_top=5, directory=directory).document_id
0    Gomber P et al, 2018, J MANAGE INF SYST, V35, ...
1     Gabor D et al, 2017, NEW POLIT ECON, V22, P423.0
2    Schueffel P et al, 2016, J INNOV MANAG, V4, P32.0
3    Leong C et al, 2017, INT J INF MANAGE, V37, P92.0
4     Haddad C et al, 2019, SMALL BUS ECON, V53, P81.0
Name: document_id, dtype: object

"""

import os

from techminer.utils import print_documents

from .utils import load_filtered_documents


def document_indicators(
    global_citations=True,
    normalized_citations=False,
    n_top=50,
    directory="./",
):
    """
    Returns the most cited documents of the given directory or records.

    Parameters
    ----------
    dirpath_or_records: str
        path to the directory or the records object.
    global_citations: bool
        Whether to use global citations or not.
    normalized_citations: bool
        Whether to use normalized citations or not.

    Returns
    -------
    most_cited_documents: pandas.DataFrame
        Most cited documents.
    """

    documents = load_filtered_documents(directory)

    max_pub_year = documents.pub_year.dropna().max()

    documents["global_normalized_citations"] = documents.global_citations.map(
        lambda w: round(w / max_pub_year, 3), na_action="ignore"
    )

    documents["local_normalized_citations"] = documents.local_citations.map(
        lambda w: round(w / max_pub_year, 3), na_action="ignore"
    )

    documents["global_citations"] = documents.global_citations.map(
        int, na_action="ignore"
    )

    citations_column = {
        (True, True): "global_normalized_citations",
        (True, False): "global_citations",
        (False, True): "local_normalized_citations",
        (False, False): "local_citations",
    }[(global_citations, normalized_citations)]

    documents = documents.sort_values(citations_column, ascending=False)
    documents = documents.reset_index(drop=True)

    documents = documents[
        [
            "authors",
            "pub_year",
            "document_title",
            "source_name",
            "iso_source_name",
            "record_no",
            "document_id",
            "abstract",
            citations_column,
        ]
    ]

    if n_top is not None:
        documents = documents.head(n_top)

    documents = documents.sort_values(by=citations_column, ascending=False)

    with open(os.path.join(directory, "top_documents.txt"), "wt") as file:
        print_documents(documents, file=file)

    documents.pop("abstract")

    return documents
