"""
Top documents (most cited documents)
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> top_documents(directory, n_top=5)
                                     authors  ...  global_citations
0                         Au YA; Kauffman RJ  ...               250
1               Aste T; Tasca P; Di Matteo T  ...               233
2  Gomber P; Kauffman RJ; Parker C; Weber BW  ...               219
3                           Lee I; Shin YJ/1  ...               210
4              Gomber P; Koch J-A; Siering M  ...               179
<BLANKLINE>
[5 rows x 8 columns]

>>> top_documents(directory, n_top=5).document_id
0    Au YA et al, 2008, ELECT COMMER RES APPL, V7, ...
1               Aste T et al, 2017, COMPUTER, V50, P18
2    Gomber P et al, 2018, J MANAGE INF SYST, V35, ...
3               Lee I et al, 2018, BUS HORIZ, V61, P35
4          Gomber P et al, 2017, J BUS ECON, V87, P537
Name: document_id, dtype: object

"""

import os

from techminer.utils import print_documents

from .utils import load_filtered_documents


def top_documents(
    directory,
    global_citations=True,
    normalized_citations=False,
    n_top=50,
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
