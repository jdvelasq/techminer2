# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Ingest Scopus
===============================================================================
# doctest: +SKIP

Example:
    >>> # Command line interface
    >>> # python3 -m techminer2.database.ingest.import_scopus_data

    >>> from techminer2.database.ingest import IngestScopus
    >>> IngestScopus(root_directory="example/").run() # doctest: +ELLIPSIS




"""
import pathlib
import sys
import time

from tqdm import tqdm

from ..._internals.mixins import ParamsMixin
from ._internals.datatests.check_empty_terms import internal__check_empty_terms
from ._internals.db import (
    internal__compress_raw_files,
    internal__create_project_structure,
    internal__drop_empty_columns,
    internal__load_raw_files,
    internal__remove_non_english_abstracts,
    internal__rename_columns,
)
from ._internals.db.report_imported_records import internal__report_imported_records
from ._internals.preprocessors import (  # type: ignore
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
    internal__preprocess_raw_abstract_nouns_and_phrases,
    internal__preprocess_raw_author_keywords,
    internal__preprocess_raw_descriptors,
    internal__preprocess_raw_document_title_nouns_and_phrases,
    internal__preprocess_raw_index_keywords,
    internal__preprocess_raw_keywords,
    internal__preprocess_raw_noun_and_phrases,
    internal__preprocess_raw_spacy_phrases,
    internal__preprocess_raw_textblob_phrases,
    internal__preprocess_record_id,
    internal__preprocess_record_no,
    internal__preprocess_references,
    internal__preprocess_source_title,
    internal__preprocess_subject_areas,
)


class IngestScopus(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):

        root_directory = self.params.root_directory
        #
        # Preparation
        # ---------------------------------------------------------------------------------
        #

        # Register tqdm pandas progress bar
        tqdm.pandas()

        # Elapsed time report
        sys.stderr.write("\n")
        sys.stderr.flush()
        start_time = time.time()

        #### delete file
        file_path = (
            pathlib.Path(self.params.root_directory)
            / "my_keywords/undetected_keywords.txt"
        )
        if file_path.exists():
            file_path.unlink()

        #
        # PHASE 1: Preparing database files and folders
        # ---------------------------------------------------------------------------------
        #
        internal__remove_non_english_abstracts(root_directory)
        internal__compress_raw_files(root_directory)
        internal__create_project_structure(root_directory)
        internal__load_raw_files(root_directory)
        internal__rename_columns(root_directory)
        internal__drop_empty_columns(root_directory)

        #
        #
        # PHASE 2: Process each column in isolation
        # ---------------------------------------------------------------------------------
        #
        #

        #
        internal__preprocess_eissn(root_directory)
        internal__preprocess_issn(root_directory)
        internal__preprocess_isbn(root_directory)
        internal__preprocess_document_type(root_directory)
        #
        internal__preprocess_doi(root_directory)
        internal__preprocess_source_title(root_directory)
        internal__preprocess_abbr_source_title(root_directory)
        internal__preprocess_global_citations(root_directory)
        #
        internal__preprocess_authors_id(root_directory)
        internal__preprocess_authors(root_directory)
        internal__preprocess_author_names(root_directory)
        #
        internal__preprocess_num_authors(root_directory)
        internal__preprocess_num_global_references(root_directory)
        #
        internal__preprocess_references(root_directory)
        #
        internal__preprocess_record_id(root_directory)
        internal__preprocess_record_no(root_directory)
        #
        internal__preprocess_subject_areas(root_directory)

        #
        #
        # PHASE 2: Keywords & noun phrases & abstracts
        # ---------------------------------------------------------------------------------
        #
        #

        # Author & index keywords
        internal__preprocess_raw_index_keywords(root_directory)
        internal__check_empty_terms("raw_index_keywords", root_directory=root_directory)
        internal__preprocess_index_keywords(root_directory)
        internal__check_empty_terms("index_keywords", root_directory=root_directory)

        internal__preprocess_raw_author_keywords(root_directory)
        internal__check_empty_terms(
            "raw_author_keywords", root_directory=root_directory
        )
        internal__preprocess_author_keywords(root_directory)
        internal__check_empty_terms("author_keywords", root_directory=root_directory)

        internal__preprocess_raw_keywords(root_directory)
        internal__check_empty_terms("raw_keywords", root_directory=root_directory)

        # Preprocess noun and phrases
        internal__preprocess_abstract(root_directory)
        internal__preprocess_document_title(root_directory)
        internal__preprocess_raw_textblob_phrases(root_directory)
        internal__preprocess_raw_spacy_phrases(root_directory)

        #
        internal__preprocess_raw_abstract_nouns_and_phrases(root_directory)
        internal__check_empty_terms(
            "raw_abstract_nouns_and_phrases", root_directory=root_directory
        )
        internal__preprocess_raw_document_title_nouns_and_phrases(root_directory)
        internal__check_empty_terms(
            "raw_document_title_nouns_and_phrases", root_directory=root_directory
        )
        internal__preprocess_raw_noun_and_phrases(root_directory)
        internal__check_empty_terms(
            "raw_noun_and_phrases", root_directory=root_directory
        )
        internal__preprocess_raw_descriptors(root_directory)
        internal__check_empty_terms("raw_descriptors", root_directory=root_directory)

        #
        #
        # PHASE 4: References
        # ---------------------------------------------------------------------------------
        #
        #

        internal__preprocess_global_references(root_directory)  # ok
        internal__preprocess_local_references(root_directory)  # ok
        internal__preprocess_local_citations(root_directory)  # ok

        #
        #
        # PHASE 5: Thesaurus files
        # ---------------------------------------------------------------------------------
        #
        #

        internal__preprocess_countries(root_directory)  # ok
        internal__preprocess_organizations(root_directory)  # ok
        internal__preprocess_descriptors(root_directory)  # ok
        internal__preprocess_abbreviations(root_directory)  # ok

        ## ------------------------------------------------------------------------------------------

        #
        # Elapsed time report
        end_time = time.time()
        elapsed_time = end_time - start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)

        internal__report_imported_records(root_directory)

        sys.stderr.write(
            f"INFO  Execution time: {int(hours):02}:{int(minutes):02}:{seconds:06.3f}\n\n"
        )

        sys.stderr.flush()


if __name__ == "__main__":

    IngestScopus(root_directory="./").run()
