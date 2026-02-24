"""
StemmingOrExtractor
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.extract import StemmingOrExtractor
    >>> terms = (
    ...     StemmingOrExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching(
    ...         [
    ...             "financial technology",
    ...             "artificial intelligence",
    ...         ],
    ...     )
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )


    >>> from pprint import pprint
    >>> pprint(terms[:10]) # doctest: +SKIP




"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.stemming import extract_stemming_or


class StemmingOrExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_stemming_or(self.params)


#
