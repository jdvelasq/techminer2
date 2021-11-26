"""
Source growth table
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> source_growth_table(directory, n_sources=5).tail(10)
iso_source_name  SUSTAINABILITY  ...  LECT NOTES COMPUT SCI
2013                          0  ...                      0
2014                          0  ...                      0
2015                          0  ...                      0
2016                          0  ...                      0
2017                          0  ...                      3
2018                          1  ...                      7
2019                          7  ...                     10
2020                         15  ...                     16
2021                         28  ...                     20
2022                         28  ...                     20
<BLANKLINE>
[10 rows x 5 columns]

"""
import numpy as np
import pandas as pd

from .column_indicators_by_year import column_indicators_by_year


def source_growth_table(directory, n_sources=10):

    source_growth = column_indicators_by_year(directory, column="iso_source_name")[
        ["pub_year", "num_documents"]
    ]
    source_growth = source_growth.pivot(columns="pub_year")
    source_growth = source_growth.transpose()
    source_growth.index = source_growth.index.get_level_values(1)

    year_range = list(range(source_growth.index.min(), source_growth.index.max() + 1))
    missing_years = [year for year in year_range if year not in source_growth.index]
    pdf = pd.DataFrame(
        np.zeros((len(missing_years), len(source_growth.columns))),
        index=missing_years,
        columns=source_growth.columns,
    )
    source_growth = source_growth.append(pdf)
    source_growth = source_growth.sort_index(axis="index")
    source_growth = source_growth.fillna(0)

    num_documents = source_growth.sum(axis=0)
    num_documents = num_documents.sort_values(ascending=False)

    source_growth = source_growth[num_documents.index[:n_sources]]
    source_growth = source_growth.cumsum()
    source_growth = source_growth.astype(int)

    return source_growth
