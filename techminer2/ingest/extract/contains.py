"""
Contains
===============================================================================

This module demonstrates how to extract terms from a specified field in a database
that contain a given pattern using the ContainsExtractor class. The process involves
configuring the field, search pattern, and database parameters.


Smoke tests:
    >>> # Creates, configures, and runs the extractor
    >>> from techminer2.database.extractors import ContainsExtractor
    >>> terms = (
    ...     ContainsExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords")
    ...     #
    ...     # SEARCH:
    ...     .having_pattern("FINTECH")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
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
    ['BANK_FINTECH_PARTNERSHIP',
     'FINANCIAL_TECHNOLOGY (FINTECH)',
     'FINTECH',
     'FINTECH_DISRUPTION',
     'FINTECH_INDUSTRY',
     'FINTECH_SERVICES']

This example shows how to extract terms from the "author_keywords" field in the database
that contain the pattern "FINTECH". The output includes the first 10 extracted terms.
"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.contains import internal__contains


class ContainsExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__contains(self.params)


#
