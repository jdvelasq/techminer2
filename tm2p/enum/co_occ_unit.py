from enum import Enum

from .field import Field


class CoOccurrenceUnit(str, Enum):

    AUTHKW = Field.AUTHKW_NORM.value
    IDXKW = Field.IDXKW_NORM.value
    KW = Field.KW_NORM.value
    CONCEPT = Field.CONCEPT_NORM.value
    WORD = Field.WORD_NORM.value
