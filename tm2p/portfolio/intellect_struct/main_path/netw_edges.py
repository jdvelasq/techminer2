"""
NetworkEdges
===============================================================================

Smoke tests:
    >>> from tm2p.portfolio.intellect_struct.main_path import NetworkEdges
    >>> df = (
    ...     NetworkEdges()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .having_top_n_units(None)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())
                                           CITING_DOC                                       CITED_DOC  POINTS
    0  Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300            Yuan HP/1, 2012, WASTE MANAG 1:00109      37
    1              Ding ZK, 2016, WASTE MANAG 1:00201  Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300      20
    2             Ding ZK, 2018, J CLEAN PROD 1:00178              Ding ZK, 2016, WASTE MANAG 1:00201      16
    3       Liu JK, 2020, ENV SCI POLLUT RESa 1:00056             Ding ZK, 2018, J CLEAN PROD 1:00178       6
    4       Liu JK, 2020, ENV SCI POLLUT RESa 1:00056  Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300       2




"""

from tm2p._intern import ParamsMixin
from tm2p.portfolio.intellect_struct.main_path._intern.comp_main_path import (
    compute_main_path,
)


class NetworkEdges(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        #
        # Creates a table with citing and cited articles
        _, data_frame = compute_main_path(params=self.params)
        return data_frame
