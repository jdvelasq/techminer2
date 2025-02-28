# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Fuzzy Key Match
===============================================================================

>>> from techminer2.thesaurus.user import CreateThesaurus
>>> CreateThesaurus(thesaurus_file="demo.the.txt", field="descriptors", 
...     root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.user import SortByFuzzyKeyMatch
>>> (
...     SortByFuzzyKeyMatch()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_pattern("INTELL")
...     .having_match_threshold(70)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 
Sorting thesaurus by fuzzy match
            File : example/thesaurus/demo.the.txt
       Keys like : INTELL
  Match thresold : 70
  3 matching keys found
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/demo.the.txt
<BLANKLINE>
    ARTIFICIAL_INTELLIGENCE
      ARTIFICIAL_INTELLIGENCE
    INTELLIGENT_ALGORITHMS
      INTELLIGENT_ALGORITHMS
    INTELLIGENT_ROBOTS
      INTELLIGENT_ROBOTS
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




"""
import sys

import pandas as pd  # type: ignore
from fuzzywuzzy import process  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class SortByFuzzyKeyMatch(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        thesaurus_path = self.thesaurus_path
        pattern = self.params.pattern
        threshold = self.params.match_threshold

        sys.stdout.write("Sorting thesaurus by fuzzy match\n")
        sys.stdout.write(f"            File : {thesaurus_path}\n")
        sys.stdout.write(f"       Keys like : {pattern}\n")
        sys.stdout.write(f"  Match thresold : {threshold}\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stdout.write("  Thesaurus sorting completed successfully\n\n")
        sys.stdout.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__select_data_frame_rows(self):

        self.data_frame["__row_selected__"] = False

        if isinstance(self.params.pattern, str):
            self.params.pattern = [self.params.pattern]

        for pattern in self.params.pattern:

            potential_matches = process.extract(
                pattern, self.data_frame.key, limit=None
            )

            for potential_match in potential_matches:

                if potential_match[1] >= self.params.match_threshold:

                    self.data_frame.loc[
                        self.data_frame.key.str.contains(
                            potential_match[0], regex=False
                        ),
                        "__row_selected__",
                    ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stdout.write(f"  {n_matches} matching keys found\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__select_data_frame_rows()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================
