"""
Annual Occurrence Matrix
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> annual_occurrence_matrix('authors',  min_occ=3, directory=directory).head(10)
pub_year    2019  2020  2021
authors                     
Hornuf L       1     1     1
Rabbani MR     0     2     1
Wojcik D       0     3     2


"""


from .column_indicators import column_indicators
from .column_indicators_by_year import column_indicators_by_year


def annual_occurrence_matrix(column, sep=";", min_occ=1, directory="./"):

    indicators_by_year = column_indicators_by_year(directory=directory, column=column)
    indicators = column_indicators(column=column, sep=sep, directory=directory)
    indicators = indicators.sort_values("OCC", ascending=False)
    indicators = indicators[indicators["OCC"] >= min_occ]

    indicators_by_year = indicators_by_year.loc[
        indicators.index,
    ]

    indicators_by_year = indicators_by_year.assign(
        year=indicators_by_year.index.get_level_values("year")
    )
    indicators_by_year.index = indicators_by_year.index.get_level_values(0)

    indicators_by_year = indicators_by_year[["year", "OCC"]]
    indicators_by_year = indicators_by_year.pivot(columns="year")
    indicators_by_year.columns = indicators_by_year.columns.droplevel(0)
    indicators_by_year = indicators_by_year.fillna(0)
    indicators_by_year = indicators_by_year.astype(int)

    return indicators_by_year
