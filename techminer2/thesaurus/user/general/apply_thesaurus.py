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
    >>> #
    >>> # TEST PREPARATION
    >>> #
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import ApplyThesaurus, CreateThesaurus

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()

    >>> # Creates, configures, and runs the applier
    >>> applier = (
    ...     ApplyThesaurus()
    ...     .with_thesaurus_file("descriptors.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .with_other_field("descriptors_cleaned")
    ...     .where_root_directory_is("example/")
    ... )
    >>> applier.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Applying user thesaurus to database
              File : example/thesaurus/descriptors.the.txt
      Source field : raw_descriptors
      Target field : descriptors_cleaned
      Thesaurus application completed successfully
    <BLANKLINE>
    <BLANKLINE>

    >>> # Query the database to check the results
    >>> from techminer2.database.tools import Query
    >>> Query(
    ...     query_expression="SELECT descriptors_cleaned FROM database LIMIT 5;",
    ...     root_directory="example/",
    ...     database="main",
    ...     record_years_range=(None, None),
    ...     record_citations_range=(None, None),
    ... ).run()
                                     descriptors_cleaned
    0  AN_EFFECT; AN_INSTITUTIONAL_ASPECT; AN_MODERAT...
    1  ACTOR_NETWORK_THEORY; ANT; AN_UNPRECEDENTED_LE...
    2  AN_INITIAL_TECHNOLOGY_ADVANTAGE; CHINA; FINANC...
    3  AGGREGATION; ANALYSIS; AN_ADVANTAGE; AN_EXTENS...
    4  ACCELERATE_ACCESS; A_FORM; BEHAVIORAL_ECONOMIC...


    >>> # Deletes the created field in the database
    >>> from techminer2.database.field_operators import DeleteFieldOperator
    >>> DeleteFieldOperator(field="descriptors_cleaned", root_directory="example/").run()


"""
import sys

from ...._internals.mixins import ParamsMixin
from ....database._internals.io import (
    internal__load_all_records_from_database,
    internal__write_records_to_database,
)
from ..._internals import ThesaurusMixin, internal__load_reversed_thesaurus_as_mapping


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

            sys.stderr.write("Applying user thesaurus to database\n")
            sys.stderr.write(f"          File : {file_path}\n")
            sys.stderr.write(f"  Source field : {field}\n")
            sys.stderr.write(f"  Target field : {other_field}\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:

            sys.stderr.write(f"  Thesaurus application completed successfully\n\n")
            sys.stderr.flush()

    #
    # ALGORITHM:
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

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_reversed_thesaurus_as_mapping()
        self.internal__load_records()
        self.internal__copy_field()
        self.internal__split_other_field()
        self.internal__apply_thesaurus_to_other_field()
        self.internal__remove_duplicates_from_other_field()
        self.internal__join_record_values()
        self.internal__write_records()
        self.internal__notify_process_end()


# =============================================================================
