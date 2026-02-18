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


Smoke tests:
    >>> # Creates, configures, and runs the extractor
    >>> from techminer2.database.extractors import StemmingAndExtractor
    >>> terms = (
    ...     StemmingAndExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords_raw")
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
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )


    >>> # Print the first 10 extracted terms
    >>> from pprint import pprint
    >>> pprint(terms[:10])
    ['ARTIFICIAL_INTELLIGENCE',
     'FINANCIAL_TECHNOLOGY',
     'FINANCIAL_TECHNOLOGY (FINTECH)']


"""
from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.stemming import internal__stemming_and


class StemmingAndExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__stemming_and(self.params)


#
