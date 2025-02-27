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

>>> from techminer2.thesaurus.user import ApplyThesaurus
>>> (
...     ApplyThesaurus()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     #
...     # FIELDS:
...     .with_field("descriptors")
...     .with_other_field("descriptors_cleaned")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
<BLANKLINE>
Thesaurus application completed successfully for file: ...s/descriptors.the.txt

"""
import sys

from ...._internals.mixins import ParamsMixin
from ....database._internals.io import internal__load_records, internal__write_records
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

        file_path = str(self.thesaurus_path)
        field = self.params.field
        other_field = self.params.other_field

        if len(file_path) > 64:
            file_path = "..." + file_path[-60:]

        sys.stderr.write("\nApplying thesaurus to database")
        sys.stderr.write(f"\n          File : {file_path}")
        sys.stderr.write(f"\n  Source field : {field}")
        sys.stderr.write(f"\n  Target field : {other_field}")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("\n")
        sys.stderr.flush()

        truncated_file_path = str(self.thesaurus_path)
        if len(truncated_file_path) > 25:
            truncated_file_path = "..." + truncated_file_path[-21:]
        sys.stdout.write(
            f"\nThesaurus application completed successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__load_reversed_thesaurus_as_mapping(self):
        self.mapping = internal__load_reversed_thesaurus_as_mapping(self.thesaurus_path)

    # -------------------------------------------------------------------------
    def internal__load_records(self):
        self.records = internal__load_records(params=self.params)

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
    def internal__write_records(self):
        internal__write_records(params=self.params, records=self.records)

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_reversed_thesaurus_as_mapping()
        self.internal__load_records()
        self.internal__copy_field()
        self.internal__split_other_field()
        self.internal__apply_thesaurus_to_other_field()
        self.internal__remove_duplicates_from_other_field()
        self.internal__write_records()
        self.internal__notify_process_end()


# =============================================================================
