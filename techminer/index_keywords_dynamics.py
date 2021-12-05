"""
Index keywords dynamics
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/index_keywords_dynamics.png"
>>> index_keywords_dynamics(10, directory=directory).savefig(file_name)

.. image:: images/index_keywords_dynamics.png
    :width: 650px
    :align: center


>>> index_keywords_dynamics(5, directory=directory, plot=False).tail(10)
index_keywords  fintech  financial service  ...  sustainable development  investment
2016                  1                  1  ...                        0           0
2017                  3                  1  ...                        0           2
2018                  9                  4  ...                        0           3
2019                 14                  6  ...                        3           4
2020                 31                 12  ...                        8           8
2021                 48                 19  ...                       12          10
<BLANKLINE>
[6 rows x 5 columns]

"""


from .column_dynamics import column_dynamics


def index_keywords_dynamics(top_n=10, figsize=(8, 6), directory="./", plot=True):

    return column_dynamics(
        "index_keywords",
        top_n=top_n,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
