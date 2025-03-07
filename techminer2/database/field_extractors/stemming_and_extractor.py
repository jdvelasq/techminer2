# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with AND
===============================================================================


Example:
    >>> from pprint import pprint
    >>> from techminer2.database.field_extractors import StemmingAndExtractor

    >>> # Creates, configures, and runs the extractor
    >>> extractor = (
    ...     StemmingAndExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_author_keywords")
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
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> terms = extractor.run()

    >>> # Print the first 10 extracted terms
    >>> pprint(terms[:10])
    ['ARTIFICIAL_INTELLIGENCE',
     'FINANCIAL_TECHNOLOGY',
     'FINANCIAL_TECHNOLOGY (FINTECH)']


"""

from ..._internals.mixins import ParamsMixin
from ._internals.stemming import internal__stemming_and


class StemmingAndExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__stemming_and(self.params)
