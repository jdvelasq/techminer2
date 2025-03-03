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
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citattions_range_is(None, None)
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

from ..._internals.mixins import ParamsMixin
from ._internals.fields_difference import internal__fields_difference


class FieldsDifferenceExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__fields_difference(self.params)
