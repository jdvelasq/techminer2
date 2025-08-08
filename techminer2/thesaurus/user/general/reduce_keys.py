# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Reduce Keys
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import InitializeThesaurus, ReduceKeys

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()


    >>> # Reset the thesaurus to initial state
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates, configures, an run the reducer
    >>> reducer = (
    ...     ReduceKeys(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> reducer.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys...
      File : examples/fintech/data/thesaurus/demo.the.txt
      Keys reduced from 1724 to 1724
      Reduction process completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""
import sys

from colorama import Fore, init
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class ReduceKeys(
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
            filename = str(file_path).split("/")[-1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write(f"Reducing thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write(
            f"  Keys reduced from {self.n_initial_keys} to {self.n_final_keys}\n"
        )
        sys.stderr.write(f"  Reduction process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
