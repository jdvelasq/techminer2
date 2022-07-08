"""
Countries' Production per Year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> countries_production_per_year(
...    directory=directory,
... ).head()
                    num_documents  ...  local_citations_per_year
countries     year                 ...                          
Hong Kong     2016              2  ...                     0.000
United States 2016              1  ...                     0.714
Australia     2017              2  ...                     1.167
China         2017              1  ...                     0.167
Hong Kong     2017              4  ...                     2.333
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_indicators_by_year import column_indicators_by_year


def countries_production_per_year(directory="./"):
    """Countries' production per year."""
    return column_indicators_by_year(
        column="countries",
        directory=directory,
        database="documents",
        use_filter=True,
    )
