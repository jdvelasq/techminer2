from enum import Enum

from .field import Field


class Col(str, Enum):

    PERCENTAGE = "PERCENTAGE"
    CLUSTER = "CLUSTER"
    CLUSTERING = "CLUSTERING"
    COLUMN = "COLUMN"
    CORE = "CORE"
    COUNTERS = "COUNTERS"

    NAME = "NAME"

    NUM_ITEMS = "NUM_ITEMS"
    NUM_REC = "NUM_REC"

    ITEMS = "ITEMS"

    FIELD = "FIELD"

    # -------------------------------------------------------------------------
    # Database
    # -------------------------------------------------------------------------

    RID = Field.REC_ID.value

    COVERAGE = "COVERAGE"
    CUM_SUM_DOCS = "CUM_SUM_DOCS"
    CUM_SUM_ITEMS = "CUM_SUM_ITEMS"

    YEAR = Field.YEAR.value
    YEAR_FIRST = YEAR + "_FIRST"
    YEAR_LAST = YEAR + "_LAST"

    # -------------------------------------------------------------------------
    # Impact
    # -------------------------------------------------------------------------

    AGE = "AGE"

    H_INDEX = "H_INDEX"
    G_INDEX = "G_INDEX"
    M_INDEX = "M_INDEX"

    GCS = Field.GCS.value
    LCS = Field.LCS.value
    OCC = "OCC"

    RANK_OCC = "RANK_OCC"
    RANK_GCS = "RANK_GCS"
    RANK_LCS = "RANK_LCS"

    GCS_PER_YEAR = "GCS_PER_YEAR"
    GCS_PER_YEAR_AVG = "GCS_PER_YEAR_AVG"
    GCS_PER_DOC = "GCS_PER_DOC"

    LCS_PER_YEAR = "LCS_PER_YEAR"
    LCS_PER_DOC = "LCS_PER_DOC"

    # -------------------------------------------------------------------------
    # Social structure
    # -------------------------------------------------------------------------
    SP = "SP"  # single publication
    MP = "MP"  # multiple publications
    MP_RATIO = "MP_RATIO"  # multiple publications ratio

    # -------------------------------------------------------------------------
    # Network-related names
    # -------------------------------------------------------------------------
    NODE = "NODE"

    PAGERANK = "PAGERANK"
    BETWEENNESS = "BETWEENNESS"
    CLOSENESS = "CLOSENESS"
    DEGREE = "DEGREE"
    EIGENVECTOR = "EIGENVECTOR"
    STRENGTH = "STRENGTH"

    # -------------------------------------------------------------------------
    # citation/co-citation/coupling-related names
    # -------------------------------------------------------------------------
    CITED_UNIT = "CITED_UNIT"
    CITING_UNIT = "CITING_UNIT"
