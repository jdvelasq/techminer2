# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Full Match
===============================================================================

>>> from techminer2.database.field_extractors import FullMatchExtractor
>>> terms = (
...     FullMatchExtractor() 
...     .for_field(
...         with_name="author_keywords", 
...         with_terms_having_pattern="L.+",
...         with_case_sensitive=False,
...         with_regex_flags=0,
...     ).for_data(
...         in_root_dir="example/",
...         where_database="main",
...         where_record_years_between=(None, None),
...         where_record_citations_between=(None, None),
...     ).build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['LENDING', 'LENDINGCLUB', 'LITERATURE_REVIEW']

"""
from ...internals.set_params_mixin.in_root_dir_mixin import SetRootDirMixin
from ...internals.set_params_mixin.set_case_mixin import SetCaseMixin
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ...internals.set_params_mixin.set_field_mixin import SetFieldMixin
from ...internals.set_params_mixin.set_flags_mixin import SetFlagsMixin
from ...internals.set_params_mixin.with_pattern_mixin import SetPatternMixin
from ..internals.field_extractors.internal__full_match import internal__full_match


class FullMatchExtractor(
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

        return internal__full_match(
            case=self.case,
            pattern=self.pattern,
            flags=self.flags,
            field=self.field,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            **self.database_filters.__dict__,
        )
