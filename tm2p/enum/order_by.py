from enum import Enum

from .col import Col


class UnitOrderBy(str, Enum):

    OCC = Col.OCC
    GCS = Col.GCS
    LCS = Col.LCS

    LCS_PER_YEAR = Col.LCS_PER_YEAR
    GCS_PER_YEAR = Col.GCS_PER_YEAR

    GCS_PER_YEAR_AVG = Col.GCS_PER_YEAR_AVG

    H_INDEX = Col.H_INDEX
    G_INDEX = Col.G_INDEX
    M_INDEX = Col.M_INDEX


class RecordOrderBy(str, Enum):

    GCS_HIGHEST = "GCS_HIGHEST"
    GCS_LOWEST = "GCS_LOWEST"

    LCS_HIGHEST = "LCS_HIGHEST"
    LCS_LOWEST = "LCS_LOWEST"

    AUTH_A_TO_Z = "AUTH_A_TO_Z"
    AUTH_Z_TO_A = "AUTH_Z_TO_A"

    YEAR_NEWEST = "YEAR_NEWEST"
    YEAR_OLDEST = "YEAR_OLDEST"

    SRC_A_TO_Z = "SRC_A_TO_Z"
    SRC_Z_TO_A = "SRC_Z_TO_A"
