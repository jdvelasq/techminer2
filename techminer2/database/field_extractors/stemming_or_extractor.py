# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with OR
===============================================================================

>>> from techminer2.database.field_extractors import StemmingOrExtractor
>>> terms = (
...     StemmingOrExtractor() 
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     #
...     # SEARCH:
...     .having_terms_like(
...         [
...             "financial technology", 
...             "artificial intelligence",
...         ],
...     )
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
['ARTIFICIAL_INTELLIGENCE',
 'DIGITAL_TECHNOLOGIES',
 'FINANCE_TECHNOLOGY',
 'FINANCIAL_COMPUTING',
 'FINANCIAL_INCLUSION',
 'FINANCIAL_INSTITUTION',
 'FINANCIAL_INSTITUTIONS',
 'FINANCIAL_INTERMEDIATION',
 'FINANCIAL_MANAGEMENT',
 'FINANCIAL_SCENARIZATION']

"""

from ..._internals.mixins import ParamsMixin
from ._internals.stemming import internal__stemming_or


class StemmingOrExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__stemming_or(self.params)
