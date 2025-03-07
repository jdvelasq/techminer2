# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Fields Intersection
===============================================================================

Example:
    >>> from pprint import pprint
    >>> from techminer2.database.field_extractors import FieldsIntersectionExtractor

    >>> # Creates, configures, and runs the extractor
    >>> extractor = (
    ...     FieldsIntersectionExtractor()
    ...     #
    ...     # FIELDS:
    ...     .with_field("raw_author_keywords")
    ...     .with_other_field("raw_index_keywords")
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
    ['ACTOR_NETWORK_THEORY',
     'ACTUALIZATION',
     'AGRICULTURE',
     'AGROPAY',
     'ARTIFICIAL_INTELLIGENCE',
     'BANKING',
     'BIG_DATA',
     'BLOCKCHAIN',
     'BUSINESS_MODELS',
     'CASE_STUDY_METHODS']


"""

from ..._internals.mixins import ParamsMixin
from ._internals.fields_intersection import internal__fields_intersection


class FieldsIntersectionExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__fields_intersection(self.params)
