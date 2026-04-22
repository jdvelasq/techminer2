from enum import Enum

from .field import Field


class AnalysisUnit(str, Enum):

    AUTH = Field.AUTH_FULL_NAME.value
    CTRY = Field.CTRY_ISO3.value
    DOC = Field.REC_SHORT_NAME.value
    ORG = Field.ORG.value
    SRC = Field.SRC_ISO4.value

    #
    # Concept-related units
    #
    AUTHKW = Field.AUTHKW_NORM.value
    CONCEPT = Field.CONCEPT_NORM.value
    DESCRIPTOR = Field.DESCRIPTOR_NORM.value
    IDXKW = Field.IDXKW_NORM.value
    KW = Field.KW_NORM.value
    WORD = Field.WORD_NORM.value

    #
    # Reference-related units
    #
    CITED_AUTH = Field.AUTH_NORM.value
    CITED_REF = "REF"
    CITED_SRC = Field.SRC_ISO4.value
