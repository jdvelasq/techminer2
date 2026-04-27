"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.portfolio.intellect_struct.main_path import Matrix
    >>> df = (
    ...     Matrix()
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
    >>> print(df.iloc[:5, :5].to_string())
                                               Chen YL, 2025, BUILD 1:00001  Cheng BQ, 2022, ENV MANAG 1:00053  Ding ZK, 2016, WASTE MANAG 1:00201  Ding ZK, 2018, J CLEAN PROD 1:00178  Liu JK, 2020, ENV SCI POLLUT RESa 1:00056
    Chen YL, 2025, BUILD 1:00001                                          0                                 14                                   0                                    0                                          0
    Cheng BQ, 2022, ENV MANAG 1:00053                                    14                                  0                                   2                                    3                                          4
    Ding ZK, 2016, WASTE MANAG 1:00201                                    0                                  2                                   0                                   16                                          0
    Ding ZK, 2018, J CLEAN PROD 1:00178                                   0                                  3                                  16                                    0                                          6
    Liu JK, 2020, ENV SCI POLLUT RESa 1:00056                             0                                  4                                   0                                    6                                          0



"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .netw_edges import NetworkEdges


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        #
        # Creates a table with citing and cited articles
        edges = NetworkEdges().update(**self.params.__dict__).run()
        units = sorted(
            set(edges["CITING_DOC"].to_list() + edges["CITED_DOC"].to_list())
        )
        df = pd.DataFrame(
            0,
            index=units,
            columns=units,
        )
        for _, row in edges.iterrows():
            df.loc[row["CITING_DOC"], row["CITED_DOC"]] = row["POINTS"]
            df.loc[row["CITED_DOC"], row["CITING_DOC"]] = row["POINTS"]
        return df
