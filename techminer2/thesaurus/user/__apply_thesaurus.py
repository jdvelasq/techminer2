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
...     .where_directory_is("example/")
...     #
...     .build()
... )


"""
import sys

from ..._internals.log_message import internal__log_message
from ..._internals.mixins import ParamsMixin
from ...database._internals.io import internal__load_records, internal__write_records
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_reversed_thesaurus_as_mapping,
)


class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):

        file_path = self.file_path
        field = self.params.field
        other_field = self.params.other_field

        sys.stdout.write("\nINFO  Applying thesaurus to database.")
        sys.stdout.write(f"\n        Thesaurus file: {file_path}")
        sys.stdout.write(f"\n          Source field: {field}")
        sys.stdout.write(f"\n          Target field: {other_field}")

        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def step_03_load_reversed_thesaurus_as_mapping(self):
        self.mapping = internal__load_reversed_thesaurus_as_mapping(self.file_path)

    # -------------------------------------------------------------------------
    def step_04_load_records(self):
        self.records = internal__load_records(params=self.params)

    # -------------------------------------------------------------------------
    def step_05_copy_field(self):
        if self.params.field != self.params.other_field:
            self.records[self.params.other_field] = self.records[
                self.params.field
            ].copy()

    # -------------------------------------------------------------------------
    def step_06_split_other_field(self):
        self.records[self.params.other_field] = self.records[
            self.params.other_field
        ].str.split("; ")

    # -------------------------------------------------------------------------
    def step_07_apply_thesaurus_to_other_field(self):

        self.records[self.params.other_field] = self.records[
            self.params.other_field
        ].map(
            lambda x: [self.mapping.get(item, item) for item in x],
            na_action="ignore",
        )

    # -------------------------------------------------------------------------
    def step_08_remove_duplicates_from_other_field(self):
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
    def step_09_write_records(self):
        internal__write_records(params=self.params, records=self.records)

    # -------------------------------------------------------------------------
    def step_10_print_info_tail(self):
        sys.stdout.write("\n        Done.")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_reversed_thesaurus_as_mapping()
        self.step_04_load_records()
        self.step_05_copy_field()
        self.step_06_split_other_field()
        self.step_07_apply_thesaurus_to_other_field()
        self.step_08_remove_duplicates_from_other_field()
        self.step_09_write_records()
        self.step_10_print_info_tail()


# =============================================================================
