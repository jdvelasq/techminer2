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
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     #
...     # SEARCH:
...     .having_terms_like("L.+")
...     .having_case_sensitive(False)
...     .having_regex_flags(0)
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
['LENDING', 'LENDINGCLUB', 'LITERATURE_REVIEW']

"""

from ..._internals.mixins import ParamsMixin
from ._internals.match import internal__match


class MatchExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__match(self.params)
