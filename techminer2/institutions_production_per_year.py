"""
Institutions' production per year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> institutions_production_per_year(
...    directory=directory,
... ).head()
                                         num_documents  ...  local_citations_per_year
institutions                   pub_year                 ...                          
Agricultural Bank of China CHN 2016                  1  ...                     0.667
Boise State University USA     2016                  1  ...                     0.667
Sungshin Womens University KOR 2016                  1  ...                     0.167
University of Technology POL   2016                  1  ...                     0.500
University of Zurich CHE       2016                  1  ...                     1.167
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_indicators_by_year import column_indicators_by_year


def institutions_production_per_year(directory="./"):
    return column_indicators_by_year(
        column="institutions",
        directory=directory,
    )
