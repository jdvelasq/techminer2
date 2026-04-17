"""
YearToItems
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.performance_metrics.trends import YearToItems
    >>> mapping = (
    ...     YearToItems()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(mapping).__name__
    'dict'
    >>> len(mapping) > 0
    True
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {2015: ['biometric',
            'fast identity online',
            'fido',
            'password',
            'pki',
            'single sign-on'],
     2016: ['fintech',
            'innovation',
            'technology',
            'content analysis',
            'digitalization',
            'popular press',
    ...

    >>> mapping = (
    ...     YearToItems()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(mapping).__name__
    'dict'
    >>> len(mapping) > 0
    True
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {2015: ['biometric 001:00001',
            'fast identity online 001:00001',
            'fido 001:00001',
            'password 001:00001',
            'pki 001:00001',
            'single sign-on 001:00001'],
     2016: ['fintech 011:01029',
            'innovation 003:00685',
            'technology 002:00650',
            'content analysis 002:00283',
            'digitalization 002:00283',
            'popular press 002:00283',
            'banking 001:00402',
    ...

"""

from tm2p._intern import Params, ParamsMixin, SortAxesMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field, UnitOrderBy

from ..item_metrics import Metrics

GCS = Field.GCS.value
OCC = UnitOrderBy.OCC.value
YEAR = Field.YEAR.value

COUNTERS = "COUNTERS"


class YearToItems(
    ParamsMixin,
    SortAxesMixin,
):
    """:meta private:"""

    def run(self) -> dict[int, list[str]]:
        """:meta private:"""

        mapping = {}

        use_counters = self.params.use_counters

        years = _get_years(params=self.params)
        for year in years:
            item_metrics = (
                Metrics()
                .update(**self.params.__dict__)
                .using_counters(True)
                .where_record_years_range(year, year)
                .run()
            )
            mapping[year] = item_metrics[COUNTERS].tolist()

        if use_counters is False:
            mapping = {
                year: [" ".join(item.split(" ")[:-1]) for item in items]
                for year, items in mapping.items()
            }

        return mapping


def _get_years(params: Params):
    df = load_filtered_main_csv_zip(params=params)
    min_year, max_year = df[YEAR].min(), df[YEAR].max()
    return list(range(min_year, max_year + 1))
