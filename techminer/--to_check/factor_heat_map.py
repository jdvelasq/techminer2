"""
Factor Analysis ---  heat map
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"


.. image:: images/factor_heat_map.png
    :width: 500px
    :align: center

"""
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

from .heat_map import heat_map
from .tf_matrix import tf_matrix
from .utils import adds_counters_to_axis
from .utils.io import load_filtered_documents

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def factor_heat_map(factor_matrix, cmap="Greys", figsize=(6, 6), fontsize=9, **kwargs):
    # computos
    matrix = factor_matrix.copy()
    # matrix.columns = matrix.columns.get_level_values(0)

    return heat_map(
        matrix,
        cmap="Greys",
        figsize=(6, 6),
        fontsize=9,
        **kwargs,
    )
