# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Ingest Raw Data
===============================================================================
# doctest: +SKIP 


>>> from techminer2.database.ingest import ingest__load_scopus_data
>>> ingest__load_scopus_data( 
...     #
...     # DATABASE PARAMS:
...     root_dir="example/",
... ) # doctest: +ELLIPSIS
-- 001 -- Compressing raw data files
-- 002 -- Creating working directories
-- 003 -- Creating stopwords.txt file
-- 004 -- Creating database file
...


"""

import time

from tqdm import tqdm

from ..internals.database import (
    internal__compress_raw_files,
    internal__create_project_structure,
    internal__drop_empty_columns,
    internal__load_raw_files,
    internal__rename_columns,
)
from ..internals.database.internal__report_imported_records import (
    internal__report_imported_records,
)
from ..internals.message import message
from ..internals.preprocessing import (
    internal__preprocess_abbr_source_title,
    internal__preprocess_abbreviations,
    internal__preprocess_abstract,
    internal__preprocess_author_keywords,
    internal__preprocess_author_names,
    internal__preprocess_authors,
    internal__preprocess_authors_id,
    internal__preprocess_countries,
    internal__preprocess_descriptors,
    internal__preprocess_document_title,
    internal__preprocess_document_type,
    internal__preprocess_doi,
    internal__preprocess_eissn,
    internal__preprocess_global_citations,
    internal__preprocess_global_references,
    internal__preprocess_index_keywords,
    internal__preprocess_isbn,
    internal__preprocess_issn,
    internal__preprocess_local_citations,
    internal__preprocess_local_references,
    internal__preprocess_num_authors,
    internal__preprocess_num_global_references,
    internal__preprocess_organizations,
    internal__preprocess_raw_abstract_nlp_phrases,
    internal__preprocess_raw_author_keywords,
    internal__preprocess_raw_descriptors,
    internal__preprocess_raw_document_title_nlp_phrases,
    internal__preprocess_raw_index_keywords,
    internal__preprocess_raw_keywords,
    internal__preprocess_raw_nlp_phrases,
    internal__preprocess_record_id,
    internal__preprocess_record_no,
    internal__preprocess_references,
    internal__preprocess_source_title,
)


def ingest__load_scopus_data(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    #
    # Preparation
    # =================================================================================
    #

    # Register tqdm pandas progress bar
    tqdm.pandas()

    # Elapsed time report
    start_time = time.time()

    #
    # PHASE 1: Preparing database files and folders
    # =================================================================================
    #
    internal__compress_raw_files(root_dir)
    internal__create_project_structure(root_dir)
    internal__load_raw_files(root_dir)
    internal__rename_columns(root_dir)
    internal__drop_empty_columns(root_dir)

    #
    #
    # PHASE 2: Process each column in isolation
    # =================================================================================
    #
    #
    internal__preprocess_abstract(root_dir)
    internal__preprocess_document_title(root_dir)
    #
    internal__preprocess_eissn(root_dir)
    internal__preprocess_issn(root_dir)
    internal__preprocess_isbn(root_dir)
    internal__preprocess_document_type(root_dir)
    #
    internal__preprocess_doi(root_dir)
    internal__preprocess_source_title(root_dir)
    internal__preprocess_abbr_source_title(root_dir)
    internal__preprocess_global_citations(root_dir)
    #
    internal__preprocess_authors_id(root_dir)
    internal__preprocess_authors(root_dir)
    internal__preprocess_author_names(root_dir)
    #
    internal__preprocess_num_authors(root_dir)
    internal__preprocess_num_global_references(root_dir)
    #
    internal__preprocess_references(root_dir)
    #
    internal__preprocess_record_id(root_dir)
    internal__preprocess_record_no(root_dir)

    #
    #
    # PHASE 2: Keywords & noun phrases & abstracts
    # =============================================================================================
    #
    #

    internal__preprocess_raw_index_keywords(root_dir)
    internal__preprocess_index_keywords(root_dir)
    internal__preprocess_raw_author_keywords(root_dir)
    internal__preprocess_author_keywords(root_dir)
    internal__preprocess_raw_keywords(root_dir)

    internal__preprocess_raw_abstract_nlp_phrases(root_dir)
    internal__preprocess_raw_document_title_nlp_phrases(root_dir)

    internal__preprocess_raw_nlp_phrases(root_dir)
    internal__preprocess_raw_descriptors(root_dir)

    #
    #
    # PHASE 4: References
    # =============================================================================================
    #
    #

    internal__preprocess_global_references(root_dir)  # ok
    internal__preprocess_local_references(root_dir)  # ok
    internal__preprocess_local_citations(root_dir)  # ok

    #
    #
    # PHASE 5: Thesaurus files
    # =============================================================================================
    #
    #

    internal__preprocess_countries(root_dir)  # ok
    internal__preprocess_organizations(root_dir)  # ok
    internal__preprocess_descriptors(root_dir)  # ok
    internal__preprocess_abbreviations(root_dir)  # ok

    ## ------------------------------------------------------------------------------------------

    internal__report_imported_records(root_dir)

    message("Process finished!!!")

    #
    # Elapsed time report
    end_time = time.time()
    elapsed_time = end_time - start_time
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print(f"Execution time: {int(hours):02}:{int(minutes):02}:{seconds:06.3f}")
