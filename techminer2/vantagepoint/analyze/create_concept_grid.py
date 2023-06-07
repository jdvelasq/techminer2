# flake8: noqa
"""
Create Concept Grid (TODO)
===============================================================================



Example:
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> graph = vantagepoint.analyze.cluster_column(
...    occ_matrix,
...    community_clustering='louvain',
... )
>>> vantagepoint.analyze.create_concept_grid(graph)


# pylint: disable=line-too-long
"""

import pandas as pd


def create_concept_grid(graph):
    """TODO: Cluster by PCA"""
