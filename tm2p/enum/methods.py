from enum import Enum


class AssociationIndex(str, Enum):

    #
    # From VOSviewer:
    #
    ASSOCIATION_STRENGTH = "ASSOCIATION_STRENGTH"

    #
    # From TLAB:
    #
    DICE = "DICE"
    EQUIVALENCE = "EQUIVALENCE"
    INCLUSION = "INCLUSION"
    JACCARD = "JACCARD"
    MUTUALINFO = "MUTUALINFO"
    SALTON = "SALTON"
    COSINE = "COSINE"


class Correlation(str, Enum):

    PEARSON = "PEARSON"
    SPEARMAN = "SPEARMAN"
    KENDALL = "KENDALL"
    COSINE = "COSINE"
    MAXPROPORTIONAL = "MAXPROPORTIONAL"


class GraphClusteringAlgorithm(str, Enum):

    INFOMAP = "INFOMAP"
    LEIDEN = "LEIDEN"
    LOUVAIN = "LOUVAIN"
    WALKTRAP = "WALKTRAP"


class Scaling(str, Enum):

    LINEAR = "LINEAR"
    LOG = "LOG"
    SQRT = "SQRT"


class NodeSizeMetric(str, Enum):

    GCS = "GCS"
    LINKS = "LINKS"
    OCC = "OCC"
    TLS = "TLS"
