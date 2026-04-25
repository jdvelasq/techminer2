"""
EndsWithExtractor
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.extr import EndsWithExtractor
    >>> terms = (
    ...     EndsWithExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching("ing")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert len(terms) > 0
    >>> from pprint import pprint
    >>> pprint(terms[:10])
    ['3d-modeling',
     'acoustic emission monitoring',
     'acoustic monitoring',
     'active learning',
     'activity tracking',
     'adaptive machine learning',
     'adaptive modeling',
     'adversarial machine learning',
     'affective computing',
     'agroengineering']

"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.extr._helpers.endswith import extract_endswith


class EndsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_endswith(self.params)


#
