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

    ACRONYM = "acronyms.the.txt"
    CONCEPT = "concept.the.txt"
    CTRY = "ctry.the.txt"
    ORG = "org.the.txt"
