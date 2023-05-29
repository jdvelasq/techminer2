"""
Create Concept Grid (TODO)
===============================================================================



Example:
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=2,
...    root_dir=root_dir,
... )
>>> graph = vantagepoint.analyze.cluster_criterion(
...    occ_matrix,
...    community_clustering='louvain',
... )
>>> vantagepoint.analyze.create_concept_grid(graph)



"""

import pandas as pd


def create_concept_grid(graph):
    """TODO: Cluster by PCA"""
