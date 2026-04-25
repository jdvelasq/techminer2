"""
MatchExtractor
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.extr import MatchExtractor
    >>> terms = (
    ...     MatchExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching("b.+")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
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
    ['back-propagation-free training',
     'backdoors',
     'bagging',
     'ballistocardiography',
     'banana disease detection',
     'bandwidth optimization',
     'bangla font style',
     'batchensemble',
     'batching',
     'batteries']


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.extr._helpers.match import extract_match


class MatchExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_match(self.params)


#
