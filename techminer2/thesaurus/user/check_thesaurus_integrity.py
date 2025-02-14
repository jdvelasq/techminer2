# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# mypy: ignore-errors
"""
Check Thesaurus Integrity
===============================================================================


>>> from techminer2.thesaurus.user import CheckThesaurusIntegrity
>>> (
...     CheckThesaurusIntegrity()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .with_field("descriptors")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
--INFO-- Checking `descriptors.the.txt` integrity.

"""
import sys

from ...database.internals.io import internal__load_filtered_database
from ...internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_reversed_thesaurus_as_mapping,
)


class CheckThesaurusIntegrity(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def load_terms_in_thesaurus(self):
        file_path = internal__generate_user_thesaurus_file_path(params=self.params)
        reversed_th_dict = internal__load_reversed_thesaurus_as_mapping(file_path)
        terms = list(reversed_th_dict.keys())
        return terms

    # -------------------------------------------------------------------------
    def load_terms_in_database(self):
        records = internal__load_filtered_database(params=self.params)
        field = self.params.field
        terms = records[field].dropna()
        terms = terms.str.split("; ").explode().str.strip().drop_duplicates().tolist()
        return terms

    # -------------------------------------------------------------------------
    def compare_terms(self, terms_in_thesaurus, terms_in_database):
        union = set(terms_in_thesaurus).union(set(terms_in_database))
        if len(union) != len(terms_in_thesaurus) or len(union) != len(
            terms_in_database
        ):
            if len(terms_in_database) > len(terms_in_thesaurus):
                print(set(terms_in_database) - set(terms_in_thesaurus))
            else:
                print(set(terms_in_thesaurus) - set(terms_in_database))

        assert len(union) == len(terms_in_database)
        assert len(union) == len(terms_in_thesaurus)

    # -------------------------------------------------------------------------
    def build(self):
        terms_in_thesaurus = self.load_terms_in_thesaurus()
        terms_in_database = self.load_terms_in_database()
        self.compare_terms(terms_in_thesaurus, terms_in_database)

        sys.stdout.write(f"--INFO-- Checking {self.params.thesaurus_file} integrity.")
        sys.stdout.flush()


# =============================================================================
