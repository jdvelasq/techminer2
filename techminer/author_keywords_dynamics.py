"""
Author keywords dynamics
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/author_keywords_dynamics.png"
>>> author_keywords_dynamics(10, directory=directory).savefig(file_name)

.. image:: images/author_keywords_dynamics.png
    :width: 650px
    :align: center


>>> author_keywords_dynamics(5, directory=directory, plot=False).tail(10)
author_keywords  fintech  financial technologies  ...  blockchain  innovation
2016                   4                       1  ...           0           2
2017                  10                       1  ...           2           3
2018                  26                       7  ...           5           6
2019                  42                      11  ...           9           9
2020                  80                      16  ...          11          12
2021                 139                      28  ...          17          13
<BLANKLINE>
[6 rows x 5 columns]

"""


from .column_dynamics import column_dynamics


def author_keywords_dynamics(top_n=10, figsize=(8, 6), directory="./", plot=True):

    return column_dynamics(
        "author_keywords",
        top_n=top_n,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
