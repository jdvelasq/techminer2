"""
StartsWithExtractor
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.extr import StartsWithExtractor
    >>> terms = (
    ...     StartsWithExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching("ml")
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
    >>> pprint(terms[:10])  # doctest: +SKIP
    ['ml',
     'ml accelerator',
     'ml classification',
     'ml in arduino',
     'ml security',
     'ml system',
     'ml systems',
     'mlops',
     'mlops for tinyml',
     'mlperf tiny benchmark']


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.extr._helpers.startswith import extract_startswith


class StartsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_startswith(self.params)


#
