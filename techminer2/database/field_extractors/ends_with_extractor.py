# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Ends With
===============================================================================

>>> from techminer2.database.field_extractors import EndsWithExtractor
>>> terms = (
...     EndsWithExtractor() 
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     #
...     # SEARCH:
...     .having_terms_like("ING")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
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
from ..._internals.mixins import ParamsMixin
from ._internals.ends_with import internal__ends_with


class EndsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__ends_with(self.params)
