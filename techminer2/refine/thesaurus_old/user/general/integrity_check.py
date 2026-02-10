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


Smoke tests:
    >>> from techminer2.refine.thesaurus_old.user import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .where_root_directory("examples/small/")
    ...     .using_colored_output(False)
    ...     .run()
    ... )


    >>> # Creates, configures, an run the integrity checker
    >>> (
    ...     IntegrityCheck()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .where_root_directory("examples/small/")
    ...     .using_colored_output(False)
    ...     .run()
    ... )



"""
import sys

from colorama import Fore, init

from techminer2._internals import ParamsMixin
from techminer2._internals.data_access import load_filtered_main_data
from techminer2.refine.thesaurus_old._internals import (
    ThesaurusMixin,
    ThesaurusResult,
    internal__load_reversed_thesaurus_as_mapping,
)


class IntegrityCheck(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__load_terms_in_thesaurus(self):
        mapping = internal__load_reversed_thesaurus_as_mapping(self.thesaurus_path)
        self.terms_in_thesaurus = list(mapping.keys())

    # -------------------------------------------------------------------------
    def internal__load_terms_in_database(self):
        records = load_filtered_main_data(params=self.params)
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
            sys.stderr.write(f"  Missing Terms in database:\n")
            for term in terms:
                sys.stderr.write(f"    - {term}\n")
            if len(terms) == 10:
                sys.stderr.write("    ...\n")
            sys.stderr.write("\n")
            sys.stderr.flush()

        #
        terms = self.missing_terms_in_thesaurus
        if terms is not None:
            terms = terms[:10]
            sys.stderr.write(f"  Missing Terms in thesaurus:\n")
            for i_term, term in enumerate(terms):
                sys.stderr.write(f"    - {term}\n")
            if len(terms) == 10:
                sys.stderr.write("    ...\n")
            sys.stderr.write("\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):

        self._build_user_thesaurus_path()
        self.internal__load_terms_in_thesaurus()
        self.internal__load_terms_in_database()
        self.internal__compare_terms()
        self.internal__report_missing_terms()

        return ThesaurusResult(
            colored_output=self.params.colored_output,
            file_path=str(self.thesaurus_path),
            msg="Thesaurus applied successfully.",
            success=True,
            status=f"{len(self.mapping.keys())} keys applied",
            data_frame=None,
        )


# =============================================================================
