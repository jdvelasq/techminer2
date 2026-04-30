"""
CountMatrix
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.coupling.direct import CountMatrix  # type: ignore
    >>> df = (
    ...     CountMatrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                    Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300  Liu JK, 2020, ENV SCI POLLUT RES 1:00207  Ding ZK, 2016, WASTE MANAG 1:00201  Ding ZK, 2018, J CLEAN PROD 1:00178  Wang JY/1, 2015, J CLEAN PROD 1:00143  Wu YZ, 2011, CITIES 1:00130
    Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300                                               1                                         0                                   5                                    2                                      3                            0
    Liu JK, 2020, ENV SCI POLLUT RES 1:00207                                                     0                                         1                                   3                                    2                                      1                            0
    Ding ZK, 2016, WASTE MANAG 1:00201                                                           5                                         3                                   1                                    9                                     10                            0
    Ding ZK, 2018, J CLEAN PROD 1:00178                                                          2                                         2                                   9                                    1                                      9                            0
    Wang JY/1, 2015, J CLEAN PROD 1:00143                                                        3                                         1                                  10                                    9                                      1                            1
    Wu YZ, 2011, CITIES 1:00130                                                                  0                                         0                                   0                                    0                                      1                            1

    
* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     CountMatrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                                    Tae Ho Woo 004:00007  Yahia Zare Mehrjerdi 003:00008  T. H. Woo 003:00005
    Tae Ho Woo 004:00007                               4                               3                    4
    Yahia Zare Mehrjerdi 003:00008                     3                               3                    1
    T. H. Woo 003:00005                                4                               1                    3



"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .count_matrix_list import CountMatrixList


class CountMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix_list = CountMatrixList().update(**self.params.__dict__).run()

        nodes = list(
            set(matrix_list["ROWS"].to_list()).union(
                set(matrix_list["COLUMNS"].to_list())
            )
        )

        def f(x):
            counters = x.split(" ")[-1]
            occ = counters.split(":")[0]
            gcs = counters.split(":")[1]
            return int(occ), int(gcs), x

        sorted_nodes = sorted(nodes, key=f, reverse=True)

        df = pd.DataFrame(0, index=sorted_nodes, columns=sorted_nodes)

        for _, row in matrix_list.iterrows():
            citing_unit = row["ROWS"]
            cited_unit = row["COLUMNS"]
            occ = row["OCC"]
            df.loc[citing_unit, cited_unit] = occ
            df.loc[cited_unit, citing_unit] = occ

        for col in df.columns:
            counters = col.split(" ")[-1]
            occ = counters.split(":")[0]
            df.loc[col, col] = int(occ)

        return df
