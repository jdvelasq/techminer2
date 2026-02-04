from enum import Enum


class RecordsOrderBy(Enum):

    CIT_COUNT_GLOBAL_BY_HIGHEST = "cit_count_global_by_highest"
    CIT_COUNT_GLOBAL_BY_LOWEST = "cit_count_global_by_lowest"
    CIT_COUNT_LOCAL_BY_HIGHEST = "cit_count_local_by_highest"
    CIT_COUNT_LOCAL_BY_LOWEST = "cit_count_local_by_lowest"
    FIRST_AUTH_A_TO_Z = "first_auth_a_to_z"
    FIRST_AUTH_Z_TO_A = "first_auth_z_to_a"
    PUBYEAR_NEWEST = "pubyear_newest"
    PUBYEAR_OLDEST = "pubyear_oldest"
    SRC_TITLE_A_TO_Z = "src_title_a_to_z"
    SRE_TITLE_Z_TO_A = "src_title_z_to_a"


class Field(Enum):

    #
    # A
    #
    ABS_RAW = "abs_raw"
    ABS_TOK = "abs_tok"
    ABS_UPPER_NP = "abs_upper_np"
    ABS_UPPER_WORD = "abs_upper_word"
    ACRONYM = "acronym"
    AFFIL_RAW = "affil_raw"
    ALL_KEY_NORM = "all_key_norm"
    ALL_KEY_NP_NORM = "all_key_np_norm"
    ALL_KEY_NP_RAW = "all_key_np_raw"
    ALL_KEY_NP_WORD_RAW = "all_key_np_word_raw"
    ALL_KEY_NP_WORD_NORM = "all_key_np_word_norm"
    ALL_KEY_RAW = "all_key_raw"
    ALL_KEY_WORD_NORM = "all_key_word_norm"
    ALL_KEY_WORD_RAW = "all_key_word_raw"
    ALL_NP_NORM = "all_np_norm"
    ALL_NP_RAW = "all_np_raw"
    ALL_WORD_NORM = "all_word_norm"
    ALL_WORD_RAW = "all_word_raw"
    ART_NO = "art_no"
    AUTH_AFFIL = "auth_affil"
    AUTH_DISAMB = "auth_disamb"
    AUTH_FULL = "auth_full"
    AUTH_ID_NORM = "auth_id_norm"
    AUTH_ID_RAW = "auth_id_raw"
    AUTH_KEY_NORM = "auth_key_norm"
    AUTH_KEY_RAW = "auth_key_raw"
    AUTH_NORM = "auth_norm"
    AUTH_RAW = "auth_raw"

    #
    # C
    #
    CAS_REG_NUMBER = "cas_reg_num"
    CIT_COUNT_GLOBAL = "cit_count_global"
    CIT_COUNT_LOCAL = "cit_count_local"
    CODEN = "coden"
    CONF_CODE = "conf_code"
    CONF_DATE = "conf_date"
    CONF_LOC = "conf_location"
    CONF_NAME = "conf_name"
    CORRESP = "corresp"
    COUNTRY = "country"

    #
    # D
    #
    DOC_TYPE_NORM = "doc_type_norm"
    DOC_TYPE_RAW = "doc_type_raw"
    DOI = "doi"

    #
    # E
    #
    EDITOR = "editor"
    EID = "document_identifier"
    EISSN = "eissn"

    #
    # F
    #
    FIRST_AUTH = "first_auth"
    FIRST_AUTH_COUNTRY = "first_auth_country"
    FIRST_AUTH_ORGANIZATION = "first_auth_organization"
    FUND_DETAILS = "fund_details"
    FUND_SPONSORS = "fund_sponsors"
    FUND_TEXTS = "fund_texts"

    #
    # I
    #
    IDX_KEY_NORM = "idx_key_norm"
    IDX_KEY_RAW = "idx_key_raw"
    ISBN = "isbn"
    ISSN = "issn"
    ISSNP = "issnp"
    ISSUE = "issue"

    #
    # K
    #

    #
    # L
    #
    LANGUAGE = "language"
    LINK = "link"

    #
    # M
    #
    MANUFACTURER = "manufacturer"

    #
    # N
    #
    NP_ABS_NORM = "np_abs_norm"
    NP_ABS_RAW = "np_abs_raw"
    NP_SPACY = "np_spacy"
    NP_TEXTBLOB = "np_textblob"
    NP_TITLE_NORM = "np_title_norm"
    NP_TITLE_RAW = "np_title_raw"
    NUM_AUTH = "num_auths"
    NUM_REF_GLOBAL = "num_ref_global"
    NUM_REF_LOCAL = "num_ref_local"

    #
    # O
    #
    OA = "open_access"
    ORGANIZATION = "organization"

    #
    # P
    #
    PAGE_FIRST = "page_first"
    PAGE_LAST = "page_last"
    PAGE_COUNT = "page_count"
    PUBLISHER = "publisher"
    PUBMED = "pubmed"
    PUB_STAGE = "pub_stage"
    PUBYEAR = "pubyear"

    #
    # R
    #
    REC_ID = "rec_id"
    REC_NO = "rec_no"
    REF_NORM = "ref_norm"
    REF_RAW = "ref_raw"
    REGION = "region"

    #
    # S
    #
    SEQ_NUM = "sequence_nums"
    SOURCE = "source"
    SRC_TITLE_ABBR_NORM = "src_title_abbr_norm"
    SRC_TITLE_ABBR_RAW = "src_title_abbr_raw"
    SRC_TITLE_NORM = "src_title_norm"
    SRC_TITLE_RAW = "src_title_raw"
    SUBJ_AREA = "subj_areas"
    SUBREGION = "subregion"

    #
    # T
    #
    TITLE_RAW = "title_raw"
    TITLE_TOK = "title_tok"
    TITLE_UPPER_NP = "title_upper_np"
    TITLE_UPPER_WORD = "title_upper_word"
    TRADENAME = "tradename"

    #
    # V
    #
    VOL = "volume"

    #
    # W
    #
    WORD_ABS_RAW = "word_abs_raw"
    WORD_TITLE_RAW = "word_title_raw"
