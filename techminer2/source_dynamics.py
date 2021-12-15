"""
Source Dynamics
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/source_dynamics.png"
>>> source_dynamics(10, directory=directory).savefig(file_name)

.. image:: images/source_dynamics.png
    :width: 700px
    :align: center


>>> source_dynamics(5, directory=directory, plot=False).tail()
iso_source_name  SUSTAINABILITY  ...  FRONTIER ARTIF INTELL
2017                          0  ...                      0
2018                          0  ...                      1
2019                          4  ...                      1
2020                         10  ...                      4
2021                         15  ...                      5
<BLANKLINE>
[5 rows x 5 columns]

"""
from .column_dynamics import column_dynamics


def source_dynamics(top_n=10, figsize=(8, 6), directory="./", plot=True):

    return column_dynamics(
        column="iso_source_name",
        top_n=top_n,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
