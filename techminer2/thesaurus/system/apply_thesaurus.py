# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Apply Thesaurus
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.system import ApplyThesaurus

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> #  Creating, configuring, and running the system thesaurus
    >>> applier = (
    ...     ApplyThesaurus(use_colorama=False)
    ...     .with_thesaurus_file("geography/country_to_region.the.txt")
    ...     .with_field("countries")
    ...     .with_other_field("regions")
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> applier.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Applying system thesaurus to database...
              File : ...2/package_data/thesaurus/geography/country_to_region.the.txt
      Source field : countries
      Target field : regions
      Application process completed successfully
    <BLANKLINE>
    <BLANKLINE>

"""
import sys

from colorama import Fore, init

from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_all_records_from_database,
    internal__write_records_to_database,
)
from techminer2.thesaurus._internals import (
    ThesaurusMixin,
    internal__load_thesaurus_as_mapping,
)


class ApplyThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        if not self.params.quiet:

            file_path = str(self.thesaurus_path)
            field = self.params.field
            other_field = self.params.other_field

            if len(file_path) > 64:
                file_path = "..." + file_path[-60:]

            if self.params.use_colorama:
                filename = str(file_path).rsplit("/", maxsplit=1)[1]
                file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
                file_path = Fore.LIGHTBLACK_EX + file_path

            sys.stderr.write("INFO: Applying system thesaurus to database...\n")
            sys.stderr.write(f"  Thesaurus    : {file_path}\n")
            sys.stderr.write(f"  Source field : {field}\n")
            sys.stderr.write(f"  Target field : {other_field}\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:

            sys.stderr.write(f"  Application process completed successfully\n")
            sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__load_thesaurus_as_mapping(self):
        self.mapping = internal__load_thesaurus_as_mapping(self.thesaurus_path)
        self.mapping = {k: v[0].strip() for k, v in self.mapping.items()}

    # -------------------------------------------------------------------------
    def internal__load_records(self):
        self.records = internal__load_all_records_from_database(params=self.params)

    # -------------------------------------------------------------------------
    def internal__copy_field(self):
        if self.params.field != self.params.other_field:
            self.records[self.params.other_field] = self.records[
                self.params.field
            ].copy()

    # -------------------------------------------------------------------------
    def internal__split_other_field(self):
        self.records[self.params.other_field] = self.records[
            self.params.other_field
        ].str.split("; ")

    # -------------------------------------------------------------------------
    def internal__apply_thesaurus_to_other_field(self):

        self.records[self.params.other_field] = self.records[
            self.params.other_field
        ].map(
            lambda x: [self.mapping.get(item, item) for item in x],
            na_action="ignore",
        )

    # -------------------------------------------------------------------------
    def internal__remove_duplicates_from_other_field(self):
        #
        def f(x):
            # remove duplicated terms preserving the order
            terms = []
            for term in x:
                if term not in terms:
                    terms.append(term)
            return terms

        self.records[self.params.other_field] = self.records[
            self.params.other_field
        ].map(f, na_action="ignore")

    # -------------------------------------------------------------------------
    def internal__split_other_field(self):
        self.records[self.params.other_field] = self.records[
            self.params.other_field
        ].str.split("; ")

    # -------------------------------------------------------------------------
    def internal__join_record_values(self):
        self.records[self.params.other_field] = self.records[
            self.params.other_field
        ].str.join("; ")

    # -------------------------------------------------------------------------
    def internal__write_records(self):
        internal__write_records_to_database(params=self.params, records=self.records)

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_system_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__load_records()
        self.internal__copy_field()
        self.internal__split_other_field()
        self.internal__apply_thesaurus_to_other_field()
        self.internal__remove_duplicates_from_other_field()
        self.internal__join_record_values()
        self.internal__write_records()
        self.internal__notify_process_end()


# =============================================================================
