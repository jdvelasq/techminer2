"""
Column dynamics table
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> column_dynamics_table(
...     column="source_abbr", 
...     top_n=10, 
...     directory=directory,
... ).tail(5)
source_abbr  CEUR WORKSHOP PROC  ...  LECT NOTES NETWORKS SYST
2018                          3  ...                         0
2019                          3  ...                         0
2020                          4  ...                         0
2021                          5  ...                         0
2022                          5  ...                         2
<BLANKLINE>
[5 rows x 10 columns]

"""
import numpy as np
import pandas as pd

from .column_indicators_by_year import column_indicators_by_year


def column_dynamics_table(
    column,
    top_n=10,
    directory="./",
):

    dynamics = column_indicators_by_year(directory=directory, column=column)
    dynamics = dynamics.assign(year=dynamics.index.get_level_values(1))
    dynamics.index = dynamics.index.get_level_values(0)

    dynamics = dynamics[["year", "num_documents"]].copy()
    dynamics = dynamics.pivot(columns="year")
    dynamics = dynamics.transpose()
    dynamics.index = dynamics.index.get_level_values(1)

    year_range = list(range(dynamics.index.min(), dynamics.index.max() + 1))
    missing_years = [year for year in year_range if year not in dynamics.index]
    pdf = pd.DataFrame(
        np.zeros((len(missing_years), len(dynamics.columns))),
        index=missing_years,
        columns=dynamics.columns,
    )
    dynamics = dynamics.append(pdf)
    dynamics = dynamics.sort_index(axis="index")
    dynamics = dynamics.fillna(0)

    num_documents = dynamics.sum(axis=0)
    num_documents = num_documents.sort_values(ascending=False)

    dynamics = dynamics[num_documents.index[:top_n]]
    dynamics = dynamics.cumsum()
    dynamics = dynamics.astype(int)

    return dynamics
