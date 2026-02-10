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
    >>> # Creates, configures, and runs the extractor
    >>> from techminer2.database.extractors import IntersectionExtractor
    >>> terms = (
    ...     IntersectionExtractor()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords_raw")
    ...     .with_other_field("index_keywords_raw")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )

    >>> # Print the first 10 extracted terms
    >>> from pprint import pprint
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
from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.intersection import internal__intersection


class IntersectionExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return internal__intersection(self.params)


#

#
#
