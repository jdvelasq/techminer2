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


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> from techminer2.thesaurus.user import InitializeThesaurus
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="examples/fintech/", quiet=True).run()

    >>> from techminer2.thesaurus.user import MergeKeys
    >>> (
    ...     MergeKeys(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_patterns(["FINTECH", "FINANCIAL_TECHNOLOGIES"])
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +SKIP
    Merging thesaurus keys...
      File : examples/fintech/data/thesaurus/demo.the.txt
      Keys : FINTECH; FINANCIAL_TECHNOLOGIES
      Keys reduced from 1721 to 1720
      Merging process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/demo.the.txt
    <BLANKLINE>
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
        A_CLUSTER_ANALYSIS
          A_CLUSTER_ANALYSIS
        A_COMMON_TOOL
          A_COMMON_TOOL
    <BLANKLINE>
    <BLANKLINE>



"""
import sys

from colorama import Fore
from tqdm import tqdm  # type: ignore

from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus._internals import ThesaurusMixin

tqdm.pandas()


class MergeKeys(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)

        if len(file_path) > 72:
            file_path = "..." + file_path[-68:]

        if self.params.use_colorama:
            filename = str(file_path).rsplit("/", maxsplit=1)[1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Merging thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.write(f"  Keys : {'; '.join(self.params.pattern)}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        msg = f"  Keys reduced from {self.n_initial_keys} to {self.n_final_keys}\n"
        sys.stderr.write(msg)
        sys.stderr.write("  Merging process completed successfully\n\n")
        sys.stderr.flush()

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

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__set_n_initial_keys()
        self.internal__merge_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__set_n_final_keys()
        self.internal__notify_process_end()
        self.internal__print_thesaurus_header(
            n=10,
            use_colorama=self.params.use_colorama,
        )
