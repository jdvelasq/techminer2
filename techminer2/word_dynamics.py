"""
Word Dynamics
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/word_dynamics.png"
>>> word_dynamics('author_keywords', 10, directory=directory).savefig(file_name)

.. image:: images/word_dynamics.png
    :width: 700px
    :align: center


>>> word_dynamics("author_keywords", 5, directory=directory, plot=False).tail()
author_keywords  fintech  financial technologies  ...  blockchain  innovation
2017                  10                       1  ...           2           3
2018                  26                       7  ...           5           6
2019                  42                      11  ...           9           9
2020                  80                      16  ...          11          12
2021                 139                      28  ...          17          13
<BLANKLINE>
[5 rows x 5 columns]

"""
from .column_dynamics import column_dynamics


def word_dynamics(column, top_n=10, figsize=(8, 6), directory="./", plot=True):

    return column_dynamics(
        column=column,
        top_n=top_n,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
