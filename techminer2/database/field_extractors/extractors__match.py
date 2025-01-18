# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Match
===============================================================================

>>> from techminer2.database.field_extractors import MatchExtractor
>>> terms = (
...     MatchExtractor() 
...     .set_pattern("L.+")
...     .set_case(False)
...     .set_flags(0)
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
['LENDING', 'LENDINGCLUB', 'LITERATURE_REVIEW']

"""

from ...internals.set_params_mixin.set_case_mixin import SetCaseMixin
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ...internals.set_params_mixin.set_field_mixin import SetFieldMixin
from ...internals.set_params_mixin.set_flags_mixin import SetFlagsMixin
from ...internals.set_params_mixin.set_pattern_mixin import SetPatternMixin
from ...internals.set_params_mixin.set_root_dir_mixin import SetRootDirMixin
from ..internals.field_extractors.internal__match import internal__match


class MatchExtractor(
    SetCaseMixin,
    SetDatabaseFiltersMixin,
    SetFieldMixin,
    SetFlagsMixin,
    SetPatternMixin,
    SetRootDirMixin,
):
    """:meta private:"""

    def __init__(self):

        self.case = False
        self.field = None
        self.flags = 0
        self.pattern = None
        self.root_dir = "./"
        self.database_filters = DatabaseFilters()

    def build(self):

        return internal__match(
            case=self.case,
            pattern=self.pattern,
            flags=self.flags,
            field=self.field,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            **self.database_filters.__dict__,
        )
