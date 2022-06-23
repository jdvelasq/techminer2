"""
Countries' production over time (TODO)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/countries_production_over_time.png"
>>> countries_production_over_time(
...    min_occ=2, 
...    directory=directory,
... ).savefig(file_name)

.. image:: images/countries_production_over_time.png
    :width: 700px
    :align: center

>>> countries_production_over_time(
...     min_occ=2, 
...     directory=directory, 
...     plot=False,
... ).head()


"""

from .dotted_gantt_chart import dotted_gantt_chart


def countries_production_over_time(
    min_occ=2,
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    return dotted_gantt_chart(
        column="countries",
        min_occ=min_occ,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
