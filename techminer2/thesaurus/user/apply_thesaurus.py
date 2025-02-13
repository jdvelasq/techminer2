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
--INFO-- The file example/thesauri/descriptors.the.txt has been modified.

"""
from ...database.io import RecordsLoader, RecordsWriter
from ...internals.mixins import InputFunctionsMixin
from ..internals import (
    internal__build_thesaurus_file_path,
    internal__load_reversed_thesaurus_as_dict,
)


class ApplyThesaurus(
    InputFunctionsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def apply_thesaurus(self, records, mapping):

        if self.params.field != self.params.other_field:
            records[self.params.other_field] = records[self.params.field].copy()

        records[self.params.other_field] = records[self.params.other_field].str.split(
            "; "
        )
        records[self.params.other_field] = records[self.params.other_field].apply(
            lambda x: [mapping.get(item, item) for item in x]
        )
        records[self.params.other_field] = records[self.params.other_field].apply(
            lambda x: "; ".join(sorted(set(x)))
        )
        return records

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__build_thesaurus_file_path(params=self.params)
        mapping = internal__load_reversed_thesaurus_as_dict(file_path)
        records = RecordsLoader().update_params(**self.params.__dict__).build()
        records = self.apply_thesaurus(records, mapping)
        RecordsWriter().update_params(**self.params.__dict__).with_records(
            records
        ).build()
