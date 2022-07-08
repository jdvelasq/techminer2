"""
Institutions' Production per Year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> institutions_production_per_year(
...    directory=directory,
... ).head()
                                                         num_documents  ...  local_citations_per_year
institutions                                       year                 ...                          
Asian Institute of International Financial Law CHN 2016              1  ...                     0.000
Duke University School of Law USA                  2016              1  ...                     0.714
Hku Asia America Institute In Transnational Law... 2016              1  ...                     0.000
Asian Institute of International Financial Law CHN 2017              2  ...                     1.167
Centre for Law AUS                                 2017              1  ...                     1.000
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_indicators_by_year import column_indicators_by_year


def institutions_production_per_year(directory="./"):
    """Institutions' production per year."""
    return column_indicators_by_year(
        column="institutions",
        directory=directory,
        database="documents",
        use_filter=True,
    )
