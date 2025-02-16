# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Match
===============================================================================

>>> from techminer2.thesaurus.user import SortThesaurusByMatch
>>> (
...     SortThesaurusByMatch()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_like("alphabetical")
...     .having_keys_starting_with(None)
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
--INFO-- The thesaurus file 'example/thesaurus/descriptors.the.txt' has been rerodered.

"""
import sys

import pandas as pd  # type: ignore

from ...internals.log_message import internal__log_message
from ...internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)


class SortThesaurusByMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def revert_th_dict(self, th_dict):
        reversed_th_dict = {}
        for key, values in th_dict.items():
            for value in values:
                reversed_th_dict[value] = key
        return reversed_th_dict

    # -------------------------------------------------------------------------
    def build_data_frame(self, reversed_th_dict):
        return pd.DataFrame(
            {
                "text": reversed_th_dict.keys(),
                "key": reversed_th_dict.values(),
            }
        )

    # -------------------------------------------------------------------------
    def filter_data_frame(self, data_frame):
        result = []
        if self.params.pattern is not None:
            if isinstance(self.params.pattern, str):
                self.params.contains = [self.params.pattern]
            for word in self.params.contains:
                result.append(data_frame[data_frame.text.str.contains(word)])
        elif self.params.pattern_startswith is not None:
            if isinstance(self.params.pattern_startswith, str):
                self.params.pattern_startswith = [self.params.pattern_startswith]
            for word in self.params.pattern_startswith:
                result.append(data_frame[data_frame.text.str.startswith(word)])
        elif self.params.endswith is not None:
            if isinstance(self.params.pattern_endswith, str):
                self.params.pattern_endswith = [self.params.pattern_endswith]
            for word in self.params.pattern_endswith:
                result.append(data_frame[data_frame.text.str.endswith(word)])
        else:
            raise ValueError("No filter provided")
        return pd.concat(result)

    # -------------------------------------------------------------------------
    def extract_findings(self, th_dict, data_frame):
        keys = data_frame.key.drop_duplicates()
        findings = {key: th_dict[key] for key in sorted(keys)}
        return findings

    # -------------------------------------------------------------------------
    def save_sorted_thesaurus(self, file_path, th_dict, findings):

        for key in findings.keys():
            th_dict.pop(key)

        with open(file_path, "w", encoding="utf-8") as file:
            for key in sorted(findings.keys()):
                file.write(key + "\n")
                for item in findings[key]:
                    file.write("    " + item + "\n")

            for key in sorted(th_dict.keys()):
                file.write(key + "\n")
                for item in th_dict[key]:
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__generate_user_thesaurus_file_path(params=self.params)
        #
        internal__log_message(
            msgs=[
                "Sorting thesaurus by match.",
                f"      Thesaurus file: '{file_path}'",
                f"           Keys like: '{self.params.like}'",
                f"  Keys starting with: '{self.params.startswith}'",
                f"    Keys ending with: '{self.params.endswith}'",
            ],
            counter_flag=self.params.counter_flag,
        )
        #
        th_dict = internal__load_thesaurus_as_mapping(file_path)
        reversed_th_dict = self.revert_th_dict(th_dict)
        data_frame = self.build_data_frame(reversed_th_dict)
        data_frame = self.filter_data_frame(data_frame)
        findings = self.extract_findings(th_dict, data_frame)
        self.save_sorted_thesaurus(file_path, th_dict, findings)

        internal__log_message(
            msgs=f"  Done.",
            counter_flag=-1,
        )


# =============================================================================
