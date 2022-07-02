"""
Word dynamics table
===============================================================================

See :doc:`column indicators by year <column_indicators_by_year>` to obtain a 
`pandas.Dataframe` with the data. 

>>> from techminer2.bibliometrix import *
>>> directory = "data/"

>>> word_dynamics_table(
...     column="author_keywords",
...     top_n=10,
...     directory=directory,
... ).tail(5)
author_keywords  regtech  fintech  ...  machine learning  regulate
2018                  18       12  ...                 0         2
2019                  31       21  ...                 1         2
2020                  50       32  ...                 4         5
2021                  64       39  ...                 5         6
2022                  70       42  ...                 6         6
<BLANKLINE>
[5 rows x 10 columns]

"""
from .column_dynamics_table import column_dynamics_table


def word_dynamics_table(
    column="author_keywords",
    top_n=10,
    directory="./",
):
    """Makes a dynamics table for a word."""
    return column_dynamics_table(
        column=column,
        top_n=top_n,
        directory=directory,
    )
