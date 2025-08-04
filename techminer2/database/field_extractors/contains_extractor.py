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
Contains
===============================================================================

This module demonstrates how to extract terms from a specified field in a database
that contain a given pattern using the ContainsExtractor class. The process involves
configuring the field, search pattern, and database parameters.


Example:
    >>> from pprint import pprint
    >>> from techminer2.database.field_extractors import ContainsExtractor

    >>> # Creates, configures, and runs the extractor
    >>> extractor = (
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> terms = extractor.run()

    >>> # Print the first 10 extracted terms
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
from ..._internals.mixins import ParamsMixin
from ._internals.contains import internal__contains


class ContainsExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__contains(self.params)
