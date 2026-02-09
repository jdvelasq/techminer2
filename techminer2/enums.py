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


class CorpusField(Enum):

    #
    # A
    #
    ABS_RAW = "abs_raw"
    ABS_TOK = "abs_tok"
    ABS_TOK_WITH_UPPER_NP = "abs_tok_with_upper_np"
    ABS_TOK_WITH_UPPER_WORD = "abs_upper_word"
    ABS_NP_NORM = "np_abs_norm"
    ABS_NP_TOK = "np_abs_raw"
    ABS_WORD_TOK = "word_abs_raw"
    ACRONYM = "acronym"
    AFFIL_RAW = "affil_raw"
    ART_NO = "art_no"
    AUTH_AFFIL = "auth_affil"
    AUTH_DISAMB = "auth_disamb"
    AUTH_FULL = "auth_full"
    AUTH_ID_NORM = "auth_id_norm"
    AUTH_ID_RAW = "auth_id_raw"
    AUTH_KEY_NORM = "auth_key_norm"
    AUTH_KEY_RAW = "auth_key_raw"
    AUTH_KEY_TOK = "auth_key_tok"
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
    CONF_LOC = "conf_loc"
    CONF_NAME = "conf_name"
    CORRESP = "corresp"
    COUNTRY = "country"

    #
    # D
    #
    DOCTYPE_NORM = "doctype_norm"
    DOCTYPE_RAW = "doc_type_raw"
    DOCTITLE_RAW = "doctitle_raw"
    DOCTITLE_TOK = "doctitle_tok"
    DOCTITLE_TOK_WITH_UPPER_NP = "doctitle_tok_with_upper_np"
    DOCTITLE_TOK_WITH_UPPER_WORD = "doctitle_tok_with_upper_word"

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
    IDX_KEY_TOK = "idx_key_tok"
    ISBN = "isbn"
    ISSN = "issn"
    ISSNP = "issnp"
    ISSUE = "issue"

    #
    # K
    #
    KEY_NORM = "all_key_norm"
    KEY_AND_NP_NORM = "all_key_np_norm"
    KEY_AND_NP_TOK = "all_key_np_tok"
    KEY_NP_AND_WORD_TOK = "all_key_np_word_tok"
    KEY_NP_AND_WORD_NORM = "all_key_np_word_norm"
    KEY_TOK = "all_key_tok"
    KEY_AND_WORD_NORM = "all_key_word_norm"
    KEY_AND_WORD_TOK = "all_key_word_tok"

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
    NP_NORM = "all_np_norm"
    NP_SPACY = "np_spacy"
    NP_TEXTBLOB = "np_textblob"
    NP_TOK = "all_np_tok"
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
    PUBSTAGE = "pub_stage"
    PUBYEAR = "pubyear"

    #
    # R
    #
    REC_ID = "rec_id"
    REC_NO = "rec_no"
    REF_NORM = "ref_norm"
    REF_RAW = "ref_raw"
    REGION = "REGION"

    #
    # S
    #
    SEQNUMUMBER = "sequence_nums"
    SOURCE = "source"
    SRCTITLE_ABBR_NORM = "src_title_abbr_norm"
    SRCTITLE_ABBR_RAW = "src_title_abbr_raw"
    SRCTITLE_NORM = "src_title_norm"
    SRCTITLE_RAW = "src_title_raw"
    SUBJAREA = "subj_areas"
    SUBREGION = "subregion"

    #
    # T
    #
    TRADENAME = "TRADENAME"
    DOCTITLE_NP_NORM = "DOCTITLE_NP_NORM"
    DOCTITLE_NP_TOK = "DOCTITLE_NP_TOK"
    DOCTITLE_WORD_TOK = "DOCTITLE_WORD_TOK"
    #
    # V
    #
    VOL = "volume"

    #
    # W
    #
    WORD_NORM = "WORD_NORM"
    WORD_TOK = "WORD_TOK"


class ThesaurusField(Enum):

    KEY = "key_temp"
    KEY_LENGTH = "key_length"
    OCC = "occ"
    PREFERRED = "preferred_term"
    PREFERRED_TEMP = "preferred_temp"
    VARIANT = "variant"
