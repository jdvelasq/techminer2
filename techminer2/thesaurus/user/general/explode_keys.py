# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
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
    ...     root_directory="example/", quiet=True).run()

    >>> # Creates, configures, an run the exploder
    >>> exploder = (
    ...     ExplodeKeys()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory_is("example/")
    ... )
    >>> exploder.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/data/thesaurus/demo.the.txt
      Keys reduced from 1726 to 1726
      Reduction process completed successfully
    <BLANKLINE>
    Exploding thesaurus keys
      File : example/data/thesaurus/demo.the.txt
      Keys reduced from 1726 to 1792
      Exploding process completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""
import sys

from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header
from .reduce_keys import ReduceKeys

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

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 72:
            truncated_path = "..." + truncated_path[-68:]
        sys.stderr.write(f"Exploding thesaurus keys\n")
        sys.stderr.write(f"  File : {truncated_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write(
            f"  Keys reduced from {self.n_initial_keys} to {self.n_final_keys}\n"
        )
        sys.stderr.write(f"  Exploding process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__explode_values(self):
        self.n_initial_keys = len(self.data_frame)
        self.data_frame["value"] = self.data_frame["value"].str.split("; ")
        self.data_frame = self.data_frame.explode("value")
        self.data_frame["value"] = self.data_frame["value"].str.strip()
        self.data_frame = self.data_frame.reset_index(drop=True)
        self.n_final_keys = len(self.data_frame)

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        ReduceKeys().update(**self.params.__dict__).run()

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__explode_values()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
