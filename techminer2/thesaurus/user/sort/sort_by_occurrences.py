# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Occurrences
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import InitializeThesaurus, SortByOccurrences

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates, configures, an run the sorter
    >>> sorter = (
    ...     SortByOccurrences()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .where_root_directory("examples/fintech/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output) # doctest: +SKIP
    Sorting thesaurus by occurrences...
      File : examples/fintech/data/thesaurus/demo.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/demo.the.txt
    <BLANKLINE>
        FINTECH
          FINTECH; FINTECHS
        FINANCE
          FINANCE
        TECHNOLOGIES
          TECHNOLOGIES; TECHNOLOGY
        INNOVATION
          INNOVATION; INNOVATIONS
        FINANCIAL_SERVICE
          FINANCIAL_SERVICE; FINANCIAL_SERVICES
        FINANCIAL_TECHNOLOGIES
          FINANCIAL_TECHNOLOGIES; FINANCIAL_TECHNOLOGY
        BANKS
          BANKS
        THE_DEVELOPMENT
          THE_DEVELOPMENT; THE_DEVELOPMENTS
    <BLANKLINE>
    <BLANKLINE>




"""
import sys

from colorama import Fore, init

from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_filtered_records_from_database,
)
from techminer2.thesaurus._internals import ThesaurusMixin
from techminer2.thesaurus.user.general.reduce_keys import ReduceKeys


class SortByOccurrences(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)

        if self.params.colored_stderr:
            filename = file_path.rsplit("/", maxsplit=1)[1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Sorting thesaurus by occurrences...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Sorting process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__reduce_keys(self):
        ReduceKeys().update(**self.params.__dict__).run()

    # -------------------------------------------------------------------------
    def internal__get_raw_occurrences(self):

        records = internal__load_filtered_records_from_database(params=self.params)
        records = records[[self.params.field]]
        records = records.dropna()
        records[self.params.field] = records[self.params.field].str.split("; ")
        records = records.explode(self.params.field)
        records[self.params.field] = records[self.params.field].str.strip()
        records["OCC"] = 1
        counts = records.groupby(self.params.field, as_index=True).agg({"OCC": "sum"})

        self.raw_key2occ = dict(zip(counts.index, counts.OCC))

    # -------------------------------------------------------------------------
    def internal__compute_key_occurrences(self):

        self.key_occurrences = self.data_frame.copy()

        self.key_occurrences["value"] = self.key_occurrences["value"].str.split("; ")
        self.key_occurrences = self.key_occurrences.explode("value")
        self.key_occurrences["value"] = self.key_occurrences["value"].str.strip()

        self.key_occurrences["OCC"] = self.key_occurrences.value.map(
            # lambda x: raw_key2occ.get(x, 1)
            lambda x: self.raw_key2occ[x]
        )
        self.key_occurrences["OCC"] = self.key_occurrences["OCC"].astype(int)
        self.key_occurrences = self.key_occurrences[["key", "OCC"]]
        self.key_occurrences = self.key_occurrences.groupby("key", as_index=False).agg(
            {"OCC": "sum"}
        )

        keys2occ = dict(zip(self.key_occurrences.key, self.key_occurrences.OCC))

        self.data_frame["OCC"] = self.data_frame.key.map(keys2occ)

        self.data_frame = self.data_frame.sort_values(
            ["OCC", "key"], ascending=[False, True]
        )

    # -------------------------------------------------------------------------
    def internal__run(self):

        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__get_raw_occurrences()
        self.internal__compute_key_occurrences()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
        self.internal__print_thesaurus_header_to_stream(n=8, stream=sys.stderr)

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        # self.internal__reduce_keys()
        self.internal__build_user_thesaurus_path()
        self.internal__run()


# =============================================================================


# =============================================================================
