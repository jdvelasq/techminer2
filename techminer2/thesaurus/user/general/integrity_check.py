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
<BLANKLINE>
Integrity checking successfully for file: example/thesaurus/demo.the.txt



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

        sys.stderr.write("\nThesaurus integrity check")
        sys.stderr.write(f"\n  File : {file_path}")
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 37:
            truncated_path = "..." + truncated_path[-33:]
        sys.stdout.write(
            f"\nIntegrity checking successfully for file: {truncated_path}"
        )
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
            sys.stderr.write(f"\n  Missing Terms in database:")
            for term in terms:
                sys.stderr.write(f"\n    - {term}")
            if len(terms) == 10:
                sys.stderr.write("\n    ...")
            sys.stderr.write("\n")
            sys.stderr.flush()

        #
        terms = self.missing_terms_in_thesaurus
        if terms is not None:
            terms = terms[:10]
            sys.stderr.write(f"\n  Missing Terms in thesaurus:")
            for i_term, term in enumerate(terms):
                sys.stderr.write(f"\n    - {term}")
            if len(terms) == 10:
                sys.stderr.write("\n    ...")
            sys.stderr.write("\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__build_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_terms_in_thesaurus()
        self.internal__load_terms_in_database()
        self.internal__compare_terms()
        self.internal__report_missing_terms()
        self.internal__notify_process_end()


# =============================================================================
