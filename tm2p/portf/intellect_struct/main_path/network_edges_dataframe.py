"""
Network Edges Frame
===============================================================================

Smoke tests:
    >>> from tm2p.synthesize.main_path import NetworkEdgesDataFrame
    >>> df = (
    ...     NetworkEdgesDataFrame()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .having_top_n_units(None)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())
                                                                                  CITING_DOC                                                                               CITED_DOC  POINTS
    0  Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7, DOI 10.1007/s40804-020-00183-y 1:00338  Arner DW, 2019, EUR BUS ORGAN LAW RE, V20, P55, DOI 10.1007/s40804-019-00135-1 1:00045      37
    1  Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7, DOI 10.1007/s40804-020-00183-y 1:00338        Buckley RP, 2020, J BANK REGUL, V21, P26, DOI 10.1057/s41261-019-00104-1 1:00037      37
    2                   Nasir A, 2021, APPL SCI-BASEL, V11, DOI 10.3390/app112110353 1:00040   Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7, DOI 10.1007/s40804-020-00183-y 1:00338      30
    3                   Nasir A, 2021, APPL SCI-BASEL, V11, DOI 10.3390/app112110353 1:00040  Arner DW, 2019, EUR BUS ORGAN LAW RE, V20, P55, DOI 10.1007/s40804-019-00135-1 1:00045      15
    4                   Nasir A, 2021, APPL SCI-BASEL, V11, DOI 10.3390/app112110353 1:00040        Buckley RP, 2020, J BANK REGUL, V21, P26, DOI 10.1057/s41261-019-00104-1 1:00037      15

"""

from tm2p._intern import ParamsMixin
from tm2p.portf.intellect_struct.main_path._intern.compute_main_path import (
    compute_main_path,
)


class NetworkEdgesDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        #
        # Creates a table with citing and cited articles
        _, data_frame = compute_main_path(params=self.params)
        return data_frame
