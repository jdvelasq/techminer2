# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Last Word
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import InitializeThesaurus, SortByLastWords

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()


    >>> # Creates, configures, an run the sorter
    >>> sorter = (
    ...     SortByLastWords(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by common last words...
      File : example/data/thesaurus/demo.the.txt
      12 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/demo.the.txt
    <BLANKLINE>
        AGRICULTURE_PLAYS
          AGRICULTURE_PLAYS
        CONTINUANCE_INTENTION_DIFFERS
          CONTINUANCE_INTENTION_DIFFERS
        ENTREPRENEURIAL_ENDEAVOURS
          ENTREPRENEURIAL_ENDEAVOURS
        FOUR_SPECIFIC_INCREASES
          FOUR_SPECIFIC_INCREASES
        LENDINGCLUB_LOANS_INCREASES
          LENDINGCLUB_LOANS_INCREASES
        POSITIVE_RELATIONSHIP_EXISTS
          POSITIVE_RELATIONSHIP_EXISTS
        RESIDENTIAL_MORTGAGE_ORIGINATION
          RESIDENTIAL_MORTGAGE_ORIGINATION
        TAXONOMY_CONTRIBUTES
          TAXONOMY_CONTRIBUTES
    <BLANKLINE>
    <BLANKLINE>



"""

import re
import sys

from colorama import Fore, init

from ...._internals.mixins import ParamsMixin
from ....package_data.text_processing import internal__load_text_processing_terms
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header
from ..general.reduce_keys import ReduceKeys


class SortByLastWords(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__reduce_keys(self):
        ReduceKeys().update(**self.params.__dict__).run()

    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)

        if len(file_path) > 64:
            file_path = "..." + file_path[-60:]

        if self.params.use_colorama:
            filename = str(file_path).split("/")[-1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Sorting thesaurus by common last words...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Sorting process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(
            thesaurus_path=self.thesaurus_path, use_colorama=self.params.use_colorama
        )

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__select_data_frame_rows(self):

        self.data_frame["__row_selected__"] = False

        patterns = internal__load_text_processing_terms("common_last_words.txt")
        patterns = [pattern.strip().upper() for pattern in patterns]

        for pattern in patterns:

            self.data_frame.loc[
                self.data_frame.key.str.endswith(pat="_" + pattern),
                "__row_selected__",
            ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} matching keys found\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__run(self):

        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__select_data_frame_rows()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        # self.internal__reduce_keys()
        self.internal__build_user_thesaurus_path()
        self.internal__run()


# =============================================================================
