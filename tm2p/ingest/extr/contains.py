"""
ContainsExtractor
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.extr import ContainsExtractor
    >>> terms = (
    ...     ContainsExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching("tinyml")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(terms[:10])
    ['additional key words and phrasestinyml',
     'distributed tinyml',
     'hw  and sw co-optimizations for tinyml inference time acceleration',
     'mlops for tinyml',
     'multiple tinyml',
     'neurotransmitters tinyml',
     'non-static tinyml',
     'pose-estimation and tinyml',
     'real-time tiny machine learning ( tinyml ) application',
     'super-tinyml']


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.extr._helpers.contains import extract_contains


class ContainsExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_contains(self.params)
