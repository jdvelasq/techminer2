from enum import Enum

from .cols import Cols


class UnitOrderBy(str, Enum):

    OCC = Cols.OCC
    GCS = Cols.GCS
    LCS = Cols.LCS

    LCS_PER_YEAR = Cols.LCS_PER_YEAR
    GCS_PER_YEAR = Cols.GCS_PER_YEAR

    GCS_PER_YEAR_AVG = Cols.GCS_PER_YEAR_AVG

    H_INDEX = Cols.H_INDEX
    G_INDEX = Cols.G_INDEX
    M_INDEX = Cols.M_INDEX


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
