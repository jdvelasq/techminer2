# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Fuzzy Match
===============================================================================

>>> from techminer2.thesaurus.user import SortThesaurusByFuzzyMatch
>>> (
...     SortThesaurusByFuzzyMatch()
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


>>> # TEST:
>>> from techminer2.thesaurus._internals import internal__print_thesaurus_head
>>> from techminer2.internals import Params
>>> params = Params().update(thesaurus_file="descriptors.the.txt", root_dir="example/")
>>> internal__print_thesaurus_head(params, n=10)
-- INFO -- Thesaurus head 'example/thesaurus/descriptors.the.txt'.
         :        ANALYTICAL_INTELLIGENCE : ANALYTICAL_INTELLIGENCE                           
         :           AN_INTELLIGENT_AGENT : AN_INTELLIGENT_AGENT                              
         :        ARTIFICIAL_INTELLIGENCE : ARTIFICIAL_INTELLIGENCE                           
         : A_HYBRID_FUZZY_INTELLIGENT ... : A_HYBRID_FUZZY_INTELLIGENT_AGENT_BASED_SYSTEM     
         :          BUSINESS_INTELLIGENCE : BUSINESS_INTELLIGENCE                             
         :     BUSINESS_INTELLIGENCE (BI) : BUSINESS_INTELLIGENCE (BI)                        
         : BUSINESS_INTELLIGENCE_FRAM ... : BUSINESS_INTELLIGENCE_FRAMEWORK                   
         :        COLLECTIVE_INTELLIGENCE : COLLECTIVE_INTELLIGENCE                           
         :       COLLECTIVE_INTELLIGENCES : COLLECTIVE_INTELLIGENCES                          
         :       COMPETITIVE_INTELLIGENCE : COMPETITIVE_INTELLIGENCE                          


"""
import pandas as pd  # type: ignore
from fuzzywuzzy import process  # type: ignore

from ...internals.log_message import internal__log_message
from ...internals.mixins import ParamsMixin
from .._internals import (
    ThesaurusMixin,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)


class SortThesaurusByFuzzyMatch(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_revert_th_dict(self, th_dict):
        reversed_th_dict = {}
        for key, values in th_dict.items():
            for value in values:
                reversed_th_dict[value] = key
        return reversed_th_dict

    # -------------------------------------------------------------------------
    def step_02_build_data_frame(self, reversed_th_dict):
        return pd.DataFrame(
            {
                "text": reversed_th_dict.keys(),
                "key": reversed_th_dict.values(),
            }
        )

    # -------------------------------------------------------------------------
    def step_03_filter_data_frame(self, data_frame):
        result = []
        if self.params.pattern is not None:
            if isinstance(self.params.pattern, str):
                self.params.pattern = [self.params.pattern]

            for pattern in self.params.pattern:
                potential_matches = process.extract(
                    pattern, data_frame.text, limit=None
                )
                for potential_match in potential_matches:
                    if potential_match[1] >= self.params.match_threshold:
                        result.append(
                            data_frame[data_frame.text.str.contains(potential_match[0])]
                        )
        else:
            raise ValueError("No filter provided")

        return pd.concat(result)

    # -------------------------------------------------------------------------
    def step_04_extract_findings(self, th_dict, data_frame):
        keys = data_frame.key.drop_duplicates()
        findings = {key: th_dict[key] for key in sorted(keys)}
        return findings

    # -------------------------------------------------------------------------
    def step_05_save_sorted_thesaurus(self, file_path, th_dict, findings):

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
                "Sorting thesaurus by fuzzy match.",
                f"   Thesaurus file: '{file_path}'",
                f"        Keys like: '{self.params.pattern}'",
                f"  Match threshold: '{self.params.match_threshold}'",
            ],
            prompt_flag=self.params.prompt_flag,
            initial_newline=True,
        )
        #
        th_dict = internal__load_thesaurus_as_mapping(file_path)
        reversed_th_dict = self.step_01_revert_th_dict(th_dict)
        data_frame = self.step_02_build_data_frame(reversed_th_dict)
        data_frame = self.step_03_filter_data_frame(data_frame)
        findings = self.step_04_extract_findings(th_dict, data_frame)
        self.step_05_save_sorted_thesaurus(file_path, th_dict, findings)
        #
        internal__log_message(
            msgs=[f"          Founded: {len(findings)} keys."], prompt_flag=-1
        )
        self.print_thesaurus_head(n=5)
        internal__log_message(msgs=[f"  Done."], prompt_flag=-1)


# =============================================================================
