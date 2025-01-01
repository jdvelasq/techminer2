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


## >>> from techminer2.ingest import ingest_raw_data
## >>> ingest_raw_data( 
## ...     #
## ...     # DATABASE PARAMS:
## ...     # root_dir="example/",
## ...     root_dir="/Users/jdvelasq/Library/Mobile Documents/com~apple~CloudDocs/__tm2__/06_blended_learning/", 
## ... ) # doctest: +ELLIPSIS
-- 001 -- Compressing raw data files
-- 002 -- Creating working directories
-- 003 -- Creating stopwords.txt file
-- 004 -- Creating database files
...


"""
import os
import time

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

# -------------------------------------------------------------------------------------
# Field basic operations
# -------------------------------------------------------------------------------------
from ..fields.further_processing.count_terms_per_record import _count_terms_per_record
from ..fields.further_processing.extract_noun_phrases import _extract_noun_phrases
from ..fields.further_processing.replace_keywords import replace_keywords
from ..fields.further_processing.replace_noun_phrases import _replace_noun_phrases
from ..fields.merge_fields import _merge_fields
from ..helpers.helper_abstracts_and_titles_to_lower_case import helper_abstracts_and_titles_to_lower_case

#
# Thesaurus
from ..thesaurus.countries.apply_thesaurus import apply_thesaurus as apply_countries_thesaurus
from ..thesaurus.descriptors.apply_thesaurus import apply_thesaurus as apply_descriptors_thesaurus
from ..thesaurus.organizations.apply_thesaurus import apply_thesaurus as apply_organizations_thesaurus

# -------------------------------------------------------------------------------------
# Auxuliary functions
# -------------------------------------------------------------------------------------
from ._compress_csv_files_in_raw_data_subdirectories import compress_csv_files_in_raw_data_subdirectories
from ._create_abbreviations_thesaurus import _create_abbreviations_thesaurus
from ._create_art_no_column import create_art_no_column
from ._create_article_column import create_article_column
from ._create_database_files import create_database_files
from ._create_local_citations_column_in_cited_by_database import create_local_citations_column_in_cited_by_database
from ._create_local_citations_column_in_documents_database import create_local_citations_column_in_documents_database
from ._create_local_citations_column_in_references_database import create_local_citations_column_in_references_database
from ._create_working_subdirectories_and_files import create_working_subdirectories_and_files
from ._disambiguate_author_names import disambiguate_author_names
from ._drop_empty_columns_in_databases import drop_empty_columns_in_databases

#
#
from ._homogenize_global_references import homogenize_global_references
from ._homogenize_local_references import homogenize_local_references
from ._list_cleanup_countries import list_cleanup_countries
from ._list_cleanup_organizations import list_cleanup_organizations
from ._message import message
from ._rename_columns_in_database_files import rename_columns_in_database_files
from ._replace_descriptors import _replace_descriptors
from ._replace_journal_name_in_references import replace_journal_name_in_references
from ._report_imported_records_per_file import report_imported_records_per_file

# -------------------------------------------------------------------------------------
# Importers
# -------------------------------------------------------------------------------------
from .field_importers.abbr_source_title_importer import run_abbr_source_title_importer
from .field_importers.abstract_importer import run_abstract_importer
from .field_importers.authors_and_index_keywords_importer import run_authors_and_index_keywords_importer
from .field_importers.authors_id_importer import run_authors_id_importer
from .field_importers.authors_importer import run_authors_importer
from .field_importers.document_title_importer import run_document_title_importer
from .field_importers.document_type_importer import run_document_type_importer
from .field_importers.doi_importer import run_doi_importer
from .field_importers.global_citations_importer import run_global_citations_importer
from .field_importers.issb_isbn_eissn_importer import run_issb_isbn_eissn_importer
from .field_importers.source_title_importer import run_source_title_importer
from .load.deprecated.repair_bad_separators_in_keywords import repair_bad_separators_in_keywords

# from ._adds_countries_and_regions_to_stopwords import _adds_countries_and_regions_to_stopwords


def ingest_raw_data(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # This file is very long. Process original csv Scopus files to a format that is
    # easier to work with. Due to great number of transformations, I decide to put
    # each function and the their inmediate call, in order to clarify the process.

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
    compress_csv_files_in_raw_data_subdirectories(root_dir)
    create_working_subdirectories_and_files(root_dir)
    create_database_files(root_dir)
    rename_columns_in_database_files(root_dir)
    repair_bad_separators_in_keywords(root_dir)
    drop_empty_columns_in_databases(root_dir)

    #
    #
    # PHASE 2: Process each column in isolation
    # =================================================================================
    #
    #
    run_authors_importer(root_dir)
    run_document_type_importer(root_dir)
    run_authors_id_importer(root_dir)
    run_issb_isbn_eissn_importer(root_dir)
    run_global_citations_importer(root_dir)
    run_doi_importer(root_dir)
    run_source_title_importer(root_dir)
    run_abbr_source_title_importer(root_dir)
    run_abstract_importer(root_dir)
    run_document_title_importer(root_dir)

    _count_terms_per_record(
        source="authors",
        dest="num_authors",
        root_dir=root_dir,
    )

    _count_terms_per_record(
        source="global_references",
        dest="num_global_references",
        root_dir=root_dir,
    )

    disambiguate_author_names(root_dir)
    replace_journal_name_in_references(root_dir)
    create_article_column(root_dir)
    create_art_no_column(root_dir)

    #
    #
    # PHASE 2: Keywords & noun phrases & abstracts
    # =============================================================================================
    #
    #

    # In the context of topic modeling for research abstracts, it is generally
    # more common and beneficial to use "noun phrases" extracted using text
    # mining techniques rather than relying solely on provided "keywords" for
    # the given document.
    #
    # Research abstracts often contain technical and domain-specific
    # language, making it challenging to accurately capture the main topics
    # and themes using only manually assigned or provided keywords. On the
    # other hand, using text mining techniques to extract noun phrases can
    # help uncover more nuanced and contextually relevant phrases that better
    # represent the content of the abstracts.
    #
    # Text mining techniques, such as part-of-speech tagging, noun phrase
    # chunking, or natural language processing algorithms, can identify
    # meaningful noun phrases that may not be explicitly listed as keywords.
    # These extracted noun phrases can provide a more comprehensive
    # representation of the topics present in the research abstracts,
    # allowing for more accurate and informative topic modeling.
    #
    # Therefore, leveraging text mining techniques to extract noun phrases is
    # often preferred over relying solely on provided keywords when
    # conducting topic modeling on research abstracts.

    #
    # Prepare author/index keywords:
    # To upper() and replace spaces with underscores
    # Merge author/index keywords into a single column
    #
    run_authors_and_index_keywords_importer(root_dir)

    _merge_fields(
        sources=["raw_author_keywords", "raw_index_keywords"],
        dest="raw_keywords",
        root_dir=root_dir,
    )

    #
    # Prepare title:
    # To lower() & remove brackets & remove multiple spaces & strip
    #

    #
    # Technological Emergence Indicators using Emergence Score.
    # Garner et al. 2017.
    # ------------------------------------------------------------------------
    #
    # Suitable terms for determining emergence are presented both in title and
    # the abstract. This allows to augment the list of terms given by the
    # authors/index keywords
    #

    #
    # Step 1: Create a candidate list of abstract noun phrases
    #

    #
    # In textblob, text in upper case is recognized as noun:
    # >>> TextBlob("Face-to-face".upper())
    # [('FACE-TO-FACE', 'NN')]
    replace_keywords(
        root_dir=root_dir,
    )

    _extract_noun_phrases(
        source="abstract",
        dest="raw_abstract_nlp_phrases",
        root_dir=root_dir,
    )

    helper_abstracts_and_titles_to_lower_case(root_dir=root_dir)

    #
    # Step 2: Create a candidate list of title noun phrases
    #
    _extract_noun_phrases(
        source="document_title",
        dest="raw_title_nlp_phrases",
        root_dir=root_dir,
    )

    # _replace_noun_phrases(
    #     column_to_process="document_title",
    #     noun_phrases_column="raw_title_nlp_phrases",
    #     root_dir=root_dir,
    # )

    #
    # Step 3: Merge fields
    #
    _merge_fields(
        sources=["raw_title_nlp_phrases", "raw_abstract_nlp_phrases"],
        dest="raw_nlp_phrases",
        root_dir=root_dir,
    )

    _merge_fields(
        sources=["raw_nlp_phrases", "raw_keywords"],
        dest="raw_descriptors",
        root_dir=root_dir,
    )

    #
    # Highlight author and index keywords
    #
    _replace_descriptors(root_dir)
    # replace_keywords(
    #     root_dir=root_dir,
    # )

    #
    #
    # PHASE 4: References
    # =============================================================================================
    #
    #

    homogenize_local_references(root_dir)
    homogenize_global_references(root_dir)

    #
    create_local_citations_column_in_documents_database(root_dir)
    create_local_citations_column_in_references_database(root_dir)
    create_local_citations_column_in_cited_by_database(root_dir)

    #
    #
    # PHASE 5: Thesaurus files
    # =============================================================================================
    #
    #

    list_cleanup_countries(root_dir)
    apply_countries_thesaurus(root_dir)

    list_cleanup_organizations(root_dir)
    apply_organizations_thesaurus(root_dir)

    #
    # Generate a list of raw entries for the descriptors thesaurus.
    #
    file = os.path.join(root_dir, "databases/_main.csv.zip")
    data_frame = pd.read_csv(file, encoding="utf-8", compression="zip")
    words = data_frame["raw_descriptors"].dropna().str.split("; ", expand=False).explode().str.strip().drop_duplicates().sort_values().to_list()

    #
    # Creates a thesaurus with an entry for each differnt descriptor
    #
    thesaurus_file = os.path.join(root_dir, "thesauri/descriptors.the.txt")
    with open(thesaurus_file, "w", encoding="utf-8") as f:
        for word in words:
            f.write(word + "\n")
            f.write("    " + word + "\n")

    apply_descriptors_thesaurus(root_dir)

    _create_abbreviations_thesaurus(root_dir)

    ## ------------------------------------------------------------------------------------------

    # Removed: _adds_countries_and_regions_to_stopwords(root_dir)

    report_imported_records_per_file(root_dir)
    # Removed: create_imported_records_report(root_dir)

    message("Process finished!!!")

    #
    # Elapsed time report
    end_time = time.time()
    print("Execution time:", round(end_time - start_time, 1), "seconds")
