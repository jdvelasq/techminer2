"""
Word Dynamics
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/word_dynamics.png"
>>> word_dynamics('author_keywords', 10, directory=directory).savefig(file_name)

.. image:: images/word_dynamics.png
    :width: 700px
    :align: center


>>> word_dynamics("author_keywords", 5, directory=directory, plot=False).tail()
author_keywords  fintech  financial technologies  ...  block-chain  innovating
2017                  10                       1  ...            2           3
2018                  26                       7  ...            5           6
2019                  42                      11  ...            9           9
2020                  80                      16  ...           11          12
2021                 139                      28  ...           17          13
<BLANKLINE>
[5 rows x 5 columns]

"""
from .column_dynamics import column_dynamics

word_dynamics = column_dynamics
