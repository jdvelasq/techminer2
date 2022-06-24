"""
Authors' production per year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> authors_production_per_year(
...    directory=directory,
... ).head()
                    num_documents  ...  local_citations_per_year
authors   pub_year                 ...                          
Dolata M  2016                  1  ...                     1.167
Hong S    2016                  1  ...                     0.167
Hung J-L  2016                  1  ...                     0.667
Kim K     2016                  1  ...                     0.167
Kotarba M 2016                  1  ...                     0.500
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_indicators_by_year import column_indicators_by_year


def authors_production_per_year(directory="./"):
    return column_indicators_by_year(
        column="authors",
        directory=directory,
    )
