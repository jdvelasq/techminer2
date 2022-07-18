"""
World map 
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/world_map.png"
>>> world_map(column="countries", directory=directory).savefig(file_name)
 
.. image:: images/world_map.png
    :width: 700px
    :align: center

"""
# from ._world_map import _world_map
from .tm2.indicators.column_indicators import column_indicators

TEXTLEN = 40


def world_map(
    column,
    metric="num_documents",
    cmap="Greys",
    figsize=(9, 5),
    directory="./",
):

    series = column_indicators(column=column, directory=directory)[metric]
    return _world_map(
        series=series,
        cmap=cmap,
        figsize=figsize,
        title=None,
    )
