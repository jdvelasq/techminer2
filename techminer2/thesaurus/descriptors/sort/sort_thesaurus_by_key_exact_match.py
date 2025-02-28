# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key Exact Match
===============================================================================

>>> from techminer2.thesaurus.descriptors import SortThesaurusByKeyExactMatch
>>> (
...     SortThesaurusByKeyExactMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("ARTIFICIAL_INTELLIGENCE")
...     .having_keys_starting_with(None)
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by exact key match completed successfully: ...riptors.the.txt


>>> (
...     SortThesaurusByKeyExactMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with("ARTIFICIAL")
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by exact key match completed successfully: ...riptors.the.txt


>>> (
...     SortThesaurusByKeyExactMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with(None)
...     .having_keys_ending_with("INTELLIGENCE")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by exact key match completed successfully: ...riptors.the.txt

"""
import re
import sys

import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
    internal__print_thesaurus_header,
)


class SortThesaurusByKeyExactMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):

        def format_pattern(pat):
            if isinstance(pat, str):
                pat = [pat]
            pat = "; ".join(pat) if pat is not None else None
            if pat is not None:
                if len(pat) > 58:
                    pat = pat[:55] + "..."
            return pat

        file_path = self.file_path
        pattern = self.params.pattern
        startswith = self.params.pattern_startswith
        endswith = self.params.pattern_endswith

        pattern = format_pattern(pattern)
        startswith = format_pattern(startswith)
        endswith = format_pattern(endswith)

        sys.stdout.write(f"\nSorting thesaurus by key exact match")
        sys.stdout.write(f"\n                File : {file_path}")
        sys.stdout.write(f"\n           Keys like : {pattern}")
        sys.stdout.write(f"\n  Keys starting with : {startswith}")
        sys.stdout.write(f"\n    Keys ending with : {endswith}")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def step_03_load_thesaurus_as_data_frame(self):
        self.data_frame = internal__load_thesaurus_as_data_frame(self.file_path)

    # -------------------------------------------------------------------------
    def step_04_search_keys(self):

        data_frame = self.data_frame

        result = []

        #
        # CONTAINS:
        #
        if self.params.pattern is not None:

            patterns = self.params.pattern

            if isinstance(patterns, str):
                patterns = [patterns]

            for pattern in patterns:
                #
                for compiled_regex in [
                    re.compile("^" + pattern + "_"),
                    re.compile("^" + pattern + r"\b"),
                    re.compile("_" + pattern + "$"),
                    re.compile(r"\b" + pattern + "$"),
                    re.compile("_" + pattern + "_"),
                    re.compile(r"\b" + pattern + "_"),
                    re.compile("_" + pattern + r"\b"),
                    re.compile(r"\b" + pattern + r"\b"),
                ]:
                    result.append(
                        data_frame[
                            data_frame.key.str.contains(compiled_regex, regex=True)
                        ]
                    )
        #
        # STARTSWITH:
        #
        elif self.params.pattern_startswith is not None:

            patterns = self.params.pattern_startswith

            if isinstance(patterns, str):
                patterns = [patterns]

            for pattern in patterns:

                for compiled_regex in [
                    re.compile("^" + pattern + "_"),
                    re.compile("^" + pattern + r"\b"),
                ]:
                    result.append(
                        data_frame[
                            data_frame.key.str.contains(compiled_regex, regex=True)
                        ]
                    )
        #
        # ENDSWITH:
        #
        elif self.params.pattern_endswith is not None:

            patterns = self.params.pattern_endswith

            if isinstance(patterns, str):
                patterns = [patterns]

            for pattern in patterns:

                for compiled_regex in [
                    re.compile("_" + pattern + "$"),
                    re.compile(r"\b" + pattern + "$"),
                ]:
                    result.append(
                        data_frame[
                            data_frame.key.str.contains(compiled_regex, regex=True)
                        ]
                    )
        #
        # ERROR:
        #
        else:
            raise ValueError("No filter provided")

        self.findings = pd.concat(result).drop_duplicates()

    # -------------------------------------------------------------------------
    def step_05_save_thesaurus(self):

        first_df = self.findings
        second_df = self.data_frame[~self.data_frame.key.isin(first_df.key)]

        first_df = first_df.groupby("key")["value"].apply(list)
        second_df = second_df.groupby("key")["value"].apply(list)

        with open(self.file_path, "w", encoding="utf-8") as file:

            for key in sorted(first_df.index):
                file.write(key + "\n")
                for value in first_df[key]:
                    file.write(f"    {value}\n")

            for key in sorted(second_df.index):
                file.write(key + "\n")
                for value in second_df[key]:
                    file.write(f"    {value}\n")

    # -------------------------------------------------------------------------
    def step_06_print_info_tail(self):

        sys.stdout.write("\n")
        sys.stdout.flush()
        internal__print_thesaurus_header(thesaurus_path=self.file_path)
        ##

        truncated_file_path = str(self.file_path)
        if len(truncated_file_path) > 19:
            truncated_file_path = "..." + truncated_file_path[-15:]
        sys.stdout.write(
            f"\nThesaurus sorting by exact key match completed successfully: {truncated_file_path}"
        )
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.with_thesaurus_file("descriptors.the.txt")

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_thesaurus_as_data_frame()
        self.step_04_search_keys()
        self.step_05_save_thesaurus()
        self.step_06_print_info_tail()
