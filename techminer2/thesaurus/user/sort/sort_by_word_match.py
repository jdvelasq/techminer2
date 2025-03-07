# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Word Match
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import CreateThesaurus, SortByWordMatch

    >>> # Redirecting stderr to avoid messages during doctests
    >>> old_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()


    >>> # Creates, configures, an run the sorter
    >>> sorter = (
    ...     SortByWordMatch()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_pattern("BUSINESS")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = old_stderr
    >>> print(output)
    Sorting thesaurus file by word match
      File : example/thesaurus/demo.the.txt
      Word : BUSINESS
      19 matching keys found
      Thesaurus sorting by word match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/demo.the.txt
    <BLANKLINE>
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
        FUNDAMENTALLY_NEW_BUSINESS_OPPORTUNITIES
          FUNDAMENTALLY_NEW_BUSINESS_OPPORTUNITIES
    <BLANKLINE>
    <BLANKLINE>


"""

import re
import sys

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class SortByWordMatch(
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

        if len(file_path) > 64:
            file_path = "..." + file_path[-60:]

        sys.stderr.write("Sorting thesaurus file by word match\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.write(f"  Word : {pattern}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Thesaurus sorting by word match completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__select_data_frame_rows(self):

        self.data_frame["__row_selected__"] = False

        patterns = self.params.pattern

        if isinstance(patterns, str):
            patterns = [patterns]

        for pattern in patterns:
            #
            for compiled_regex in [
                re.compile("^" + pattern + "$"),
                re.compile("^" + pattern + "_"),
                re.compile("^" + pattern + " "),
                re.compile("_" + pattern + "$"),
                re.compile(r" " + pattern + "$"),
                re.compile("_" + pattern + "_"),
                re.compile(r" " + pattern + "_"),
                re.compile("_" + pattern + r" "),
                re.compile(r" " + pattern + r" "),
            ]:
                self.data_frame.loc[
                    self.data_frame.key.str.contains(compiled_regex, regex=True),
                    "__row_selected__",
                ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} matching keys found\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__select_data_frame_rows()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
