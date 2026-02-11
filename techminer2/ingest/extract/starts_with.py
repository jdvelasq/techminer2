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


Smoke tests:
    >>> # Creates, configures, and runs the extractor
    >>> from techminer2.database.extractors import StartsWithExtractor
    >>> terms = (
    ...     StartsWithExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords_raw")
    ...     #
    ...     # SEARCH:
    ...     .having_pattern("FINAN")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )


    >>> # Print the first 10 extracted terms
    >>> from pprint import pprint
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
from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.starts_with import internal__starts_with


class StartsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__starts_with(self.params)


#
