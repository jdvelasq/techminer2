"""
Countries' Production per Year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> countries_production_per_year(
...    directory=directory,
... ).head()


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
