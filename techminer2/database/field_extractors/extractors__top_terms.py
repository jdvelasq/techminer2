# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-few-public-methods
"""
Filter a Field
===============================================================================

>>> from techminer2.database.field_extractors import TopTermsExtractor
>>> terms = (
...     TopTermsExtractor()
...     #
...     .with_source_field("author_keywords")
...     .select_top_n_terms(10)
...     .order_terms_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['FINTECH',
 'INNOVATION',
 'FINANCIAL_SERVICES',
 'FINANCIAL_INCLUSION',
 'FINANCIAL_TECHNOLOGY',
 'CROWDFUNDING',
 'MARKETPLACE_LENDING',
 'BUSINESS_MODELS',
 'CYBER_SECURITY',
 'CASE_STUDY']

"""
from ...internals.mixins import InputFunctionsMixin
from ..internals.field_extractors.internal__top_terms import internal__top_terms


class TopTermsExtractor(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__top_terms(
            source_field=self.params.source_field,
            terms_order_criteria=self.params.terms_order_by,
            top_n_terms=self.params.top_n_terms,
            term_occurrences_range=self.params.term_occurrences_range,
            term_citations_range=self.params.term_citations_range,
            terms_in=self.params.terms_in,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
            database=self.params.database,
            record_years_range=self.params.record_years_range,
            record_citations_range=self.params.record_citations_range,
            records_order_by=self.params.records_order_by,
            records_match=self.params.records_match,
        )
