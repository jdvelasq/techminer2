"""
TopItemsExtractor
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, UnitOrderBy
    >>> from tm2p.ingest.extr import TopItemsExtractor
    >>> items = (
    ...     TopItemsExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(items[:10])
    ['artificial intelligence',
     'banking',
     'blockchain',
     'china',
     'financial inclusion',
     'financial services',
     'financial technology',
     'fintech',
     'green finance',
     'innovation']


"""

from tm2p._intern import ParamsMixin
from tm2p.portf.perf_metric.unit.metrics import Metrics


class TopItemsExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = Metrics().update(**self.params.__dict__).run()
        terms = data_frame.index.tolist()
        terms = sorted(terms)

        return terms
