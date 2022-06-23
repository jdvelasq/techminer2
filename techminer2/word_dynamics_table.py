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

"""
from .column_dynamics_table import column_dynamics_table


def word_dynamics_table(
    column="author_keywords",
    top_n=10,
    directory="./",
):
    return column_dynamics_table(
        column=column,
        top_n=top_n,
        directory=directory,
    )
