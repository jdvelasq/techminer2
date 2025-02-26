# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Fuzzy Key Match Sorter
===============================================================================

>>> from techminer2.thesaurus.user import FuzzyKeyMatchSorter
>>> (
...     FuzzyKeyMatchSorter()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_pattern("INTELL")
...     .having_match_threshold(70)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by fuzzy key match completed successfully: ...us/demo.the.txt



"""
import sys

import pandas as pd  # type: ignore
from fuzzywuzzy import process  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals import ThesaurusMixin, internal__print_thesaurus_header


class FuzzyKeyMatchSorter(
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

        sys.stderr.write("\nSorting thesaurus by fuzzy match")
        sys.stderr.write(f"\n                 File : {thesaurus_path}")
        sys.stderr.write(f"\n            Keys like : {pattern}")
        sys.stderr.write(f"\n       Match thresold : {threshold}")

        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 20:
            truncated_path = "..." + truncated_path[-15:]
        sys.stdout.write(
            f"\nThesaurus sorting by fuzzy key match completed successfully: {truncated_path}"
        )
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__filter_data_frame(self):
        #
        data_frame = self.data_frame
        #
        result = []
        #
        if self.params.pattern is not None:
            if isinstance(self.params.pattern, str):
                self.params.pattern = [self.params.pattern]

            for pattern in self.params.pattern:
                potential_matches = process.extract(pattern, data_frame.key, limit=None)
                for potential_match in potential_matches:
                    if potential_match[1] >= self.params.match_threshold:
                        result.append(
                            data_frame[
                                data_frame.key.str.contains(
                                    potential_match[0], regex=False
                                )
                            ]
                        )
        else:
            raise ValueError("No filter provided")

        if result != []:
            self.result = pd.concat(result)
            self.data_frame = self.result.drop_duplicates("key")
        else:
            self.data_frame = None

        if self.data_frame is None:
            sys.stderr.write("\n  Matching keys found : 0")
        else:
            sys.stderr.write(
                f"\n  Matching keys found : {len(self.data_frame.key.drop_duplicates())}"
            )
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_thesaurus_mapping_to_data_frame()
        self.internal__filter_data_frame()
        self.internal__extract_findings()
        self.internal__write_thesaurus_mapping_to_disk()
        self.internal__notify_process_end()

        internal__print_thesaurus_header(self.thesaurus_path)


# =============================================================================
