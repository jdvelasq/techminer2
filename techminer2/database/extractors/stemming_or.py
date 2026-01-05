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
    >>> # Creates, configures, and runs the extractor
    >>> from techminer2.database.extractors import StemmingOrExtractor
    >>> terms = (
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
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )


    >>> # Print the first 10 extracted terms
    >>> from pprint import pprint
    >>> pprint(terms[:10]) # doctest: +SKIP
    ['ARTIFICIAL_INTELLIGENCE',
     'DIGITAL_TECHNOLOGIES',
     'FINANCE_TECHNOLOGY',
     'FINANCIAL_COMPUTING',
     'FINANCIAL_INCLUSION',
     'FINANCIAL_INSTITUTION',
     'FINANCIAL_INSTITUTIONS',
     'FINANCIAL_INTERMEDIATION',
     'FINANCIAL_MANAGEMENT',
     'FINANCIAL_SCENARIZATION']




"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.extractors.stemming import internal__stemming_or


class StemmingOrExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__stemming_or(self.params)


#
