"""
EndsWithExtractor
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.extract import EndsWithExtractor
    >>> terms = (
    ...     EndsWithExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching("ing")
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
    ['alternative lending',
     'banking',
     'crowdfunding',
     'innovative banking',
     'retail banking']

"""

from tm2p._internals import ParamsMixin
from tm2p.ingest.extract._helpers.endswith import extract_endswith


class EndsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_endswith(self.params)


#
