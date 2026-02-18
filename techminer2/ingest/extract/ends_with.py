# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Ends With
===============================================================================

Smoke tests:
    >>> # Creates, configures, and runs the extractor
    >>> from techminer2.database.extractors import EndsWithExtractor
    >>> terms = (
    ...     EndsWithExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords")
    ...     #
    ...     # SEARCH:
    ...     .having_pattern("ING")
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
    ['BANKING',
     'CLOUD_COMPUTING',
     'CROWDFUNDING',
     'DATA_MINING',
     'DIGITAL_BANKING',
     'ECONOMIC_FORECASTING',
     'FINANCIAL_COMPUTING',
     'FUTURE_OF_BANKING',
     'LENDING',
     'MARKETPLACE_LENDING']


"""
from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.ends_with import internal__ends_with


class EndsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__ends_with(self.params)


#
