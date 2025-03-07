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

This module demonstrates how to extract the top terms from a specified field in a database
using the TopTermsExtractor class. The process involves configuring the field, search
parameters, and database parameters.

Example:
    >>> from pprint import pprint
    >>> from techminer2.database.field_extractors import TopTermsExtractor

    >>> # Creates, configures, and runs the extractor
    >>> extractor = (
    ...     TopTermsExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_author_keywords")
    ...     #
    ...     # SEARCH:
    ...     .having_terms_in_top(10)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> terms = extractor.run()

    >>> # Print the first 10 extracted terms
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


This example shows how to extract the top terms from the "raw_author_keywords" field in the
database based on the specified parameters. The output includes the first 10 extracted terms.

"""
from ..._internals.mixins import ParamsMixin
from ..metrics.performance import DataFrame


class TopTermsExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()
        terms = data_frame.index.tolist()
        terms = sorted(terms)

        return terms
