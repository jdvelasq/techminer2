"""
LatentMatrix
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.coupling.latent import LatentMatrix  # type: ignore
    >>> df = (
    ...     LatentMatrix()
    ...     #
    ...     # COUPLING UNIT:
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
    Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300                                           1.000                                     0.568                               0.710                                0.731                                  0.715                        0.251
    Liu JK, 2020, ENV SCI POLLUT RES 1:00207                                                 0.568                                     1.000                               0.529                                0.549                                  0.475                        0.152
    Ding ZK, 2016, WASTE MANAG 1:00201                                                       0.710                                     0.529                               1.000                                0.750                                  0.653                        0.356
    Ding ZK, 2018, J CLEAN PROD 1:00178                                                      0.731                                     0.549                               0.750                                1.000                                  0.644                        0.355
    Wang JY/1, 2015, J CLEAN PROD 1:00143                                                    0.715                                     0.475                               0.653                                0.644                                  1.000                        0.200
    Wu YZ, 2011, CITIES 1:00130                                                              0.251                                     0.152                               0.356                                0.355                                  0.200                        1.000


* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     LatentMatrix()
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
    Tae Ho Woo 004:00007                           1.000                           0.325                0.190
    Yahia Zare Mehrjerdi 003:00008                 0.325                           1.000                0.867
    T. H. Woo 003:00005                            0.190                           0.867                1.000




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
