"""
YearToItems
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.performance_metrics.trends import YearToItems
    >>> mapping = (
    ...     YearToItems()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
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
    {2015: ['debit cards',
            'electronic commerce',
            'financial service',
            'internet banking',
            'research and application',
            'virtual addresses',
    ...


    >>> mapping = (
    ...     YearToItems()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
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
    {2015: ['debit cards 001:00018',
            'electronic commerce 001:00018',
            'financial service 001:00018',
            'internet banking 001:00018',
    ...

"""

from tm2p._intern import Params, ParamsMixin, SortAxesMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field, UnitOrderBy

from ..unit import Metrics

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
