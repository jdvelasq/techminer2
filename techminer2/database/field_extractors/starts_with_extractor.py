# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Starts With
===============================================================================


Example:
    >>> from pprint import pprint
    >>> from techminer2.database.field_extractors import StartsWithExtractor

    >>> # Creates, configures, and runs the extractor
    >>> extractor = (
    ...     StartsWithExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_author_keywords")
    ...     #
    ...     # SEARCH:
    ...     .having_pattern("FINAN")
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
    ['FINANCE',
     'FINANCE_TECHNOLOGY',
     'FINANCIALISATION',
     'FINANCIAL_COMPUTING',
     'FINANCIAL_INCLUSION',
     'FINANCIAL_INSTITUTION',
     'FINANCIAL_INSTITUTIONS',
     'FINANCIAL_INTERMEDIATION',
     'FINANCIAL_MANAGEMENT',
     'FINANCIAL_SCENARIZATION']



"""

from ..._internals.mixins import ParamsMixin
from ._internals.starts_with import internal__starts_with


class StartsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__starts_with(self.params)
