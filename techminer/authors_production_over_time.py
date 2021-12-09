"""
Authors Production over Time
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/authors_production_over_time.png"
>>> authors_production_over_time(min_occ=2, directory=directory).savefig(file_name)

.. image:: images/authors_production_over_time.png
    :width: 700px
    :align: center

>>> authors_production_over_time(min_occ=2, directory=directory, plot=False).head()
pub_year    2016  2017  2018  2019  2020  2021
authors                                       
Arqawi S       0     0     0     0     1     1
Bernards N     0     0     0     2     0     0
Budi I         0     0     0     0     1     1
Daragmeh A     0     0     0     0     0     2
Dincer H       0     0     0     0     0     2


"""

from .column_frequency_over_time import column_frequency_over_time


def authors_production_over_time(
    min_occ=2,
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    return column_frequency_over_time(
        column="authors",
        min_occ=min_occ,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
