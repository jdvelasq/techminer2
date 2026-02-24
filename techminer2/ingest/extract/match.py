"""
MatchExtractor
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.extract import MatchExtractor
    >>> terms = (
    ...     MatchExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching("b.+")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(terms[:10])
    ['bank',
     'bank 30',
     'banking',
     'banking innovations',
     'banking regulation',
     'bayesian estimation',
     'biometric',
     'biometric authentication',
     'blockchain']

"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.match import extract_match


class MatchExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_match(self.params)


#
