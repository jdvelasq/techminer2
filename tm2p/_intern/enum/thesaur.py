from enum import Enum


class ThField(Enum):

    CHANGED = "CHANGED"
    IS_KEYWORD = "IS_KEYWORD"
    OCC = "OCC"
    OLD = "OLD"
    PREFERRED = "PREFERRED"
    SIGNATURE = "SIGNATURE"
    VARIANT = "VARIANT"


class ThFile(Enum):

    ORG = "org.the.txt"
    CTRY = "ctry.the.txt"
    CONCEPT = "concept.the.txt"
