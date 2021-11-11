"""
Top documents (most cited documents)
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> top_documents(directory, n_top=5)
                             authors  pub_year  \\
0                   Lee I; Shin YJ/1      2018   
1      Gomber P; Koch J-A; Siering M      2017   
2  Adhami S; Giudici G; Martinazzi S      2018   
3                  Gabor D; Brooks S      2017   
4                           Ozili PK      2018   
.
                                      document_title  \\
0  Fintech: Ecosystem, business models, investmen...   
1  Digital Finance and FinTech: current research ...   
2  Why do businesses go crypto? An empirical anal...   
3  The digital revolution in financial inclusion:...   
4  Impact of digital finance on financial inclusi...   
.
                         source_name document_id  global_citations  
0                  BUSINESS HORIZONS   2018-0001               201  
1      JOURNAL OF BUSINESS ECONOMICS   2017-0001               171  
2  JOURNAL OF ECONOMICS AND BUSINESS   2018-0002               167  
3              NEW POLITICAL ECONOMY   2017-0002               142  
4              BORSA ISTANBUL REVIEW   2018-0003               124
"""


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
            "document_id",
            "wos_id",
            citations_column,
        ]
    ]

    if n_top is not None:
        documents = documents.head(n_top)

    documents = documents.sort_values(by=citations_column, ascending=False)

    return documents
