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
...     .with_other_field("descriptors")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
--INFO-- The file example/thesaurus/descriptors.the.txt has been modified.

"""
import sys

import pandas as pd  # type: ignore

from ...database.internals.io import internal__load_records, internal__write_records
from ...internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_reversed_thesaurus_as_mapping,
)


class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_copy_field(self, records):
        if self.params.field != self.params.other_field:
            records[self.params.other_field] = records[self.params.field].copy()
        return records

    # -------------------------------------------------------------------------
    def step_02_split_other_field(self, records):
        records[self.params.other_field] = records[self.params.other_field].str.split(
            "; "
        )
        return records

    # -------------------------------------------------------------------------
    def step_03_apply_thesaurus_to_other_field(self, records, mapping):
        records[self.params.other_field] = records[self.params.other_field].map(
            lambda x: [mapping.get(item, item) for item in x], na_action="ignore"
        )
        return records

    # -------------------------------------------------------------------------
    def step_04_remove_duplicates_from_other_field(self, records):
        #
        def f(x):
            # remove duplicated terms preserving the order
            terms = []
            for term in x:
                if term not in terms:
                    terms.append(term)
            return terms

        records[self.params.other_field] = records[self.params.other_field].map(
            f, na_action="ignore"
        )
        return records

    # -------------------------------------------------------------------------
    def apply_thesaurus(self, records, mapping):

        records = self.step_01_copy_field(records)
        records = self.step_02_split_other_field(records)
        records = self.step_03_apply_thesaurus_to_other_field(records, mapping)
        records = self.step_04_remove_duplicates_from_other_field(records)
        return records

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__generate_user_thesaurus_file_path(params=self.params)
        mapping = internal__load_reversed_thesaurus_as_mapping(file_path)
        records = internal__load_records(params=self.params)
        #
        records = self.apply_thesaurus(records, mapping)
        #
        internal__write_records(params=self.params, records=records)
        #
        sys.stdout.write(f"--INFO-- The thesaurus file '{file_path}' has been applied.")
        sys.stdout.flush()
