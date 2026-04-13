from enum import Enum

from .field import Field


class CitationUnit(str, Enum):

    AUTH = Field.AUTH_FULL_NAME.value
    CTRY = Field.CTRY_ISO3.value
    DOC = "DOC"
    ORG = Field.ORG.value
    SRC = Field.SRC_ISO4.value
