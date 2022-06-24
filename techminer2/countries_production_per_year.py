"""
Countries' production per year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> countries_production_per_year(
...    directory=directory,
... ).head()
                        num_documents  ...  local_citations_per_year
countries     pub_year                 ...                          
china         2016                  1  ...                     0.667
poland        2016                  1  ...                     0.500
south korea   2016                  1  ...                     0.167
switzerland   2016                  2  ...                     3.500
united states 2016                  1  ...                     0.667
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_indicators_by_year import column_indicators_by_year


def countries_production_per_year(directory="./"):
    return column_indicators_by_year(
        column="countries",
        directory=directory,
    )
