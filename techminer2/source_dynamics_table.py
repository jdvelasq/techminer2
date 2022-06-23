"""
Source dynamics table
===============================================================================

See :doc:`column indicators by year <column_indicators_by_year>` to obtain a 
`pandas.Dataframe` with the data. 

>>> from techminer2.bibliometrix import *
>>> directory = "data/"

>>> source_dynamics_table(
...     top_n=10, 
...     directory=directory,
... ).tail(5)
iso_source_name  SUSTAINABILITY  ...  PROCEDIA COMPUT SCI
2017                          0  ...                    0
2018                          0  ...                    1
2019                          4  ...                    4
2020                         10  ...                    4
2021                         15  ...                    4
<BLANKLINE>
[5 rows x 10 columns]

"""
from .column_dynamics_table import column_dynamics_table


def source_dynamics_table(
    top_n=10,
    directory="./",
):
    return column_dynamics_table(
        column="iso_source_name",
        top_n=top_n,
        directory=directory,
    )
