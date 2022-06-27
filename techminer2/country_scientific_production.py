"""
Country Scientific Production
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/country_scientific_production.png"
>>> country_scientific_production(directory=directory).savefig(file_name)
 
.. image:: images/country_scientific_production.png
    :width: 700px
    :align: center


"""
from os.path import dirname, join

import matplotlib.pyplot as plt
import numpy as np

from ._world_map import _world_map
from .column_indicators import column_indicators

TEXTLEN = 40


def country_scientific_production(
    cmap="Blues",
    figsize=(9, 5),
    directory="./",
):

    """Worldmap plot with the number of documents per country."""

    series = column_indicators("countries", directory=directory).num_documents

    return _world_map(
        series=series,
        cmap=cmap,
        figsize=figsize,
        title="Country Scientific Production",
    )
