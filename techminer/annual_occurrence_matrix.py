"""
Annual occurrence matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> annual_occurrence_matrix(directory, 'authors',  min_occ=3).head(10)
pub_year       2008  2015  2016  2017  2018  2019  2020  2021  2022
authors                                                            
Aas TH            0     0     0     0     0     0     1     2     0
Abdeldayem MM     0     0     0     0     0     0     2     2     0
Al Dulaimi SH     0     0     0     0     0     0     2     1     0
Al-Dmour A        0     0     0     0     0     0     1     2     0
Al-Dmour H        0     0     0     0     0     0     1     2     0
Al-Dmour R        0     0     0     0     0     0     1     2     0
Alaassar A        0     0     0     0     0     0     1     2     0
Ali MAM           0     0     0     0     0     0     0     3     0
Almunawar MN      0     0     0     0     0     1     1     1     0
Anshari M         0     0     0     0     0     1     1     2     0


"""


from .column_indicators import column_indicators
from .column_indicators_by_year import column_indicators_by_year


def annual_occurrence_matrix(directory, column, sep="; ", min_occ=1):

    indicators_by_year = column_indicators_by_year(directory, column, sep=sep)
    indicators = column_indicators(directory, column, sep=sep)
    indicators = indicators.sort_values("num_documents", ascending=False)
    indicators = indicators[indicators["num_documents"] >= min_occ]

    indicators_by_year = indicators_by_year.loc[
        indicators.index,
    ]

    indicators_by_year = indicators_by_year[["pub_year", "num_documents"]]
    indicators_by_year = indicators_by_year.pivot(columns="pub_year")
    indicators_by_year.columns = indicators_by_year.columns.droplevel(0)
    indicators_by_year = indicators_by_year.fillna(0)
    indicators_by_year = indicators_by_year.astype(int)

    return indicators_by_year
