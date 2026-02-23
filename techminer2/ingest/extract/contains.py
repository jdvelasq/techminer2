"""
Contains
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.extract import ContainsExtractor
    >>> terms = (
    ...     ContainsExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching("FINTECH")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
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
    ['fintech',
     'fintech industry',
     'investment in fintech',
     'taiwan fintech industry']


"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.contains import extract_contains


class ContainsExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_contains(self.params)
