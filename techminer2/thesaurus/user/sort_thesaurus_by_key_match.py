# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key Match
===============================================================================


>>> from techminer2.thesaurus.user import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_like("BUSINESS")
...     .having_keys_starting_with(None)
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by key match completed successfully: ...s/descriptors.the.txt

>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_like(None)
...     .having_keys_starting_with("BUSINESS")
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by key match completed successfully: ...s/descriptors.the.txt

>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_like(None)
...     .having_keys_starting_with(None)
...     .having_keys_ending_with("BUSINESS")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by key match completed successfully: ...s/descriptors.the.txt


"""
import sys

import pandas as pd  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)


class SortThesaurusByKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):

        file_path = str(self.file_path)
        pattern = self.params.pattern
        startswith = self.params.pattern_startswith
        endswith = self.params.pattern_endswith

        if len(file_path) > 64:
            file_path = "..." + file_path[-60:]

        sys.stderr.write("\nSorting thesaurus file by key match")
        sys.stderr.write(f"\n       Thesaurus file : {file_path}")
        sys.stderr.write(f"\n            Keys like : {pattern}")
        sys.stderr.write(f"\n   Keys starting with : {startswith}")
        sys.stderr.write(f"\n     Keys ending with : {endswith}")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def step_03_load_thesaurus_as_mapping(self):
        self.th_dict = internal__load_thesaurus_as_mapping(self.file_path)

    # -------------------------------------------------------------------------
    def step_04_build_data_frame(self):
        self.data_frame = pd.DataFrame(
            {
                "key": self.th_dict.keys(),
                "value": self.th_dict.values(),
            }
        )

    # -------------------------------------------------------------------------
    def step_05_filter_data_frame(self):
        #
        data_frame = self.data_frame
        #
        result = []
        ##
        if self.params.pattern is not None:
            if isinstance(self.params.pattern, str):
                self.params.contains = [self.params.pattern]
            for word in self.params.contains:
                result.append(data_frame[data_frame.key.str.contains(word)])
        ##
        elif self.params.pattern_startswith is not None:
            if isinstance(self.params.pattern_startswith, str):
                self.params.pattern_startswith = [self.params.pattern_startswith]
            for word in self.params.pattern_startswith:
                result.append(data_frame[data_frame.key.str.startswith(word)])
        ##
        elif self.params.pattern_endswith is not None:
            if isinstance(self.params.pattern_endswith, str):
                self.params.pattern_endswith = [self.params.pattern_endswith]
            for word in self.params.pattern_endswith:
                result.append(data_frame[data_frame.key.str.endswith(word)])
        ##
        else:
            raise ValueError("No filter provided")
        ##
        self.data_frame = pd.concat(result)
        self.data_frame = self.data_frame.drop_duplicates("key")

        sys.stderr.write(
            f"\n  Matching keys found : {len(self.data_frame.key.drop_duplicates())}"
        )
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def step_06_extract_findings(self):
        keys = self.data_frame.key.drop_duplicates()
        findings = {key: self.th_dict[key] for key in sorted(keys)}
        self.findings = findings

    # -------------------------------------------------------------------------
    def step_07_save_thesaurus(self):

        for key in self.findings.keys():
            self.th_dict.pop(key)

        with open(self.file_path, "w", encoding="utf-8") as file:

            # write the finding keys
            for key in sorted(self.findings.keys()):
                file.write(key + "\n")
                for item in self.findings[key]:
                    file.write("    " + item + "\n")

            # write the remaining keys
            for key in sorted(self.th_dict.keys()):
                file.write(key + "\n")
                for item in self.th_dict[key]:
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def step_08_print_info_tail(self):

        sys.stderr.write("\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(file_path=self.file_path)
        ##
        truncated_file_path = str(self.file_path)
        if len(truncated_file_path) > 26:
            truncated_file_path = "..." + truncated_file_path[-21:]
        sys.stdout.write(
            f"\nThesaurus sorting by key match completed successfully: {truncated_file_path}"
        )
        sys.stdout.flush()
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_thesaurus_as_mapping()
        self.step_04_build_data_frame()
        self.step_05_filter_data_frame()
        self.step_06_extract_findings()
        self.step_07_save_thesaurus()
        self.step_08_print_info_tail()


# =============================================================================
