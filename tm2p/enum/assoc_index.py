from enum import Enum


class AssociationIndex(str, Enum):

    # -------------------------------------------------------------------------
    # From VOSviewer:
    # -------------------------------------------------------------------------
    ASSOCIATION_STRENGTH = "ASSOCIATION_STRENGTH"

    # -------------------------------------------------------------------------
    # From TLAB:
    # -------------------------------------------------------------------------
    DICE = "DICE"
    EQUIVALENCE = "EQUIVALENCE"
    INCLUSION = "INCLUSION"
    JACCARD = "JACCARD"
    MUTUALINFO = "MUTUALINFO"
    SALTON = "SALTON"
    COSINE = "COSINE"
