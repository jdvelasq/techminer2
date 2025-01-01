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


## >>> from techminer2.ingest.load import ingest_raw_data
## >>> ingest_raw_data( 
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/",
## ... ) # doctest: +ELLIPSIS +SKIP
-- 001 -- Compressing raw data files
-- 002 -- Creating working directories
-- 003 -- Creating stopwords.txt file
-- 004 -- Creating database file
...


"""

import time

from tqdm import tqdm  # type: ignore

from .internals.database import (
    database__compress_raw_files,
    database__create_project_structure,
    database__drop_empty_columns,
    database__load_raw_files,
    database__rename_columns,
)
from .internals.message import message
from .internals.preprocessing import (
    preprocessing__abbr_source_title,
    preprocessing__abbreviations,
    preprocessing__abstract,
    preprocessing__author_names,
    preprocessing__authors,
    preprocessing__authors_id,
    preprocessing__countries,
    preprocessing__descriptors,
    preprocessing__document_title,
    preprocessing__document_type,
    preprocessing__doi,
    preprocessing__eissn,
    preprocessing__global_citations,
    preprocessing__global_references,
    preprocessing__highlight_descriptors,
    preprocessing__isbn,
    preprocessing__issn,
    preprocessing__local_citations,
    preprocessing__local_references,
    preprocessing__num_authors,
    preprocessing__num_global_references,
    preprocessing__organizations,
    preprocessing__raw_abstract_nlp_phrases,
    preprocessing__raw_author_keywords,
    preprocessing__raw_descriptors,
    preprocessing__raw_index_keywords,
    preprocessing__raw_keywords,
    preprocessing__raw_nlp_phrases,
    preprocessing__raw_title_nlp_phrases,
    preprocessing__record_id,
    preprocessing__record_no,
    preprocessing__references,
    preprocessing__review_nlp_phrases,
    preprocessing__source_title,
)
from .internals.report_imported_records import report_imported_records


def ingest_raw_data(
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
    database__compress_raw_files(root_dir)
    database__create_project_structure(root_dir)
    database__load_raw_files(root_dir)
    database__rename_columns(root_dir)
    database__drop_empty_columns(root_dir)

    #
    #
    # PHASE 2: Process each column in isolation
    # =================================================================================
    #
    #
    preprocessing__abstract(root_dir)
    preprocessing__document_title(root_dir)
    #
    preprocessing__eissn(root_dir)
    preprocessing__issn(root_dir)
    preprocessing__isbn(root_dir)
    preprocessing__document_type(root_dir)
    #
    preprocessing__doi(root_dir)
    preprocessing__source_title(root_dir)
    preprocessing__abbr_source_title(root_dir)
    preprocessing__global_citations(root_dir)
    #
    preprocessing__authors_id(root_dir)
    preprocessing__authors(root_dir)
    preprocessing__author_names(root_dir)
    #
    preprocessing__num_authors(root_dir)
    preprocessing__num_global_references(root_dir)
    #
    preprocessing__references(root_dir)
    #
    preprocessing__record_id(root_dir)
    preprocessing__record_no(root_dir)

    #
    #
    # PHASE 2: Keywords & noun phrases & abstracts
    # =============================================================================================
    #
    #

    preprocessing__raw_index_keywords(root_dir)
    preprocessing__raw_author_keywords(root_dir)
    preprocessing__raw_keywords(root_dir)

    preprocessing__raw_abstract_nlp_phrases(root_dir)
    preprocessing__raw_title_nlp_phrases(root_dir)
    preprocessing__raw_nlp_phrases(root_dir)
    preprocessing__raw_descriptors(root_dir)
    preprocessing__highlight_descriptors(root_dir)
    preprocessing__review_nlp_phrases(root_dir)

    #
    #
    # PHASE 4: References
    # =============================================================================================
    #
    #

    preprocessing__global_references(root_dir)  # ok
    preprocessing__local_references(root_dir)  # ok
    preprocessing__local_citations(root_dir)  # ok

    #
    #
    # PHASE 5: Thesaurus files
    # =============================================================================================
    #
    #

    preprocessing__countries(root_dir)  # ok
    preprocessing__organizations(root_dir)  # ok
    preprocessing__descriptors(root_dir)  # ok
    preprocessing__abbreviations(root_dir)  # ok

    ## ------------------------------------------------------------------------------------------

    report_imported_records(root_dir)

    message("Process finished!!!")

    #
    # Elapsed time report
    end_time = time.time()
    elapsed_time = end_time - start_time
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print(f"Execution time: {int(hours):02}:{int(minutes):02}:{seconds:06.3f}")
