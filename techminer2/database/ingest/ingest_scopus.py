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
    >>> from techminer2.database.ingest import IngestScopus
    >>> IngestScopus(root_directory="examples/fintech/").run() # doctest: +ELLIPSIS




"""
import pathlib
import sys
import time

from techminer2.database._internals.db import internal__check_hyphenated_form

from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.datatests.check_empty_terms import (
    internal__check_empty_terms,
)
from techminer2.database._internals.db import internal__compress_raw_files
from techminer2.database._internals.db import internal__create_project_structure
from techminer2.database._internals.db import internal__drop_empty_columns
from techminer2.database._internals.db import internal__load_raw_files
from techminer2.database._internals.db import internal__remove_non_english_abstracts
from techminer2.database._internals.db import internal__rename_columns
from techminer2.database._internals.db.report_imported_records import (
    internal__report_imported_records,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_abbr_source_title,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_acronyms,
)
from techminer2.database._internals.preprocessors import internal__preprocess_abstract
from techminer2.database._internals.preprocessors import (
    internal__preprocess_author_keywords,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_author_names,
)
from techminer2.database._internals.preprocessors import internal__preprocess_authors
from techminer2.database._internals.preprocessors import internal__preprocess_authors_id
from techminer2.database._internals.preprocessors import internal__preprocess_countries
from techminer2.database._internals.preprocessors import (
    internal__preprocess_descriptors,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_document_title,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_document_type,
)
from techminer2.database._internals.preprocessors import internal__preprocess_doi
from techminer2.database._internals.preprocessors import internal__preprocess_eissn
from techminer2.database._internals.preprocessors import (
    internal__preprocess_global_citations,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_global_references,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_index_keywords,
)
from techminer2.database._internals.preprocessors import internal__preprocess_isbn
from techminer2.database._internals.preprocessors import internal__preprocess_issn
from techminer2.database._internals.preprocessors import (
    internal__preprocess_local_citations,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_local_references,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_num_authors,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_num_global_references,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_organizations,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_abstract_nouns_and_phrases,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_author_keywords,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_descriptors,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_document_title_nouns_and_phrases,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_index_keywords,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_keywords,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_noun_and_phrases,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_spacy_phrases,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_raw_textblob_phrases,
)
from techminer2.database._internals.preprocessors import internal__preprocess_record_id
from techminer2.database._internals.preprocessors import internal__preprocess_record_no
from techminer2.database._internals.preprocessors import internal__preprocess_references
from techminer2.database._internals.preprocessors import (
    internal__preprocess_source_title,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_subject_areas,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_tokenized_abstract,
)
from techminer2.database._internals.preprocessors import (
    internal__preprocess_tokenized_document_title,
)
from tqdm import tqdm


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
        for file in [
            "my_keywords/undetected_keywords.txt",
            "my_keywords/hyphenated_is_incorrect.txt",
            "my_keywords/hyphenated_is_correct.txt",
        ]:

            file_path = pathlib.Path(self.params.root_directory) / file
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
        internal__check_hyphenated_form(root_directory)

        #
        #
        # PHASE 2: Keywords & noun phrases & abstracts
        # ---------------------------------------------------------------------------------
        #
        #
        internal__preprocess_tokenized_document_title(root_directory)
        internal__preprocess_tokenized_abstract(root_directory)
        #
        internal__preprocess_raw_textblob_phrases(root_directory)
        internal__preprocess_raw_spacy_phrases(root_directory)
        internal__preprocess_abstract(root_directory)
        internal__preprocess_document_title(root_directory)

        #
        internal__preprocess_raw_abstract_nouns_and_phrases(root_directory)
        internal__check_empty_terms(
            "raw_abstract_nouns_and_phrases", root_directory=root_directory
        )
        #
        internal__preprocess_raw_document_title_nouns_and_phrases(root_directory)
        internal__check_empty_terms(
            "raw_document_title_nouns_and_phrases", root_directory=root_directory
        )
        internal__preprocess_raw_noun_and_phrases(root_directory)
        internal__check_empty_terms(
            "raw_noun_and_phrases", root_directory=root_directory
        )

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

        internal__preprocess_raw_descriptors(root_directory)
        internal__check_empty_terms("raw_descriptors", root_directory=root_directory)

        #
        #
        # PHASE 3: Process each column in isolation
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
        internal__preprocess_acronyms(root_directory)  # ok

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


#
