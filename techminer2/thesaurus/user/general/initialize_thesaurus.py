# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Initialize Thesaurus
===============================================================================


Example:
    >>> # TEST:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import InitializeThesaurus

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Initialize the thesaurus
    >>> initializator = (
    ...     InitializeThesaurus(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> initializator.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Initializing thesaurus from 'raw_descriptors' field...
      File : examples/fintech/data/thesaurus/demo.the.txt
      1724 keys found
      Initialization process completed successfully
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
    <BLANKLINE>
    <BLANKLINE>

"""
import sys

import pandas as pd  # type: ignore
from colorama import Fore, init
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class InitializeThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        if not self.params.quiet:

            field = self.params.field
            file_path = str(self.thesaurus_path)
            if len(file_path) > 72:
                file_path = "..." + file_path[-68:]

            if self.params.use_colorama:
                filename = str(file_path).split("/")[-1]
                file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
                file_path = Fore.LIGHTBLACK_EX + file_path

            sys.stderr.write(f"Initializing thesaurus from '{field}' field...\n")
            sys.stderr.write(f"  File : {file_path}\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:

            sys.stderr.write(f"  {len(self.data_frame)} keys found\n")
            sys.stderr.write("  Initialization process completed successfully\n\n")
            sys.stderr.flush()

            internal__print_thesaurus_header(
                thesaurus_path=self.thesaurus_path,
                use_colorama=self.params.use_colorama,
            )

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_filtered_records()
        self.internal__create_thesaurus_data_frame_from_field()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
