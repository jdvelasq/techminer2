from enum import Enum


class RecordsOrderBy(Enum):

    DATE_NEWEST = "date_newest"
    DATE_OLDEST = "date_oldest"
    GLOBAL_CITED_BY_HIGHEST = "global_cited_by_highest"
    GLOBAL_CITED_BY_LOWEST = "global_cited_by_lowest"
    LOCAL_CITED_BY_HIGHEST = "local_cited_by_highest"
    LOCAL_CITED_BY_LOWEST = "local_cited_by_lowest"
    FIRST_AUTHOR_A_TO_Z = "first_author_a_to_z"
    FIRST_AUTHOR_Z_TO_A = "first_author_z_to_a"
    SOURCE_TITLE_A_TO_Z = "source_title_a_to_z"
    SOURCE_TITLE_Z_TO_A = "source_title_z_to_a"


class Field(Enum):

    #
    # A
    #
    ABS_RAW = "abstract_raw"
    ABS_TOK = "abstract_tokenized"
    ABS_UPPER_NP = "abstract_uppercase_noun_phrase"
    ABS_UPPER_WORD = "abstract_uppercase_word"
    ACRONYM = "acronym"
    AFFIL_RAW = "affiliation"
    ALLKEY_NORM = "all_keywords_norm"
    ALLKEY_NP_NORM = "all_keywords_noun_phrase_norm"
    ALLKEY_NP_RAW = "all_keywords_noun_phrase_raw"
    ALLKEY_RAW = "all_keywords_raw"
    ALLKEY_WORD_NORM = "all_keywords_word_norm"
    ALLKEY_WORD_RAW = "all_keywords_word_raw"
    ALLNP_NORM = "all_noun_phrases_norm"
    ALLNP_RAW = "all_noun_phrases_raw"
    ALLTERMS_NORM = "all_terms_norm"
    ALLTERMS_RAW = "all_terms_raw"
    ALLWORD_NORM = "all_word_norm"
    ALLWORD_RAW = "all_word_raw"
    ARTNO = "art_no"
    AUTH_AFFIL = "author_with_affiliation"
    AUTH_DISAMB = "author_disambiguated"
    AUTH_FULL = "author_full_names"
    AUTH_ID_NORM = "author_id_norm"
    AUTH_ID_RAW = "author_id_raw"
    AUTH_NORM = "author_norm"
    AUTH_RAW = "author_raw"
    AUTHKEY_NORM = "author_keywords_norm"
    AUTHKEY_RAW = "author_keywords_raw"

    #
    # C
    #
    CASREGNUMBER = "cas_reg_number"
    CITCOUNT_GLOBAL = "citation_count_global"
    CITCOUNT_LOCAL = "citation_count_local"
    CODEN = "coden"
    CONFCODE = "conference_code"
    CONFDATE = "conference_date"
    CONFLOC = "conference_location"
    CONFNAME = "conference_name"
    CORRESP = "correspondence_address"
    COUNTRY = "country"

    #
    # D
    #
    DOCTYPE_NORM = "document_type_norm"
    DOCTYPE_RAW = "document_type_raw"
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
    FIRSTAUTH = "first_author"
    FIRSTAUTH_COUNTRY = "first_author_country"
    FIRSTAUTH_ORGANIZATION = "first_author_organization"
    FUND_DETAILS = "funding_details"
    FUND_SPONSORS = "funding_sponsors"
    FUND_TEXTS = "funding_texts"

    #
    # I
    #
    IDXKEY_NORM = "index_keywords_norm"
    IDXKEY_RAW = "index_keywords_raw"
    ISBN = "isbn"
    ISSN = "issn"
    ISSNP = "issnp"
    ISSUE = "issue"

    #
    # K
    #
    KEYTERMS_RAW = "keyterms_raw"
    KEYTERMS_NORM = "keyterms_norm"

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
    NP_ABS_NORM = "noun_phrases_abstract_norm"
    NP_ABS_RAW = "noun_phrases_abstract_raw"
    NP_SPACY = "noun_phrases_spacy"
    NP_TEXTBLOB = "noun_phrases_textblob"
    NP_TITLE_NORM = "noun_phrases_title_norm"
    NP_TITLE_RAW = "noun_phrases_title_raw"
    NUMAUTH = "number_of_authors"
    NUMREF_GLOBAL = "number_of_global_references"
    NUMREF_LOCAL = "number_of_local_references"

    #
    # O
    #
    OA = "open_access"
    ORGANIZATION = "organization"

    #
    # P
    #
    PAGEFIRST = "page_first"
    PAGELAST = "page_last"
    PAGES = "page_count"
    PUBLISHER = "publisher"
    PUBMED = "pubmed"
    PUBSTAGE = "publication_stage"
    PUBYEAR = "year"

    #
    # R
    #
    RECID = "record_id"
    RECNO = "record_no"
    REF_GLOBAL_RAW = "references_global_raw"
    REGION = "region"

    #
    # S
    #
    SEQNUM = "sequence_numbers"
    SOURCE = "source"
    SRCTITLE_ABBR_NORM = "source_title_abbr_norm"
    SRCTITLE_ABBR_RAW = "source_title_abbr_raw"
    SRCTITLE_NORM = "source_title_norm"
    SRCTITLE_RAW = "source_title_raw"
    SUBJAREA = "subject_areas"
    SUBREGION = "subregion"

    #
    # T
    #
    TITLE_RAW = "title_raw"
    TITLE_TOK = "title_tokenized"
    TITLE_UPPER_NP = "title_uppercase_noun_phrase"
    TITLE_UPPER_WORD = "title_uppercase_word"
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
