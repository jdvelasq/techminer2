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
    >>> # Creates, configures, and runs the extractor
    >>> from techminer2.database.extractors import MatchExtractor
    >>> terms = (
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
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )


    >>> # Print the first 10 extracted terms
    >>> from pprint import pprint
    >>> pprint(terms[:10])
    ['LENDING', 'LENDINGCLUB', 'LITERATURE_REVIEW']

"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.text.extract._helpers.match import internal__match


class MatchExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__match(self.params)


#
