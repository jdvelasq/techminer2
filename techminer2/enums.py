from enum import Enum


class CorpusField(Enum):

    # ==========================================================================
    # Citation information
    # ==========================================================================

    #
    # Authors
    #
    AUTH_ID_RAW = "AUTH_ID_RAW"
    AUTH_ID_NORM = "AUTH_ID_NORM"

    AUTH_FULL = "AUTH_FULL"
    AUTH_RAW = "AUTH_RAW"
    AUTH_DISAMB = "AUTH_DISAMB"
    AUTH_NORM = "AUTH_NORM"
    AUTH_FIRST = "AUTH_FIRST"

    #
    # Document title
    #
    TITLE_RAW = "TITLE_RAW"
    TITLE_TOK = "TITLE_TOK"

    #
    # Year
    #
    PUBYEAR = "PUBYEAR"

    #
    # EID
    #
    ART_NO = "ART_NO"
    EID = "EID"
    LINK = "LINK"

    #
    # Source title & subject area
    #
    SRC_TITLE_RAW = "SRC_TITLE_RAW"
    SRC_TITLE_NORM = "SRC_TITLE_NORM"
    SUBJ_AREA = "SUBJ_AREA"

    #
    # Volume, issues, pages
    #
    VOL = "VOL"
    ISSUE = "ISSUE"
    PAGE_FIRST = "PAGE_FIRST"
    PAGE_LAST = "PAGE_LAST"
    PAGE_COUNT = "PAGE_COUNT"

    #
    # Citation count
    #
    CIT_COUNT_GLOBAL = "CIT_COUNT_GLOBAL"
    CIT_COUNT_LOCAL = "CIT_COUNT_LOCAL"

    #
    # Source & document type
    #
    SOURCE = "SOURCE"
    DOC_TYPE_RAW = "DOC_TYPE_RAW"
    DOC_TYPE_NORM = "DOC_TYPE_NORM"

    #
    # Publication stage
    #
    PUBSTAGE = "PUBSTAGE"

    #
    # DOI
    #
    DOI = "DOI"

    #
    # Open access
    #
    OA = "OPEN_ACCESS"

    # ==========================================================================
    # Bibliographical information
    # ==========================================================================

    #
    # Affiliations
    #
    AUTH_AFFIL = "AUTH_AFFIL"
    AFFIL_RAW = "AFFIL_RAW"

    COUNTRY = "COUNTRY"
    COUNTRY_AUTH_FIRST = "COUNTRY_AUTH_FIRST"
    COUNTRY_AND_AFFIL = "COUNTRY_AND_AFFIL"

    ORG = "ORG"
    ORG_AUTH_FIRST = "ORG_AUTH_FIRST"
    ORG_AND_AFFIL = "ORG_AND_AFFIL"

    REGION = "REGION"
    SUBREGION = "SUBREGION"

    #
    # Serial identifiers
    #
    EISSN = "EISSN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISSNP = "ISSNP"

    #
    # PubMed ID
    #
    PUBMED = "PUBMED"

    #
    # Publisher
    #
    PUBLISHER = "PUBLISHER"

    #
    # Editor
    #
    EDITOR = "EDITOR"

    #
    # Language
    #
    LANGUAGE = "LANGUAGE"

    #
    # Correspondence address
    #
    CORRESP = "CORRESP"

    #
    # Abbreviated source title
    #
    SRC_TITLE_ABBR_NORM = "SRC_TITLE_ABBR_NORM"
    SRC_TITLE_ABBR_RAW = "SRC_TITLE_ABBR_RAW"

    # ==========================================================================
    # Abstract & keywords
    # ==========================================================================

    #
    # Abstract
    #
    ABS_RAW = "ABS_RAW"
    ABS_TOK = "ABS_TOK"

    #
    # Author keywords
    #
    AUTH_KEY_RAW = "AUTH_KEY_RAW"
    AUTH_KEY_TOK = "AUTH_KEY_TOK"
    AUTH_KEY_NORM = "AUTH_KEY_NORM"

    #
    # Index keywords
    #
    IDX_KEY_RAW = "IDX_KEY_RAW"
    IDX_KEY_TOK = "IDX_KEY_TOK"
    IDX_KEY_NORM = "IDX_KEY_NORM"

    #
    # Hybrid keywords (author + index)
    #
    HYB_KEY_TOK = "HYB_KEY_TOK"
    HYB_KEY_NORM = "HYB_KEY_NORM"

    # ==========================================================================
    # Noun phrases & words
    # ==========================================================================

    #
    # Noun phrases extracted from abstract and title
    #
    NP_TEXTBLOB = "NP_TEXTBLOB"
    NP_SPACY = "NP_SPACY"

    #
    # Abstract and title text with NP in uppercase
    #
    ABS_TOK_NP_UPPER = "ABS_TOK_NP_UPPER"
    TITLE_TOK_NP_UPPER = "TITLE_TOK_NP_UPPER"

    #
    # Abstract and title text with WORDS in uppercase
    #
    ABS_TOK_WORD_UPPER = "ABS_TOK_WORD_UPPER"
    TITLE_TOK_WORD_UPPER = "TITLE_TOK_WORD_UPPER"

    #
    # Noun phrases extracted from abstract and title (upper case in text)
    #
    ABS_NP_TOK = "ABS_NP_TOK"
    TITLE_NP_TOK = "TITLE_NP_TOK"

    #
    # Words extracted from abstract and title (upper case in text)
    #
    ABS_WORD_TOK = "ABS_WORD_TOK"
    TITLE_WORD_TOK = "TITLE_WORD_TOK"

    #
    # Noun phrases and words from abstract and title
    #
    NP_TOK = "NP_TOK"
    WORD_TOK = "WORD_TOK"

    #
    # Hybrid keywords + NP
    #
    KEY_AND_NP_TOK = "KEY_AND_NP_TOK"
    KEY_AND_NP_NORM = "KEY_AND_NP_NORM"

    #
    # Hybrid keywords + WORDs
    #
    KEY_AND_WORD_TOK = "KEY_AND_WORD_TOK"
    KEY_AND_WORD_NORM = "KEY_AND_WORD_NORM"

    #
    # Term = Hybrid keyword + NP + WORD
    #
    TERM_TOK = "TERM_TOK"
    TERM_NORM = "TERM_NORM"

    # ==========================================================================
    # Funding details
    # ==========================================================================

    #
    # Acronym
    #
    ACRONYM = "ACRONYM"

    #
    # Funding text
    #
    FUND_DETAILS = "FUND_DETAILS"
    FUND_SPONSORS = "FUND_SPONSORS"
    FUND_TEXTS = "FUND_TEXTS"

    # ==========================================================================
    # Other information
    # ==========================================================================

    #
    # Tradenames & manufacturers
    #
    TRADENAME = "TRADENAME"
    MANUFACTURER = "MANUFACTURER"

    #
    # Accession numbers & chemicals
    #
    CAS_REG_NUMBER = "CAS_REG_NUMBER"
    CODEN = "CODEN"
    SEQ_NUMBER = "SEQ_NUMBER"

    #
    # Conference information
    #
    CONF_CODE = "CONF_CODE"
    CONF_DATE = "CONF_DATE"
    CONF_LOC = "CONF_LOC"
    CONF_NAME = "CONF_NAME"

    #
    # References
    #
    REF_RAW = "REF_RAW"
    REF_NORM = "REF_NORM"
    REF_AND_REC_ID = "REF_AND_REC_ID"

    # ==========================================================================
    # tm2+ information
    # ==========================================================================

    #
    # Record identifiers
    #
    REC_ID = "REC_ID"
    REC_NO = "REC_NO"

    #
    # Item counts
    #
    NUM_AUTH = "NUM_AUTH"
    NUM_REF_GLOBAL = "NUM_REF_GLOBAL"
    NUM_REF_LOCAL = "NUM_REF_LOCAL"

    #
    # User fields
    #

    USER_0 = "USER_0"
    USER_1 = "USER_1"
    USER_2 = "USER_2"
    USER_3 = "USER_3"
    USER_4 = "USER_4"
    USER_5 = "USER_5"
    USER_6 = "USER_6"
    USER_7 = "USER_7"
    USER_8 = "USER_8"
    USER_9 = "USER_9"


class ItemsOrderBy(Enum):

    OCC = "OCC"
    CIT_COUNT_GLOBAL = "CIT_COUNT_GLOBAL"
    CIT_COUNT_LOCAL = "CIT_COUNT_LOCAL"


class RecordsOrderBy(Enum):

    CIT_COUNT_GLOBAL_BY_HIGHEST = "CIT_COUNT_GLOBAL_BY_HIGHEST"
    CIT_COUNT_GLOBAL_BY_LOWEST = "CIT_COUNT_GLOBAL_BY_LOWEST"
    CIT_COUNT_LOCAL_BY_HIGHEST = "CIT_COUNT_LOCAL_BY_HIGHEST"
    CIT_COUNT_LOCAL_BY_LOWEST = "CIT_COUNT_LOCAL_BY_LOWEST"
    FIRST_AUTH_A_TO_Z = "FIRST_AUTH_A_TO_Z"
    FIRST_AUTH_Z_TO_A = "FIRST_AUTH_Z_TO_A"
    PUBYEAR_NEWEST = "PUBYEAR_NEWEST"
    PUBYEAR_OLDEST = "PUBYEAR_OLDEST"
    SRC_TITLE_A_TO_Z = "SRC_TITLE_A_TO_Z"
    SRC_TITLE_Z_TO_A = "SRC_TITLE_Z_TO_A"


class ThesaurusField(Enum):

    CHANGED = "CHANGED"
    IS_KEYWORD = "IS_KEYWORD"
    OCC = "OCC"
    OLD = "OLD"
    PREFERRED = "PREFERRED"
    SIGNATURE = "SIGNATURE"
    VARIANT = "VARIANT"
