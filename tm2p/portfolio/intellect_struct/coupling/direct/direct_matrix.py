"""
DirectMatrix
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.coupling.direct import DirectMatrix  # type: ignore
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
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
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                         Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300  Liu JK, 2020, ENV SCI POLLUT RES 1:00207  Ding ZK, 2016, WASTE MANAG 1:00201  Ding ZK, 2018, J CLEAN PROD 1:00178  Wang JY/1, 2015, J CLEAN PROD 1:00143  Wu YZ, 2011, CITIES 1:00130
    ROWS                                                                                                                                                                                                                                                                                 
    Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300                                             0.0                                       0.0                                 5.0                                  2.0                                    3.0                          0.0
    Liu JK, 2020, ENV SCI POLLUT RES 1:00207                                                   0.0                                       0.0                                 3.0                                  2.0                                    1.0                          0.0
    Ding ZK, 2016, WASTE MANAG 1:00201                                                         5.0                                       3.0                                 0.0                                  9.0                                   10.0                          0.0
    Ding ZK, 2018, J CLEAN PROD 1:00178                                                        2.0                                       2.0                                 9.0                                  0.0                                    9.0                          0.0
    Wang JY/1, 2015, J CLEAN PROD 1:00143                                                      3.0                                       1.0                                10.0                                  9.0                                    0.0                          1.0
    Wu YZ, 2011, CITIES 1:00130                                                                0.0                                       0.0                                 0.0                                  0.0                                    1.0                          0.0


* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     DirectMatrix()
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
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
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
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                         Tae Ho Woo 004:00007  Yahia Zare Mehrjerdi 003:00008  T. H. Woo 003:00005
    ROWS                                                                                                     
    Tae Ho Woo 004:00007                           0.000                           0.250                0.333
    Yahia Zare Mehrjerdi 003:00008                 0.250                           0.000                0.111
    T. H. Woo 003:00005                            0.333                           0.111                0.000





"""

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix

from .count_matrix import CountMatrix


class DirectMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = CountMatrix().update(**self.params.__dict__).run()
        direct_matrix = normalize_matrix(
            association_index=self.params.association_index,
            matrix=matrix,
            params=self.params,
        )

        direct_matrix.columns.name = "COLUMNS"
        direct_matrix.index.name = "ROWS"

        return direct_matrix
