"""
Authors' Production per Year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> authors_production_per_year(
...    directory=directory,
... ).head()
                   OCC  ...  local_citations_per_year
authors      year       ...                          
Abdullah Y   2022    1  ...                     0.000
Abi-Lahoud E 2018    1  ...                     0.000
Ajmi JA      2021    1  ...                     0.500
Al Haider N  2020    1  ...                     0.333
Alam TM      2021    1  ...                     0.000
<BLANKLINE>
[5 rows x 7 columns]


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
