from enum import Enum


class ThField(str, Enum):

    CHANGED = "CHANGED"
    IS_KEYWORD = "IS_KEYWORD"
    OCC = "OCC"
    OLD = "OLD"
    PREFERRED = "PREFERRED"
    SIGNATURE = "SIGNATURE"
    VARIANT = "VARIANT"


class ThFile(str, Enum):

    ORG = "org.the.txt"
    CTRY = "ctry.the.txt"
    CONCEPT = "concept.the.txt"
