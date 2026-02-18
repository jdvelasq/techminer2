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
Fields difference
===============================================================================

Smoke tests:
    >>> # Creates, configures, and runs the extractor
    >>> from techminer2.database.extractors import DifferenceExtractor
    >>> terms = (
    ...     DifferenceExtractor()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords_raw")
    ...     .with_other_field("index_keywords_raw")
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
    ['ADOPTION',
     'AI',
     'ALTERNATIVE_DATA',
     'BANKING_COMPETITION',
     'BANKING_INNOVATIONS',
     'BANKS',
     'BANK_FINTECH_PARTNERSHIP',
     'BEHAVIOURAL_ECONOMICS',
     'BLOCKCHAINS',
     'BUSINESS_MODEL']


"""
from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.difference import internal__difference


class DifferenceExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__difference(self.params)


#
