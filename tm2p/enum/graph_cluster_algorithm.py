from enum import Enum


class GraphClusteringAlgorithm(str, Enum):

    INFOMAP = "INFOMAP"
    LEIDEN = "LEIDEN"
    LOUVAIN = "LOUVAIN"
    WALKTRAP = "WALKTRAP"
