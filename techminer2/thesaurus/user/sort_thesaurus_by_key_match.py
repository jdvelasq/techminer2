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
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/descriptors.the.txt
           Keys like: BUSINESS
  Keys starting with: None
    Keys ending with: None
  104 matching keys found
Printing thesaurus header
  Loading example/thesaurus/descriptors.the.txt thesaurus file
  Header:
    AGRIBUSINESS
      AGRIBUSINESS
    AGRIBUSINESS_MANAGEMENT
      AGRIBUSINESS_MANAGEMENT
    A_BUSINESS_STRATEGY_EVALUATION_MODEL
      A_BUSINESS_STRATEGY_EVALUATION_MODEL
    A_SERVICE_BUSINESS
      A_SERVICE_BUSINESS
    BUSINESSES
      BUSINESS; BUSINESSES
    BUSINESS_ANALYSIS
      BUSINESS_ANALYSIS
    BUSINESS_AND_ECONOMICS
      BUSINESS_AND_ECONOMICS
    BUSINESS_AND_INFORMATION_SYSTEMS_RESEARCH
      BUSINESS_AND_INFORMATION_SYSTEMS_RESEARCH



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
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/descriptors.the.txt
           Keys like: None
  Keys starting with: BUSINESS
    Keys ending with: None
  49 matching keys found
Printing thesaurus header
  Loading example/thesaurus/descriptors.the.txt thesaurus file
  Header:
    BUSINESSES
      BUSINESS; BUSINESSES
    BUSINESS_ANALYSIS
      BUSINESS_ANALYSIS
    BUSINESS_AND_ECONOMICS
      BUSINESS_AND_ECONOMICS
    BUSINESS_AND_INFORMATION_SYSTEMS_RESEARCH
      BUSINESS_AND_INFORMATION_SYSTEMS_RESEARCH
    BUSINESS_AND_IT_ALIGNMENT
      BUSINESS_AND_IT_ALIGNMENT
    BUSINESS_AND_MANAGEMENT_RESEARCH
      BUSINESS_AND_MANAGEMENT_RESEARCH
    BUSINESS_APPLICATIONS_OF_COMPUTERS
      BUSINESS_APPLICATIONS_OF_COMPUTERS
    BUSINESS_ARCHITECTURE
      BUSINESS_ARCHITECTURE



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
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/descriptors.the.txt
           Keys like: None
  Keys starting with: None
    Keys ending with: BUSINESS
  16 matching keys found
Printing thesaurus header
  Loading example/thesaurus/descriptors.the.txt thesaurus file
  Header:
    AGRIBUSINESS
      AGRIBUSINESS
    A_SERVICE_BUSINESS
      A_SERVICE_BUSINESS
    DIGITAL_BUSINESS
      DIGITAL_BUSINESS
    EBUSINESS
      EBUSINESS
    ELECTRONIC_BUSINESS
      ELECTRONIC_BUSINESS
    ETHICS_BUSINESS
      BUSINESS_ETHICS; ETHICS_BUSINESS
    EURASIA_BUSINESS
      EURASIA_BUSINESS
    E_BUSINESS
      E_BUSINESS



"""
import sys

import pandas as pd  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_head,
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

        if self.params.show_progress:

            file_path = self.file_path
            pattern = self.params.pattern
            startswith = self.params.pattern_startswith
            endswith = self.params.pattern_endswith

            sys.stdout.write("Sorting thesaurus file by key match.\n")
            sys.stdout.write(f"      Thesaurus file: {file_path}\n")
            sys.stdout.write(f"           Keys like: {pattern}\n")
            sys.stdout.write(f"  Keys starting with: {startswith}\n")
            sys.stdout.write(f"    Keys ending with: {endswith}\n")

            sys.stdout.flush()

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

        if self.params.show_progress:
            sys.stdout.write(
                f"  {len(self.data_frame.key.drop_duplicates())} matching keys found\n"
            )
            sys.stdout.flush()

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
        if self.params.show_progress:
            internal__print_thesaurus_head(file_path=self.file_path)

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
