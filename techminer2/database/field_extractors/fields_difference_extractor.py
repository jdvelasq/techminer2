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

Example:
    >>> from pprint import pprint
    >>> from techminer2.database.field_extractors import FieldsDifferenceExtractor

    >>> # Creates, configures, and runs the extractor
    >>> extractor = (
    ...     FieldsDifferenceExtractor()
    ...     #
    ...     # FIELDS:
    ...     .with_field("raw_author_keywords")
    ...     .with_other_field("raw_index_keywords")
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

from ..._internals.mixins import ParamsMixin
from ._internals.fields_difference import internal__fields_difference


class FieldsDifferenceExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__fields_difference(self.params)
