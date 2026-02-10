# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# mypy: ignore-errors
"""
Normalize Keys
===============================================================================


Example:

    >>> # Redirecting stderr to avoid messages
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Restore the thesaurus
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> from techminer2.refine.thesaurus_old.descriptors import NormalizeKeys
    >>> (
    ...     NormalizeKeys()
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +SKIP
    Normalizing Keys...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      15 replacements made successfully
      Normalization process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        *GEOGRAPHIC_REGIONS*
          AUSTRALIA_AND_NEW_ZEALAND; BRAZIL; CHINA; EUROPE; GERMANY; INDONESIA; KEN...
        *SURVEY*
          SURVEYS
        CONSTRUCT
          CONSTRUCTS
        ORGANIZATION
          BUSINESS; BUSINESSES; COMPANIES; FIRMS; ORGANIZATIONS
        A_A_THEORY
          A_A_THEORY
        A_BASIC_RANDOM_SAMPLING_STRATEGY
          A_BASIC_RANDOM_SAMPLING_STRATEGY
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_BETTER_UNDERSTANDING
          A_BETTER_UNDERSTANDING
    <BLANKLINE>
    <BLANKLINE>



"""
import sys
from importlib.resources import files

from colorama import Fore, init
from tqdm import tqdm  # type: ignore

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old._internals import (
    ThesaurusMixin,
    internal__load_reversed_thesaurus_as_mapping,
)

tqdm.pandas()


class NormalizeKeys(
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

        if self.params.colored_stderr:
            filename = str(file_path).rsplit("/", maxsplit=1)[1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Cleanup Thesaurus...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Cleanup process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__transform_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        file_path = files("techminer2.package_data.thesaurus.system").joinpath(
            "descriptors.the.txt"
        )
        file_path = str(file_path)

        mapping = internal__load_reversed_thesaurus_as_mapping(file_path)
        self.data_frame["key"] = self.data_frame["key"].map(lambda x: mapping.get(x, x))

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} replacements made successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("descriptors.the.txt")
        self._build_user_thesaurus_path()
        self.internal__notify_process_start()
        self._load_thesaurus_as_mapping()
        self._transform_mapping_to_data_frame()
        self.internal__transform_keys()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self._sort_data_frame_by_rows_and_key()
        self._write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
        self.internal__print_thesaurus_header_to_stream(n=8, stream=sys.stderr)
