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
<BLANKLINE>
Thesaurus sorting by key match completed successfully: ...hesaurus/demo.the.txt




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
    def notify__process_start(self):

        file_path = str(self.thesaurus_path)
        pattern = self.params.pattern

        if len(file_path) > 64:
            file_path = "..." + file_path[-60:]

        sys.stderr.write("\nSorting thesaurus file by key match")
        sys.stderr.write(f"\n                 File : {file_path}")
        sys.stderr.write(f"\n              Pattern : {pattern}")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def notify__process_end(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 26:
            truncated_path = "..." + truncated_path[-21:]
        sys.stderr.write("\n")
        sys.stdout.write(
            f"\nThesaurus sorting by key match completed successfully: {truncated_path}"
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
        if isinstance(self.params.pattern, str):
            self.params.pattern = [self.params.pattern]
        for pat in self.params.pattern:
            result.append(data_frame[data_frame.key.str.endswith(pat=pat)])
        #
        if result != []:
            self.data_frame = pd.concat(result)
            self.data_frame = self.data_frame.drop_duplicates("key")
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
    def run(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.notify__process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_thesaurus_mapping_to_data_frame()
        self.internal__filter_data_frame()
        self.internal__extract_findings()
        self.internal__write_thesaurus_mapping_to_disk()
        self.notify__process_end()

        internal__print_thesaurus_header(self.thesaurus_path)


# =============================================================================
