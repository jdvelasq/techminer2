"""
Column Gantt Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/column_gantt_chart.png"
>>> column_gantt_chart('authors', min_occ=2, directory=directory).savefig(file_name)

.. image:: images/column_gantt_chart.png
    :width: 700px
    :align: center

>>> column_gantt_chart('authors', min_occ=2, directory=directory, plot=False).head()
pub_year    2016  2017  2018  2019  2020  2021
authors                                       
Arqawi S       0     0     0     0     1     1
Bernards N     0     0     0     2     0     0
Budi I         0     0     0     0     1     1
Daragmeh A     0     0     0     0     0     2
Dincer H       0     0     0     0     0     2


"""


from .annual_occurrence_matrix import annual_occurrence_matrix
from .dotted_gantt_chart import dotted_gantt_chart


def column_gantt_chart(
    column,
    min_occ=2,
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    production = annual_occurrence_matrix(
        column,
        min_occ=min_occ,
        directory=directory,
    )
    if plot is False:
        return production

    return dotted_gantt_chart(production, figsize=figsize)
