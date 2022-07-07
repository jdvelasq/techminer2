"""
Terms List
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> make_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... ).head(10)
                                   OCC  ...  local_citations_per_document
author_keywords                         ...                              
regtech                             70  ...                             0
fintech                             42  ...                             1
blockchain                          18  ...                             0
artificial intelligence             13  ...                             0
regulatory technologies (regtech)   12  ...                             0
compliance                          12  ...                             0
financial technologies               9  ...                             0
financial regulation                 8  ...                             1
regulate                             6  ...                             2
machine learning                     6  ...                             0
<BLANKLINE>
[10 rows x 5 columns]


>>> from pprint import pprint
>>> pprint(sorted(make_list("author_keywords", directory=directory).columns.to_list()))
['OCC',
 'global_citations',
 'global_citations_per_document',
 'local_citations',
 'local_citations_per_document']

"""
from .column_indicators import column_indicators


def terms_list(
    column,
    metric="OCC",
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    database="documents",
):
    """Creates a list of terms with indicators."""

    indicators = column_indicators(
        column=column,
        directory=directory,
        database=database,
        use_filter=(database == "documents"),
        sep=";",
    )

    indicators = indicators.sort_values(metric, ascending=False)

    if min_occ is not None:
        indicators = indicators[indicators.OCC >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators.OCC <= max_occ]
    if top_n is not None:
        indicators = indicators.head(top_n)

    return indicators
