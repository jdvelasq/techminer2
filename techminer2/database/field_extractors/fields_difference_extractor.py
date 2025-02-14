# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Fields difference
===============================================================================

>>> from techminer2.database.field_extractors import FieldsDifferenceExtractor
>>> terms = (
...     FieldsDifferenceExtractor() 
...     #
...     # FIELDS:
...     .with_field("author_keywords")
...     .with_other_field("index_keywords")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
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

from ...internals.mixins import ParamsMixin
from .internals.internal__fields_difference import internal__fields_difference


class FieldsDifferenceExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__fields_difference(
            #
            # FIELDS:
            field=self.params.field,
            other_field=self.params.other_field,
            #
            # DATABASE:
            root_dir=self.params.root_dir,
            database=self.params.database,
            record_years_range=self.params.record_years_range,
            record_citations_range=self.params.record_citations_range,
            records_order_by=self.params.records_order_by,
            records_match=self.params.records_match,
        )
