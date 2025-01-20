# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with AND
===============================================================================

>>> from techminer2.database.field_extractors import StemmingAndExtractor
>>> terms = (
...     StemmingAndExtractor() 
...     .for_field(
...         with_name="author_keywords", 
...         matching_terms_with(
...             [
...                 "financial technology", 
...                 "artificial intelligence",
...             ],
...         ), 
...     ).for_data(
...         in_root_dir="example/",
...         where_database="main",
...         where_record_years_between=(None, None),
...         where_record_citations_between=(None, None),
...     ).build()
... )
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['ARTIFICIAL_INTELLIGENCE',
 'FINANCIAL_TECHNOLOGY',
 'FINANCIAL_TECHNOLOGY (FINTECH)']

"""

from ...internals.set_params_mixin.in_root_dir_mixin import SetRootDirMixin
from ...internals.set_params_mixin.set_custom_items_mixin import SetCustomItemsMixin
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ...internals.set_params_mixin.set_source_field_mixin import SetSourceFieldMixin
from ..internals.field_extractors.internal__stemming import internal__stemming_and


class StemmingAndExtractor(
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

        return internal__stemming_and(
            custom_items=self.custom_items,
            source_field=self.source_field,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            **self.database_filters.__dict__,
        )
