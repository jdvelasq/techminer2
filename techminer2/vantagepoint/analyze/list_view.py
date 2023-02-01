"""
List View
===============================================================================


>>> directory = "data/regtech/"


>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.list_view(
...    criterion='author_keywords',
...    directory=directory,
... ).head()
                       OCC  ...  local_citations_per_document
author_keywords             ...                              
regtech                 28  ...                             2
fintech                 12  ...                             4
compliance               7  ...                             1
regulatory technology    7  ...                             2
regulation               5  ...                             4
<BLANKLINE>
[5 rows x 5 columns]


>>> from pprint import pprint
>>> pprint(sorted(vantagepoint.analyze.list_view("author_keywords", directory=directory).columns.to_list()))
['OCC',
 'global_citations',
 'global_citations_per_document',
 'local_citations',
 'local_citations_per_document']

"""
from ...tm2.indicators.tm2__indicators_by_topic import tm2__indicators_by_topic


def list_view(
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
