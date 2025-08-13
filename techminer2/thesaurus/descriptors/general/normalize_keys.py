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
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> from techminer2.thesaurus.descriptors import NormalizeKeys
    >>> (
    ...     NormalizeKeys(use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
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

from colorama import Fore
from colorama import init
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus._internals import internal__load_reversed_thesaurus_as_mapping
from techminer2.thesaurus._internals import internal__print_thesaurus_header
from techminer2.thesaurus._internals import ThesaurusMixin
from tqdm import tqdm  # type: ignore

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

        if self.params.use_colorama:
            filename = str(file_path).split("/")[-1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Cleanup Thesaurus...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Cleanup process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(
            thesaurus_path=self.thesaurus_path, use_colorama=self.params.use_colorama
        )

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
        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__transform_keys()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
