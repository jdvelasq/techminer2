"""
StemmingAndExtractor
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.extr import StemmingAndExtractor
    >>> terms = (
    ...     StemmingAndExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching(
    ...         (
    ...             "tinyml",
    ...             "artificial intelligence",
    ...         ),
    ...     )
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
    ['ai ( artificial intelligence )',
     'artificial intelligence',
     'artificial intelligence ( ai )',
     'artificial intelligence of things',
     'artificial intelligence of things ( aiot )',
     'artificial intelligent',
     'distributed tinyml',
     'edge artificial intelligence',
     'edge artificial intelligence ( ai )',
     'edge artificial intelligence model and effective stress and sleep monitoring']



"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.extr._helpers.stemming import extract_stemming_and


class StemmingAndExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_stemming_and(self.params)


#
