# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Contains
===============================================================================

>>> from techminer2.database.field_extractors import ContainsExtractor
>>> terms = (
...     ContainsExtractor() 
...     .set_pattern("FINTECH")
...     .set_field("author_keywords") 
...     .set_root_dir("example/")
...     .set_database_filters(
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['BANK_FINTECH_PARTNERSHIP',
 'FINANCIAL_TECHNOLOGY (FINTECH)',
 'FINTECH',
 'FINTECH_DISRUPTION',
 'FINTECH_INDUSTRY',
 'FINTECH_SERVICES']


"""


from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ...internals.set_params_mixin.set_field_mixin import SetFieldMixin
from ...internals.set_params_mixin.set_pattern_mixin import SetPatternMixin
from ...internals.set_params_mixin.set_root_dir_mixin import SetRootDirMixin
from ..internals.field_extractors.internal__contains import internal__contains


class ContainsExtractor(
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

        return internal__contains(
            field=self.field,
            pattern=self.pattern,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            **self.database_filters.__dict__,
        )
