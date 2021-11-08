"""
Auto-correlation --- heat map
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> matrix = auto_corr_matrix(directory, column='authors', min_occ=4)
>>> auto_corr_heat_map(matrix, num_terms=10)

.. image:: images/auto_corr_heat_map.png
    :width: 400px
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


def auto_corr_heat_map(
    auto_corr_matrix, cmap="Greys", figsize=(6, 6), fontsize=9, **kwargs
):
    # computos
    matrix = auto_corr_matrix.copy()

    return heat_map(
        matrix,
        cmap="Greys",
        figsize=(6, 6),
        fontsize=9,
        **kwargs,
    )
