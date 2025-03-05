# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Ends With Key Match
===============================================================================


>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.user import CreateThesaurus
>>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors", 
...     root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.user import SortByEndsWithKeyMatch
>>> (
...     SortByEndsWithKeyMatch()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_pattern("BUSINESS")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 


>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus file by key match
     File : example/thesaurus/demo.the.txt
  Pattern : BUSINESS
  3 matching keys found
  Thesaurus sorting by key match completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/demo.the.txt
<BLANKLINE>
    AGRIBUSINESS
      AGRIBUSINESS
    BUSINESS
      BUSINESS; BUSINESSES
    THE_BANKING_BUSINESS
      THE_BANKING_BUSINESS
    A_A_)_THEORY
      A_A_)_THEORY
    A_A_THEORY
      A_A_THEORY
    A_BASIC_RANDOM_SAMPLING_STRATEGY
      A_BASIC_RANDOM_SAMPLING_STRATEGY
    A_BEHAVIOURAL_PERSPECTIVE
      A_BEHAVIOURAL_PERSPECTIVE
    A_BETTER_UNDERSTANDING
      A_BETTER_UNDERSTANDING
<BLANKLINE>
<BLANKLINE>



"""
import sys

import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class SortByEndsWithKeyMatch(
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

        sys.stderr.write("Sorting thesaurus file by key match\n")
        sys.stderr.write(f"     File : {file_path}\n")
        sys.stderr.write(f"  Pattern : {pattern}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Thesaurus sorting by key match completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__select_data_frame_rows(self):

        self.data_frame["__row_selected__"] = False

        if isinstance(self.params.pattern, str):
            self.params.pattern = [self.params.pattern]

        for pat in self.params.pattern:

            self.data_frame.loc[
                self.data_frame.key.str.endswith(pat=pat),
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


# =============================================================================
