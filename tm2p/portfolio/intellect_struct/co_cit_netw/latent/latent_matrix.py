"""
LatentMatrix
===============================================================================

* **CITED_REF** / **CITED_AUTH** / **CITED_SRC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw.latent import LatentMatrix  # type: ignore
    >>> df = (
    ...     LatentMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                               Forrester JayWright., 2013, Industrial dynamics 74:0  Sterman J.D., 2000, BUSINESS DYNAMICS 70:0  Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0  Barlas Y, 1996, SYST DYNAM REV 27:0  FORRESTER JW, 1958, HARVARD BUS REV 25:0  Swanson J, 2002, J OPER RES SOC 21:0
    ROWS                                                                                                                                                                                                                                                                                                                            
    Forrester JayWright., 2013, Industrial dynamics 74:0                                                 1.000                                       0.665                                                0.470                                0.636                                     0.637                                 0.382
    Sterman J.D., 2000, BUSINESS DYNAMICS 70:0                                                           0.665                                       1.000                                                0.296                                0.545                                     0.578                                 0.537
    Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0                                                  0.470                                       0.296                                                1.000                                0.585                                     0.229                                 0.249
    Barlas Y, 1996, SYST DYNAM REV 27:0                                                                  0.636                                       0.545                                                0.585                                1.000                                     0.359                                 0.387
    FORRESTER JW, 1958, HARVARD BUS REV 25:0                                                             0.637                                       0.578                                                0.229                                0.359                                     1.000                                 0.327
    Swanson J, 2002, J OPER RES SOC 21:0                                                                 0.382                                       0.537                                                0.249                                0.387                                     0.327                                 1.000


    >>> df = (
    ...     LatentMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.JACCARD)
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
    >>> print(df.iloc[:10, :10].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE

    COLUMNS                                          Forrester JayWright., 2013, Industrial dynamics  Sterman J.D., 2000, BUSINESS DYNAMICS  Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY  Barlas Y, 1996, SYST DYNAM REV  FORRESTER JW, 1958, HARVARD BUS REV  Swanson J, 2002, J OPER RES SOC
    ROWS                                                                                                                                                                                                                                                                                         
    Forrester JayWright., 2013, Industrial dynamics                                            1.000                                  0.665                                           0.470                           0.636                                0.637                            0.382
    Sterman J.D., 2000, BUSINESS DYNAMICS                                                      0.665                                  1.000                                           0.296                           0.545                                0.578                            0.537
    Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY                                             0.470                                  0.296                                           1.000                           0.585                                0.229                            0.249
    Barlas Y, 1996, SYST DYNAM REV                                                             0.636                                  0.545                                           0.585                           1.000                                0.359                            0.387
    FORRESTER JW, 1958, HARVARD BUS REV                                                        0.637                                  0.578                                           0.229                           0.359                                1.000                            0.327
    Swanson J, 2002, J OPER RES SOC                                                            0.382                                  0.537                                           0.249                           0.387                                0.327                            1.000

    
"""

import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix

from ..direct.direct_matrix import DirectMatrix


class LatentMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = DirectMatrix().update(**self.params.__dict__).run()
        df = _compute_cosine_similarity(df)

        return df


def _compute_cosine_similarity(matrix):
    """Computes cosine similarity between rows of a matrix."""

    similarity = cosine_similarity(matrix)

    df = pd.DataFrame(
        similarity,
        columns=matrix.columns,
        index=matrix.index,
    )

    return df
