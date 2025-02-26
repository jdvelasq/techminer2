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

>>> from techminer2.database.field_extractors import StartsWithExtractor
>>> terms = (
...     StartsWithExtractor() 
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     #
...     # SEARCH:
...     .having_terms_like("FINAN")
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

    def build(self):

        return internal__starts_with(self.params)
