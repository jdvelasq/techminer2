# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=attribute-defined-outside-init
"""
Explode Keys
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import InitializeThesaurus, ExplodeKeys

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()


    >>> # Reset the thesaurus to initial state
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates, configures, an run the exploder
    >>> (
    ...     ExplodeKeys(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory("examples/fintech/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +SKIP
    Reducing thesaurus keys...
      File : examples/fintech/data/thesaurus/demo.the.txt
      Keys reduced from 1721 to 1721
      Reduction process completed successfully
    <BLANKLINE>
    Exploding thesaurus keys...
      File : examples/fintech/data/thesaurus/demo.the.txt
      Keys expanded from 1721 to 1788
      Exploding process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/demo.the.txt
    <BLANKLINE>
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
        A_COMMON_UNDERSTANDING
          A_COMMON_UNDERSTANDING
    <BLANKLINE>
    <BLANKLINE>


"""
import sys

from colorama import Fore
from tqdm import tqdm  # type: ignore

from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus._internals import ThesaurusMixin
from techminer2.thesaurus.user.general.reduce_keys import ReduceKeys

tqdm.pandas()


class ExplodeKeys(
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

        sys.stderr.write("Exploding thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        msg = f"  Keys expanded from {self.n_initial_keys} to {self.n_final_keys}\n"
        sys.stderr.write(msg)
        sys.stderr.write("  Exploding process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__explode_values(self):
        self.data_frame["value"] = self.data_frame["value"].str.split("; ")
        self.data_frame = self.data_frame.explode("value")
        self.data_frame["value"] = self.data_frame["value"].str.strip()
        self.data_frame = self.data_frame.reset_index(drop=True)

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        ReduceKeys().update(**self.params.__dict__).run()

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__set_n_initial_keys()
        self.internal__explode_values()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__set_n_final_keys()
        self.internal__notify_process_end()
        self.internal__print_thesaurus_header(
            n=10,
            use_colorama=self.params.use_colorama,
        )
