# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Key Match
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import CreateThesaurus, SortByKeyMatch

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()


    >>> # Creates, configures, an run the sorter
    >>> sorter = (
    ...     SortByKeyMatch()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_pattern("BUSINESS")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus file by key match
                File : example/thesaurus/demo.the.txt
             Pattern : BUSINESS
      Case sensitive : False
         Regex Flags : 0
        Regex Search : False
      21 matching keys found
      Thesaurus sorting by key match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/demo.the.txt
    <BLANKLINE>
        AGRIBUSINESS
          AGRIBUSINESS
        BUSINESS
          BUSINESS; BUSINESSES
        BUSINESS_DEVELOPMENT
          BUSINESS_DEVELOPMENT
        BUSINESS_GERMANY
          BUSINESS_GERMANY
        BUSINESS_INFRASTRUCTURE
          BUSINESS_INFRASTRUCTURE; BUSINESS_INFRASTRUCTURES
        BUSINESS_MODEL
          BUSINESS_MODEL; BUSINESS_MODELS
        BUSINESS_OPPORTUNITIES
          BUSINESS_OPPORTUNITIES
        BUSINESS_PROCESS
          BUSINESS_PROCESS
    <BLANKLINE>
    <BLANKLINE>


"""
import sys

import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header
from ..general.reduce_keys import ReduceKeys


class SortByKeyMatch(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)
        pattern = self.params.pattern
        case_sensitive = self.params.case_sensitive
        regex_flags = self.params.regex_flags
        regex_search = self.params.regex_search

        if len(file_path) > 64:
            file_path = "..." + file_path[-60:]

        sys.stderr.write("Sorting thesaurus file by key match\n")
        sys.stderr.write(f"            File : {file_path}\n")
        sys.stderr.write(f"         Pattern : {pattern}\n")
        sys.stderr.write(f"  Case sensitive : {case_sensitive}\n")
        sys.stderr.write(f"     Regex Flags : {regex_flags}\n")
        sys.stderr.write(f"    Regex Search : {regex_search}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Thesaurus sorting by key match completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__reduce_keys(self):
        ReduceKeys().update(**self.params.__dict__).run()

    # -------------------------------------------------------------------------
    def internal__select_data_frame_rows(self):

        self.data_frame["__row_selected__"] = False

        if isinstance(self.params.pattern, str):
            self.params.pattern = [self.params.pattern]

        for pat in self.params.pattern:

            self.data_frame.loc[
                self.data_frame.key.str.contains(
                    pat=pat,
                    case=self.params.case_sensitive,
                    flags=self.params.regex_flags,
                    regex=self.params.regex_search,
                ),
                "__row_selected__",
            ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} matching keys found\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__reduce_keys()
        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__select_data_frame_rows()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================
