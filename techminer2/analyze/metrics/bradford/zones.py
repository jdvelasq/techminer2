# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Zones
===============================================================================


Smoke tests:
    >>> from techminer2.analyze.metrics.bradford_law import ZonesDataFrame
    >>> (
    ...     ZonesDataFrame()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head() # doctest: +NORMALIZE_WHITESPACE
                         no  OCC  cum_OCC  global_citations  zone
    source_title_abbr
    J. Econ. Bus.         1    3        3               422     1
    J Manage Inf Syst     2    2        5               696     1
    Rev. Financ. Stud.    3    2        7               432     1
    Ind Manage Data Sys   4    2        9               386     1
    Electron. Mark.       5    2       11               287     1


"""
from techminer2._internals import ParamsMixin
from techminer2._internals.data_access import load_filtered_main_data


class ZonesDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_filtered_records(self):
        self.records = load_filtered_main_data(params=self.params)

    # -------------------------------------------------------------------------
    def internal__compute_citations_and_occurrences_by_source(self):

        indicators = self.records[["source_title_abbr", "global_citations"]]
        indicators = indicators.assign(OCC=1)
        indicators = indicators.groupby(["source_title_abbr"], as_index=False).sum()
        indicators = indicators.sort_values(
            by=["OCC", "global_citations"], ascending=False
        )
        indicators = indicators.assign(cum_OCC=indicators["OCC"].cumsum())
        indicators = indicators.assign(no=1)
        indicators = indicators.assign(no=indicators.no.cumsum())

        self.indicators = indicators

    # -------------------------------------------------------------------------
    def internal__compute_zones(self):

        indicators = self.indicators.copy()
        cum_occ = indicators["OCC"].sum()
        indicators = indicators.reset_index(drop=True)
        indicators = indicators.assign(zone=3)
        indicators.zone = indicators.zone.where(
            indicators.cum_OCC >= int(cum_occ * 2 / 3), 2
        )
        indicators.zone = indicators.zone.where(
            indicators.cum_OCC >= int(cum_occ / 3), 1
        )
        indicators = indicators.set_index("source_title_abbr")
        indicators = indicators[["no", "OCC", "cum_OCC", "global_citations", "zone"]]

        self.indicators = indicators

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__load_filtered_records()
        self.internal__compute_citations_and_occurrences_by_source()
        self.internal__compute_zones()

        return self.indicators


#

#
#
