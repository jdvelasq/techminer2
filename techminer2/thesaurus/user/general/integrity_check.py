# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# mypy: ignore-errors
"""
Integrity Check
===============================================================================


>>> from techminer2.thesaurus.user import CreateThesaurus
>>> CreateThesaurus(thesaurus_file="demo.the.txt", field="descriptors", 
...     root_directory="example/", quiet=True).run()

>>> from techminer2.thesaurus.user import IntegrityCheck
>>> (
...     IntegrityCheck()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .with_field("descriptors")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Thesaurus integrity check
  File : example/thesaurus/demo.the.txt
  1865 terms checked
  Integrity check completed successfully
<BLANKLINE>



"""
import sys

from ...._internals.mixins import ParamsMixin
from ....database._internals.io import internal__load_filtered_database
from ..._internals import ThesaurusMixin, internal__load_reversed_thesaurus_as_mapping


class IntegrityCheck(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = self.thesaurus_path

        sys.stdout.write("Thesaurus integrity check\n")
        sys.stdout.write(f"  File : {file_path}\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        n_terms = max(len(self.terms_in_thesaurus), len(self.terms_in_database))
        sys.stdout.write(f"  {n_terms} terms checked\n")
        sys.stdout.write(f"  Integrity check completed successfully\n\n")
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__load_terms_in_thesaurus(self):
        mapping = internal__load_reversed_thesaurus_as_mapping(self.thesaurus_path)
        self.terms_in_thesaurus = list(mapping.keys())

    # -------------------------------------------------------------------------
    def internal__load_terms_in_database(self):
        records = internal__load_filtered_database(params=self.params)
        field = self.params.field
        terms = records[field].dropna()
        terms = terms.str.split("; ").explode().str.strip().drop_duplicates().tolist()
        self.terms_in_database = terms

    # -------------------------------------------------------------------------
    def internal__compare_terms(self):

        terms_in_thesaurus = self.terms_in_thesaurus
        terms_in_database = self.terms_in_database

        union = set(terms_in_thesaurus).union(set(terms_in_database))

        self.missing_terms_in_database = None
        self.missing_terms_in_thesaurus = None

        if len(union) != len(terms_in_thesaurus) or len(union) != len(
            terms_in_database
        ):
            if len(terms_in_database) > len(terms_in_thesaurus):
                terms = set(terms_in_database) - set(terms_in_thesaurus)
                terms = list(terms)
                self.missing_terms_in_thesaurus = terms
            else:
                terms = set(terms_in_thesaurus) - set(terms_in_database)
                terms = list(terms)
                self.missing_terms_in_database = terms

    # -------------------------------------------------------------------------
    def internal__report_missing_terms(self):

        #
        terms = self.missing_terms_in_database
        if terms is not None:
            terms = terms[:10]
            sys.stdout.write(f"  Missing Terms in database:\n")
            for term in terms:
                sys.stdout.write(f"    - {term}\n")
            if len(terms) == 10:
                sys.stdout.write("    ...\n")
            sys.stdout.write("\n")
            sys.stdout.flush()

        #
        terms = self.missing_terms_in_thesaurus
        if terms is not None:
            terms = terms[:10]
            sys.stdout.write(f"  Missing Terms in thesaurus:\n")
            for i_term, term in enumerate(terms):
                sys.stdout.write(f"    - {term}\n")
            if len(terms) == 10:
                sys.stdout.write("    ...\n")
            sys.stdout.write("\n")
            sys.stdout.flush()

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_terms_in_thesaurus()
        self.internal__load_terms_in_database()
        self.internal__compare_terms()
        self.internal__report_missing_terms()
        self.internal__notify_process_end()


# =============================================================================
