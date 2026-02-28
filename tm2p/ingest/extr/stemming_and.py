"""
StemmingAndExtractor
===============================================================================

Smoke tests:
    >>> from tm2p import CorpusField
    >>> from tm2p.ingest.extract import StemmingAndExtractor
    >>> terms = (
    ...     StemmingAndExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching(
    ...         (
    ...             "financial technology",
    ...             "artificial intelligence",
    ...         ),
    ...     )
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )


    >>> # Print the first 10 extracted terms
    >>> from pprint import pprint
    >>> pprint(terms[:10])


"""

from tm2p._internals import ParamsMixin
from tm2p.ingest.extr._helpers.stemming import extract_stemming_and


class StemmingAndExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_stemming_and(self.params)


#
