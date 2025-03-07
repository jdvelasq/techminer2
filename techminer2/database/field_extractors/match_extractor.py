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

Example:
    >>> from pprint import pprint
    >>> from techminer2.database.field_extractors import MatchExtractor

    >>> # Creates, configures, and runs the extractor
    >>> extractor = (
    ...     MatchExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords")
    ...     #
    ...     # SEARCH:
    ...     .having_pattern("L.+")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> terms = extractor.run()

    >>> # Print the first 10 extracted terms
    >>> pprint(terms[:10])
    ['LENDING', 'LENDINGCLUB', 'LITERATURE_REVIEW']

"""

from ..._internals.mixins import ParamsMixin
from ._internals.match import internal__match


class MatchExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__match(self.params)
