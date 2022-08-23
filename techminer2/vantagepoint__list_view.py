"""
List View
===============================================================================


>>> directory = "data/regtech/"


>>> from techminer2 import vantagepoint__list_view
>>> vantagepoint__list_view(
...    criterion='author_keywords',
...    directory=directory,
... ).head()
                         OCC  ...  local_citations_per_document
author_keywords               ...                              
regtech                   69  ...                             0
fintech                   42  ...                             1
blockchain                18  ...                             0
artificial intelligence   13  ...                             0
regulatory technology     12  ...                             0
<BLANKLINE>
[5 rows x 5 columns]


>>> from pprint import pprint
>>> pprint(sorted(vantagepoint__list_view("author_keywords", directory=directory).columns.to_list()))
['OCC',
 'global_citations',
 'global_citations_per_document',
 'local_citations',
 'local_citations_per_document']

"""
from .tm2__indicators_by_topic import tm2__indicators_by_topic


def vantagepoint__list_view(
    criterion,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a list of terms with indicators."""

    return tm2__indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
