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
...     .with_field("raw_descriptors")
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
from ...database._internals.io import internal__load_filtered_database
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_reversed_thesaurus_as_mapping,
)


class CheckThesaurusIntegrity(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):
        file_path = self.file_path
        sys.stdout.write("\nINFO  Checking thesaurus integrity.")
        sys.stdout.write(f"\n        Thesaurus file: {file_path}")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def step_03_load_terms_in_thesaurus(self):
        reversed_th_dict = internal__load_reversed_thesaurus_as_mapping(self.file_path)
        self.terms_in_thesaurus = list(reversed_th_dict.keys())

    # -------------------------------------------------------------------------
    def step_04_load_terms_in_database(self):
        records = internal__load_filtered_database(params=self.params)
        field = self.params.field
        terms = records[field].dropna()
        terms = terms.str.split("; ").explode().str.strip().drop_duplicates().tolist()
        self.terms_in_database = terms

    # -------------------------------------------------------------------------
    def step_05_compare_terms(self):

        terms_in_thesaurus = self.terms_in_thesaurus
        terms_in_database = self.terms_in_database

        union = set(terms_in_thesaurus).union(set(terms_in_database))

        if len(union) != len(terms_in_thesaurus) or len(union) != len(
            terms_in_database
        ):
            if len(terms_in_database) > len(terms_in_thesaurus):
                terms = set(terms_in_database) - set(terms_in_thesaurus)
            else:
                terms = set(terms_in_thesaurus) - set(terms_in_database)
            terms = list(terms)
        else:
            terms = None

        self.missing_terms = terms

    # -------------------------------------------------------------------------
    def step_06_print_missing_terms(self):

        terms = self.missing_terms

        if terms is not None:
            terms = terms[:10]
            for i_term, term in enumerate(terms):
                if i_term == 0:
                    sys.stdout.write(f"\n         Missing Terms: {term}")
                else:
                    sys.stdout.write(f"\n                        {term}")
            if len(terms) == 10:
                sys.stdout.write("\n                        ...")

        sys.stdout.write("\n        Done.")

    # -------------------------------------------------------------------------
    def build(self):

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_terms_in_thesaurus()
        self.step_04_load_terms_in_database()
        self.step_05_compare_terms()
        self.step_06_print_missing_terms()


# =============================================================================
