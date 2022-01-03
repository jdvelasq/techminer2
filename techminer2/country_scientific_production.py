"""
Country Scientific Production
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/country_scientific_production.png"
>>> country_scientific_production(directory=directory).savefig(file_name)
 
.. image:: images/country_scientific_production.png
    :width: 700px
    :align: center


# >>> from IPython.display import display
# >>> import ipywidgets as widgets
# >>> display(widgets.HTML("<h3>Country Scientific Production</h3>"))
# HTML(value='<h3>Country Scientific Production</h3>')

# >>> import matplotlib.pyplot as plt
# >>> fig, ax = plt.subplots() 
# >>> ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# >>> display(fig)

"""
import json
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
