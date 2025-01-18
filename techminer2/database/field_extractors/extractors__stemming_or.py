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
...     .set_custom_items(
...         [
...             "financial technology", 
...             "artificial intelligence",
...         ]
...     ) 
...     .set_source_field("author_keywords")
...     .set_root_dir("example/")
...     .set_database_filters(
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
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

from ...internals.set_params_mixin.set_custom_items_mixin import SetCustomItemsMixin
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ...internals.set_params_mixin.set_root_dir_mixin import SetRootDirMixin
from ...internals.set_params_mixin.set_source_field_mixin import SetSourceFieldMixin
from ..internals.field_extractors.internal__stemming import internal__stemming_or


class StemmingOrExtractor(
    SetCustomItemsMixin,
    SetDatabaseFiltersMixin,
    SetRootDirMixin,
    SetSourceFieldMixin,
):
    """:meta private:"""

    def __init__(self):

        self.custom_items = None
        self.root_dir = "./"
        self.source_field = None
        self.database_filters = DatabaseFilters()

    def build(self):

        return internal__stemming_or(
            custom_items=self.custom_items,
            source_field=self.source_field,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            **self.database_filters.__dict__,
        )
