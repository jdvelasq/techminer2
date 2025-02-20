# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Fuzzy Key Match
===============================================================================

>>> from techminer2.thesaurus.user import SortThesaurusByFuzzyKeyMatch
>>> (
...     SortThesaurusByFuzzyKeyMatch()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_like("INTELLIGE")
...     .having_match_threshold(70)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus by fuzzy match
  Thesaurus file: example/thesaurus/descriptors.the.txt
       Keys like: INTELLIGE
  Match thresold: 70
  38 matching keys found
Printing thesaurus header
  Loading example/thesaurus/descriptors.the.txt thesaurus file
  Header:
    ANALYTICAL_INTELLIGENCE
      ANALYTICAL_INTELLIGENCE
    AN_INTELLIGENT_AGENT
      AN_INTELLIGENT_AGENT
    ARTIFICIAL_INTELLIGENCE
      ARTIFICIAL_INTELLIGENCE
    A_HYBRID_FUZZY_INTELLIGENT_AGENT_BASED_SYSTEM
      A_HYBRID_FUZZY_INTELLIGENT_AGENT_BASED_SYSTEM
    BUSINESS_INTELLIGENCE
      BUSINESS_INTELLIGENCE
    BUSINESS_INTELLIGENCE (BI)
      BUSINESS_INTELLIGENCE (BI)
    BUSINESS_INTELLIGENCE_FRAMEWORK
      BUSINESS_INTELLIGENCE_FRAMEWORK
    COLLECTIVE_INTELLIGENCES
      COLLECTIVE_INTELLIGENCE; COLLECTIVE_INTELLIGENCES


"""
import sys

import pandas as pd  # type: ignore
from fuzzywuzzy import process  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals import (
    ThesaurusMixin,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_head,
)


class SortThesaurusByFuzzyKeyMatch(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):

        if self.params.show_progress:

            file_path = self.file_path
            pattern = self.params.pattern
            threshold = self.params.match_threshold

            sys.stdout.write("Sorting thesaurus by fuzzy match\n")
            sys.stdout.write(f"  Thesaurus file: {file_path}\n")
            sys.stdout.write(f"       Keys like: {pattern}\n")
            sys.stdout.write(f"  Match thresold: {threshold}\n")

            sys.stdout.flush()

    # -------------------------------------------------------------------------
    def step_03_load_thesaurus_as_mapping(self):
        self.th_dict = internal__load_thesaurus_as_mapping(self.file_path)

    # -------------------------------------------------------------------------
    def step_04_revert_th_dict(self):
        reversed_th_dict = {}
        for key, values in self.th_dict.items():
            for value in values:
                reversed_th_dict[value] = key
        self.reversed_th_dict = reversed_th_dict

    # -------------------------------------------------------------------------
    def step_05_build_data_frame(self):
        self.data_frame = pd.DataFrame(
            {
                "text": self.reversed_th_dict.keys(),
                "key": self.reversed_th_dict.values(),
            }
        )

    # -------------------------------------------------------------------------
    def step_06_filter_data_frame(self):
        data_frame = self.data_frame
        result = []
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
            self.data_frame = pd.concat(result)
            self.data_frame = self.data_frame.drop_duplicates()
        else:
            self.data_frame = None

        if self.params.show_progress:
            if self.data_frame is None:
                sys.stdout.write("  No matching keys found\n")
            else:
                sys.stdout.write(
                    f"  {len(self.data_frame.key.drop_duplicates())} matching keys found\n"
                )
                sys.stdout.flush()

    # -------------------------------------------------------------------------
    def step_07_extract_findings(self):
        if self.data_frame is None:
            self.findings = {}
            return
        keys = self.data_frame.key.drop_duplicates()
        findings = {key: self.th_dict[key] for key in sorted(keys)}
        self.findings = findings

    # -------------------------------------------------------------------------
    def step_08_save_sorted_thesaurus(self):

        for key in self.findings.keys():
            self.th_dict.pop(key)

        with open(self.file_path, "w", encoding="utf-8") as file:
            for key in sorted(self.findings.keys()):
                file.write(key + "\n")
                for item in self.findings[key]:
                    file.write("    " + item + "\n")

            for key in sorted(self.th_dict.keys()):
                file.write(key + "\n")
                for item in self.th_dict[key]:
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def step_09_print_info_tail(self):
        if self.params.show_progress:
            internal__print_thesaurus_head(file_path=self.file_path)

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_thesaurus_as_mapping()
        self.step_04_revert_th_dict()
        self.step_05_build_data_frame()
        self.step_06_filter_data_frame()
        self.step_07_extract_findings()
        self.step_08_save_sorted_thesaurus()
        self.step_09_print_info_tail()


# =============================================================================
