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
...     .set_compare_field("author_keywords") 
...     .set_to_field("index_keywords")
...     .set_root_dir("example/")
...     .set_database_filters(
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
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

from ...internals.set_params_mixin.set_compare_field_mixin import SetCompareFieldMixin
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ...internals.set_params_mixin.set_root_dir_mixin import SetRootDirMixin
from ...internals.set_params_mixin.set_to_field_mixin import SetToFieldMixin
from ..internals.field_extractors.internal__fields_difference import (
    internal__fields_difference,
)


class FieldsDifferenceExtractor(
    SetCompareFieldMixin,
    SetDatabaseFiltersMixin,
    SetRootDirMixin,
    SetToFieldMixin,
):
    """:meta private:"""

    def __init__(self):

        self.compare_field = None
        self.root_dir = "./"
        self.to_field = None
        self.database_filters = DatabaseFilters()

    def build(self):

        return internal__fields_difference(
            compare_field=self.compare_field,
            to_field=self.to_field,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            **self.database_filters.__dict__,
        )
