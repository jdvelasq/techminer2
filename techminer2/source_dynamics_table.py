"""
Source dynamics table
===============================================================================

See :doc:`column indicators by year <column_indicators_by_year>` to obtain a 
`pandas.Dataframe` with the data. 

>>> from techminer2.bibliometrix import *
>>> directory = "data/regtech/"

>>> source_dynamics_table(
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
from .column_dynamics_table import column_dynamics_table


def source_dynamics_table(
    top_n=10,
    directory="./",
):
    return column_dynamics_table(
        column="source_abbr",
        top_n=top_n,
        directory=directory,
    )
