from enum import Enum

from .field import Field


class CouplingUnit(str, Enum):

    AUTH = Field.AUTH_FULL_NAME.value
    CTRY = Field.CTRY_ISO3.value
    DOC = Field.REC_SHORT_NAME.value
    ORG = Field.ORG.value
    SRC = Field.SRC_ISO4.value
