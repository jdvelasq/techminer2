# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Fuzzy Match
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> from techminer2.thesaurus.user import InitializeThesaurus
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates, configures, an run the sorter
    >>> from techminer2.thesaurus.user import SortByFuzzyMatch
    >>> (
    ...     SortByFuzzyMatch(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_pattern("INTELL")
    ...     .having_match_threshold(70)
    ...     .where_root_directory("examples/fintech/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Sorting thesaurus by fuzzy match...
                File : examples/fintech/data/thesaurus/demo.the.txt
           Keys like : INTELL
      Match thresold : 70
      3 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/demo.the.txt
    <BLANKLINE>
        ARTIFICIAL_INTELLIGENCE
          ARTIFICIAL_INTELLIGENCE
        INTELLIGENT_ALGORITHMS
          INTELLIGENT_ALGORITHMS
        INTELLIGENT_ROBOTS
          INTELLIGENT_ROBOTS
        A_A_THEORY
          A_A_THEORY
        A_BASIC_RANDOM_SAMPLING_STRATEGY
          A_BASIC_RANDOM_SAMPLING_STRATEGY
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_BETTER_UNDERSTANDING
          A_BETTER_UNDERSTANDING
        A_BLOCKCHAIN_IMPLEMENTATION_STUDY
          A_BLOCKCHAIN_IMPLEMENTATION_STUDY
    <BLANKLINE>
    <BLANKLINE>





"""
import re
import sys

import pandas as pd  # type: ignore
from colorama import Fore, init
from fuzzywuzzy import process  # type: ignore

from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus._internals import (
    ThesaurusMixin,
    internal__print_thesaurus_header,
)
from techminer2.thesaurus.user.general.reduce_keys import ReduceKeys


class SortByFuzzyMatch(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = self.thesaurus_path
        pattern = self.params.pattern
        threshold = self.params.match_threshold

        if self.params.use_colorama:
            filename = str(file_path).rsplit("/", maxsplit=1)[1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Sorting thesaurus by fuzzy match...\n")
        sys.stderr.write(f"            File : {file_path}\n")
        sys.stderr.write(f"       Keys like : {pattern}\n")
        sys.stderr.write(f"  Match thresold : {threshold}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Sorting process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(
            thesaurus_path=self.thesaurus_path,
            use_colorama=self.params.use_colorama,
        )

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

        for pattern in self.params.pattern:

            # pattern = re.escape(pattern)
            key = self.data_frame.key.map(lambda x: re.escape(x))
            key = self.data_frame.key
            potential_matches = process.extract(pattern, key, limit=None)

            for potential_match in potential_matches:

                if potential_match[1] >= self.params.match_threshold:

                    self.data_frame.loc[
                        self.data_frame.key.str.contains(
                            potential_match[0], regex=False
                        ),
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
