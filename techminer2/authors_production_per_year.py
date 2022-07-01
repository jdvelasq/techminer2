"""
Authors' production per year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> authors_production_per_year(
...    directory=directory,
... ).head()
                  num_documents  ...  local_citations_per_year
authors     year                 ...                          
Arner DW    2016              1  ...                     0.000
Barberis JN 2016              1  ...                     0.000
Baxter LG   2016              1  ...                     0.714
Arner DW    2017              2  ...                     1.167
Barberis JN 2017              2  ...                     1.167
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_indicators_by_year import column_indicators_by_year


def authors_production_per_year(directory="./"):
    """Authors' production per year."""
    return column_indicators_by_year(
        column="authors",
        directory=directory,
        database="documents",
        use_filter=True,
    )
