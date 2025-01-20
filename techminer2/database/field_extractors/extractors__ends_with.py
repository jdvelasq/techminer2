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
...     .for_field(
...         with_name="author_keywords", 
...         with_terms_having_pattern="ING",
...     ).for_data(
...         in_root_dir="example/",
...         where_database="main",
...         where_record_years_between=(None, None),
...         where_record_citations_between=(None, None),
...     ).build()
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


from ...internals.set_params_mixin.in_root_dir_mixin import SetRootDirMixin
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ...internals.set_params_mixin.set_field_mixin import SetFieldMixin
from ...internals.set_params_mixin.with_pattern_mixin import SetPatternMixin
from ..internals.field_extractors.internal__ends_with import internal__ends_with


class EndsWithExtractor(
    SetDatabaseFiltersMixin,
    SetFieldMixin,
    SetPatternMixin,
    SetRootDirMixin,
):
    """:meta private:"""

    def __init__(self):

        self.field = None
        self.pattern = None
        self.root_dir = "./"
        self.database_filters = DatabaseFilters()

    def build(self):

        return internal__ends_with(
            field=self.field,
            pattern=self.pattern,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            **self.database_filters.__dict__,
        )
