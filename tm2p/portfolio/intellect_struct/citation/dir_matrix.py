"""
DirectMatrix
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.cit_netw import DirectMatrix  # type: ignore
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
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
    >>> assert df.shape[0] > 0
    >>> assert df.shape[1] > 0
    >>> df.iloc[0:10, 0:10].round(3)  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                         Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300  ...  Khan S, 2009, ENV MODEL SOFTW 1:00084
    ROWS                                                                                            ...
    Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300                                             0.0  ...                                    0.0
    Liu JK, 2020, ENV SCI POLLUT RES 1:00207                                                   1.0  ...                                    0.0
    Ding ZK, 2016, WASTE MANAG 1:00201                                                         1.0  ...                                    0.0
    Ding ZK, 2018, J CLEAN PROD 1:00178                                                        0.0  ...                                    0.0
    Wang JY/1, 2015, J CLEAN PROD 1:00143                                                      0.0  ...                                    0.0
    Orji IJ, 2015, COMPUT IND ENG 1:00125                                                      0.0  ...                                    0.0
    Yuan HP/1, 2012, WASTE MANAG 1:00109                                                       1.0  ...                                    0.0
    Wei SK, 2012, EUR J OPER RES 1:00105                                                       0.0  ...                                    0.0
    He L, 2022, WASTE MANAG 1:00091                                                            0.0  ...                                    0.0
    Khan S, 2009, ENV MODEL SOFTW 1:00084                                                      0.0  ...                                    0.0
    <BLANKLINE>
    [10 rows x 10 columns]



* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

    >>> from tm2p.portfolio.intellect_struct.cit_netw import DirectMatrix  # type: ignore
    >>> # ---------------------------------------------------------------------
    >>> # OTHER
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(1)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
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
    >>> assert df.shape[0] > 0
    >>> assert df.shape[1] > 0
    >>> df.iloc[0:10, 0:10].round(3)  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                              Hamed Nozari 006:00045  ...  Lihong Li 003:00019
    ROWS                                                         ...
    Hamed Nozari 006:00045                                  0.0  ...                  0.0
    Vivian W. Y. Tam 004:00532                              0.0  ...                  0.0
    Lulu Zhang 004:00064                                    0.0  ...                  0.0
    Mohamed Marzouk 003:00323                               0.0  ...                  0.0
    Jingkuang Liu 003:00284                                 0.0  ...                  0.0
    Wenya Yu 003:00056                                      0.0  ...                  0.0
    Meina Li 003:00049                                      0.0  ...                  0.0
    Javier Ibanez 003:00023                                 0.0  ...                  0.0
    Jaime Martinez-Valderrama 003:00023                     0.0  ...                  0.0
    Lihong Li 003:00019                                     0.0  ...                  0.0
    <BLANKLINE>
    [10 rows x 10 columns]



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix

from .matrix import Matrix


class DirectMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).run()

        matrix = normalize_matrix(
            association_index=self.params.association_index,
            matrix=matrix,
            params=self.params,
        )

        matrix.columns.name = "COLUMNS"
        matrix.index.name = "ROWS"

        return matrix
