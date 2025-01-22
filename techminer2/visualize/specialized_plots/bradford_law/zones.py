# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Zones
===============================================================================

# >>> from techminer2.visualize.specialized_plots.bradford_law import zones
# >>> zones(
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(None, None),
# ...     cited_by_filter=(None, None),
# ... ).head()
                     no  OCC  cum_OCC  global_citations  zone
abbr_source_title                                            
J. Econ. Bus.         1    3        3               422     1
J Manage Inf Syst     2    2        5               696     1
Rev. Financ. Stud.    3    2        7               432     1
Ind Manage Data Sys   4    2        9               386     1
Electron. Mark.       5    2       11               287     1

"""
from ....database.load.load__filtered_database import load__filtered_database


def zones(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    records = load__filtered_database(
        root_dir=root_dir,
        database=database,
        record_years_range=year_filter,
        record_citations_range=cited_by_filter,
        records_order_by=None,
        **filters,
    )

    indicators = records[["abbr_source_title", "global_citations"]]
    indicators = indicators.assign(OCC=1)
    indicators = indicators.groupby(["abbr_source_title"], as_index=False).sum()
    indicators = indicators.sort_values(by=["OCC", "global_citations"], ascending=False)
    indicators = indicators.assign(cum_OCC=indicators["OCC"].cumsum())
    indicators = indicators.assign(no=1)
    indicators = indicators.assign(no=indicators.no.cumsum())

    cum_occ = indicators["OCC"].sum()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.assign(zone=3)
    indicators.zone = indicators.zone.where(
        indicators.cum_OCC >= int(cum_occ * 2 / 3), 2
    )
    indicators.zone = indicators.zone.where(indicators.cum_OCC >= int(cum_occ / 3), 1)
    indicators = indicators.set_index("abbr_source_title")
    indicators = indicators[["no", "OCC", "cum_OCC", "global_citations", "zone"]]

    return indicators
