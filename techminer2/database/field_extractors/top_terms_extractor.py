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
...     # FIELD:
...     .with_field("author_keywords")
...     #
...     # SEARCH:
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['BUSINESS_MODELS',
 'CASE_STUDY',
 'CROWDFUNDING',
 'CYBER_SECURITY',
 'FINANCIAL_INCLUSION',
 'FINANCIAL_SERVICES',
 'FINANCIAL_TECHNOLOGY',
 'FINTECH',
 'INNOVATION',
 'MARKETPLACE_LENDING']

"""
from ...internals.mixins import InputFunctionsMixin
from ..metrics.performance import DataFrame


class TopTermsExtractor(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        data_frame = DataFrame().update_params(**self.params.__dict__).build()
        terms = data_frame.index.tolist()
        terms = sorted(terms)

        return terms
