# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with OR
===============================================================================


Example:
    >>> from pprint import pprint
    >>> from techminer2.database.field_extractors import StemmingOrExtractor

    >>> # Creates, configures, and runs the extractor
    >>> extractor = (
    ...     StemmingOrExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords")
    ...     #
    ...     # SEARCH:
    ...     .having_pattern(
    ...         [
    ...             "financial technology",
    ...             "artificial intelligence",
    ...         ],
    ...     )
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> terms = extractor.run()

    >>> # Print the first 10 extracted terms
    >>> pprint(terms[:10])
    ['ARTIFICIAL_INTELLIGENCE',
     'DIGITAL_TECHNOLOGIES',
     'FINANCE_TECHNOLOGY',
     'FINANCIAL_COMPUTING',
     'FINANCIAL_INCLUSION',
     'FINANCIAL_INSTITUTION',
     'FINANCIAL_INTERMEDIATION',
     'FINANCIAL_MANAGEMENT',
     'FINANCIAL_SCENARIZATION',
     'FINANCIAL_SERVICE']



"""

from ..._internals.mixins import ParamsMixin
from ._internals.stemming import internal__stemming_or


class StemmingOrExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__stemming_or(self.params)
