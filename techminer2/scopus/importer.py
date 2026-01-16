"""
Importer
===============================================================================
# doctest: +SKIP

Smoke test:
    >>> from techminer2.scopus import Importer
    >>> (
    ...     Importer()
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )


"""

import sys
import time

from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.datatests.check_empty_terms import (
    internal__check_empty_terms,
)
from techminer2.scopus._internals.preparation import (
    compress_raw_files,
    create_database_files,
    drop_empty_columns,
    remove_non_english_abstracts,
    rename_columns,
)
from techminer2.scopus._internals.preprocessors import (
    _preprocess_abbr_source_title,
    _preprocess_abstract,
    _preprocess_acronyms,
    _preprocess_author_keywords,
    _preprocess_author_names,
    _preprocess_authors,
    _preprocess_authors_id,
    _preprocess_countries,
    _preprocess_descriptors,
    _preprocess_document_title,
    _preprocess_document_type,
    _preprocess_doi,
    _preprocess_eissn,
    _preprocess_global_citations,
    _preprocess_global_references,
    _preprocess_index_keywords,
    _preprocess_isbn,
    _preprocess_issn,
    _preprocess_local_citations,
    _preprocess_local_references,
    _preprocess_num_authors,
    _preprocess_num_global_references,
    _preprocess_organizations,
    _preprocess_raw_abstract_nouns_and_phrases,
    _preprocess_raw_author_keywords,
    _preprocess_raw_descriptors,
    _preprocess_raw_document_title_nouns_and_phrases,
    _preprocess_raw_index_keywords,
    _preprocess_raw_keywords,
    _preprocess_raw_noun_and_phrases,
    _preprocess_raw_spacy_phrases,
    _preprocess_raw_textblob_phrases,
    _preprocess_record_id,
    _preprocess_record_no,
    _preprocess_references,
    _preprocess_source_title,
    _preprocess_subject_areas,
    _preprocess_tokenized_abstract,
    _preprocess_tokenized_document_title,
)
from techminer2.scopus._internals.report_imported_records import (
    internal__report_imported_records,
)
from techminer2.scopus._internals.scaffolding import create_project_structure
from techminer2.scopus._internals.validation import internal__check_hyphenated_form


class Importer(
    ParamsMixin,
):
    """:meta private:"""

    # ------------------------------------------------------------------------
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._phase: int = 0

    # ------------------------------------------------------------------------
    def _print_header(self) -> None:
        sys.stderr.write("\n" + "=" * 70 + "\n")
        sys.stderr.write("Importing Scopus Data\n")
        sys.stderr.write("=" * 70 + "\n")
        sys.stderr.flush()

    # ------------------------------------------------------------------------
    def _print_phase(self, description: str) -> None:
        sys.stderr.write(f"\n[{self._phase}] {description}\n")
        sys.stderr.flush()

    # ------------------------------------------------------------------------
    def _print_step(self, message: str):
        sys.stderr.write(f"  → {message}...\n")
        sys.stderr.flush()

    # ------------------------------------------------------------------------
    def _print_detail(self, message: str) -> None:
        """Print step result or additional detail."""
        sys.stderr.write(f"    {message}\n")
        sys.stderr.flush()

    # ------------------------------------------------------------------------
    def _run_phase_1_preparation(self) -> None:

        self._phase += 1
        self._print_phase("Preparing database files and folders")

        self._print_step("Creating project structure")
        create_project_structure(self.params.root_directory)

        self._print_step("Removing non-English abstracts")
        n_removed = remove_non_english_abstracts(self.params.root_directory)
        if n_removed > 0:
            self._print_detail(
                f"Removed {n_removed} records with non-English abstracts"
            )

        self._print_step("Compressing raw files")
        n_compressed = compress_raw_files(self.params.root_directory)
        if n_compressed > 0:
            self._print_detail(f"Compressed {n_compressed} raw files")

        self._print_step("Creating database files")
        n_created = create_database_files(self.params.root_directory)
        if n_created:
            for key, value in n_created.items():
                self._print_detail(f"Created {value} records in {key} database file")

        self._print_step("Renaming columns")
        processed = rename_columns(self.params.root_directory)
        if processed > 0:
            self._print_detail(f"Renamed columns in {processed} files")

        self._print_step("Renaming columns")
        dropped = drop_empty_columns(self.params.root_directory)

        for file_type, cols in dropped.items():
            if cols:
                self._print_detail(f"{file_type}: dropped {len(cols)} empty columns")
                for col in cols[:5]:  # Show first 5
                    self._print_detail(f"  • {col}")
                if len(cols) > 5:
                    self._print_detail(f"  • ... and {len(cols)-5} more")

    # ------------------------------------------------------------------------
    def run(self) -> None:

        # root_directory = self.params.root_directory
        #
        # Preparation
        # ---------------------------------------------------------------------------------
        #

        # Register tqdm pandas progress bar
        # tqdm.pandas()

        # Elapsed time report
        # sys.stderr.write("\n")
        # sys.stderr.flush()
        # start_time = time.time()

        #
        # PHASE 1: Preparing database files and folders
        # ---------------------------------------------------------------------------------
        #
        self._print_header()
        self._run_phase_1_preparation()

        #

        #
        # internal__check_hyphenated_form(root_directory)

        #
        #
        # PHASE 2: Keywords & noun phrases & abstracts
        # ---------------------------------------------------------------------------------
        #
        #
        # _preprocess_tokenized_document_title(root_directory)
        # _preprocess_tokenized_abstract(root_directory)
        #
        # _preprocess_raw_textblob_phrases(root_directory)
        # _preprocess_raw_spacy_phrases(root_directory)
        # _preprocess_abstract(root_directory)
        # _preprocess_document_title(root_directory)

        #
        # _preprocess_raw_abstract_nouns_and_phrases(root_directory)
        # internal__check_empty_terms(
        #     "raw_abstract_nouns_and_phrases", root_directory=root_directory
        # )
        #
        # _preprocess_raw_document_title_nouns_and_phrases(root_directory)
        # internal__check_empty_terms(
        #     "raw_document_title_nouns_and_phrases", root_directory=root_directory
        # )
        # _preprocess_raw_noun_and_phrases(root_directory)
        # internal__check_empty_terms(
        #     "raw_noun_and_phrases", root_directory=root_directory
        # )

        # Author & index keywords
        # _preprocess_raw_index_keywords(root_directory)
        # _preprocess_index_keywords(root_directory)
        # internal__check_empty_terms("index_keywords", root_directory=root_directory)
        # internal__check_empty_terms("raw_index_keywords", root_directory=root_directory)

        # _preprocess_raw_author_keywords(root_directory)
        # internal__check_empty_terms(
        #     "raw_author_keywords", root_directory=root_directory
        # )
        # _preprocess_author_keywords(root_directory)
        # internal__check_empty_terms("author_keywords", root_directory=root_directory)

        # _preprocess_raw_keywords(root_directory)
        # internal__check_empty_terms("raw_keywords", root_directory=root_directory)

        # _preprocess_raw_descriptors(root_directory)
        # internal__check_empty_terms("raw_descriptors", root_directory=root_directory)

        #
        #
        # PHASE 3: Process each column in isolation
        # ---------------------------------------------------------------------------------
        #
        #

        #
        # _preprocess_eissn(root_directory)
        # _preprocess_issn(root_directory)
        # _preprocess_isbn(root_directory)
        # _preprocess_document_type(root_directory)
        #
        # _preprocess_source_title(root_directory)
        # _preprocess_abbr_source_title(root_directory)
        # _preprocess_doi(root_directory)
        # _preprocess_global_citations(root_directory)
        #
        # _preprocess_authors_id(root_directory)
        # _preprocess_authors(root_directory)
        # _preprocess_author_names(root_directory)
        #
        # _preprocess_num_authors(root_directory)
        # _preprocess_num_global_references(root_directory)
        #
        # _preprocess_references(root_directory)
        #

        # _preprocess_record_id(root_directory)
        # _preprocess_record_no(root_directory)
        #
        # _preprocess_subject_areas(root_directory)

        #
        #
        # PHASE 4: References
        # ---------------------------------------------------------------------------------
        #
        #

        # _preprocess_global_references(root_directory)  # ok
        # _preprocess_local_references(root_directory)  # ok
        # _preprocess_local_citations(root_directory)  # ok

        #
        #
        # PHASE 5: Thesaurus files
        # ---------------------------------------------------------------------------------
        #
        #

        # _preprocess_countries(root_directory)  # ok
        # _preprocess_organizations(root_directory)  # ok
        # _preprocess_descriptors(root_directory)  # ok
        # _preprocess_acronyms(root_directory)  # ok

        ## ------------------------------------------------------------------------------------------

        #
        # Elapsed time report
        # end_time = time.time()
        # elapsed_time = end_time - start_time
        # hours, rem = divmod(elapsed_time, 3600)
        # minutes, seconds = divmod(rem, 60)

        # internal__report_imported_records(root_directory)

        # sys.stderr.write(
        #     f"INFO: Execution time : {int(hours):02}:{int(minutes):02}:{seconds:04.1f}\n\n"
        # )

        # sys.stderr.flush()


#
