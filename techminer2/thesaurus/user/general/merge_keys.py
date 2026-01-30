# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Merge Keys
===============================================================================


Smoke tests:
    >>> from techminer2.thesaurus.user import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .where_root_directory("examples/small/")
    ...     .using_colored_output(False)
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success : True
      File    : examples/fintech/data/thesaurus/demo.the.txt
      Status  : 1721 keys found
      Header  :
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
        A_CASE_STUDY
          A_CASE_STUDY
        A_CHALLENGE
          A_CHALLENGE
        A_CLUSTER_ANALYSIS
          A_CLUSTER_ANALYSIS
    <BLANKLINE>

    >>> from techminer2.thesaurus.user import MergeKeys
    >>> (
    ...     MergeKeys()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_patterns_matching(["FINTECH", "FINANCIAL_TECHNOLOGIES"])
    ...     .where_root_directory("examples/small/")
    ...     .using_colored_output(False)
    ...     .run()
    ... )
    INFO: Thesaurus keys merged successfully.
      Success : True
      File    : examples/fintech/data/thesaurus/demo.the.txt
      Status  : 1 changed keys
      Header  :
        FINTECH
          FINANCIAL_TECHNOLOGIES; FINANCIAL_TECHNOLOGY; FINTECH; FINTECHS
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
        A_CASE_STUDY
          A_CASE_STUDY
        A_CHALLENGE
          A_CHALLENGE
    <BLANKLINE>



"""


from tqdm import tqdm  # type: ignore

from techminer2._internals import ParamsMixin
from techminer2.thesaurus._internals import ThesaurusMixin, ThesaurusResult

tqdm.pandas()


class MergeKeys(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__merge_keys(self):

        self.data_frame["__row_selected__"] = False

        lead_key = self.params.pattern[0]
        candidate_keys = self.params.pattern[1:]
        self.data_frame.loc[self.data_frame["key"] == lead_key, "__row_selected__"] = (
            True
        )

        for candidate in candidate_keys:
            self.data_frame.loc[self.data_frame["key"] == candidate, "key"] = lead_key

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self._build_user_thesaurus_path()
        self._load_thesaurus_as_mapping()
        self._transform_mapping_to_data_frame()
        self.internal__set_initial_keys()
        self.internal__merge_keys()
        self.internal__explode_and_group_values_by_key()
        self._sort_data_frame_by_rows_and_key()
        self._write_thesaurus_data_frame_to_disk()
        self.internal__set_final_keys()
        self.internal__compute_changed_keys()

        return ThesaurusResult(
            colored_output=self.params.colored_output,
            file_path=str(self.thesaurus_path),
            msg="Thesaurus keys merged successfully.",
            success=True,
            status=f"{self.total_key_changes} changed keys",
            data_frame=self.data_frame,
        )
