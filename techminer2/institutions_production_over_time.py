"""
Institutions' production over time (TODO)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/institutions_production_over_time.png"
>>> institutions_production_over_time(
...    min_occ=2, 
...    directory=directory,
... ).savefig(file_name)

.. image:: images/institutions_production_over_time.png
    :width: 700px
    :align: center

>>> institutions_production_over_time(
...     min_occ=2, 
...     directory=directory, 
...     plot=False,
... ).head()


"""

from .dotted_gantt_chart import dotted_gantt_chart


def institutions_production_over_time(
    min_occ=2,
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    return dotted_gantt_chart(
        column="institutions",
        min_occ=min_occ,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
