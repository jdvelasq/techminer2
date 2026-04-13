from enum import Enum

from .field import Field


class CollaborationUnit(str, Enum):

    AUTH = Field.AUTH_FULL_NAME.value
    CTRY = Field.CTRY_ISO3.value
    ORG = Field.ORG.value
