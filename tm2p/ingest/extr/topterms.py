"""
TopTermsExtractor
===============================================================================

Smoke tests:
    >>> from tm2p import CorpusField
    >>> from tm2p.ingest.extract import TopTermsExtractor
    >>> terms = (
    ...     TopTermsExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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


"""

from tm2p._intern import ParamsMixin
from tm2p.anal._intern.performance import PerformanceMetrics


class TopTermsExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = PerformanceMetrics().update(**self.params.__dict__).run()
        terms = data_frame.index.tolist()
        terms = sorted(terms)

        return terms
