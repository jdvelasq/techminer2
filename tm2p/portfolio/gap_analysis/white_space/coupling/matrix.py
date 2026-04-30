"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.gap_analysis.white_space.coupling import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # WHITESPACE ANALYSIS:
    ...     .using_wh_gap_computation(GapComputation.LATENT_MINUS_OBSERVED)
    ...     .using_wh_minimum_latent_similarity(0.6)
    ...     .using_wh_maximum_observed_similarity(0.1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
    COLUMNS                                         Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300  Liu JK, 2020, ENV SCI POLLUT RES 1:00207  Ding ZK, 2016, WASTE MANAG 1:00201  Ding ZK, 2018, J CLEAN PROD 1:00178  Wang JY/1, 2015, J CLEAN PROD 1:00143  Wu YZ, 2011, CITIES 1:00130  Orji IJ, 2015, COMPUT IND ENG 1:00125  Yuan HP/1, 2012, WASTE MANAG 1:00109  Wei SK, 2012, EUR J OPER RES 1:00105  He L, 2022, WASTE MANAG 1:00091
    ROWS                                                                                                                                                                                                                                                                                                                                                                                                                                     
    Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300                                             0.0                                       0.0                               0.000                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    Liu JK, 2020, ENV SCI POLLUT RES 1:00207                                                   0.0                                       0.0                               0.000                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    Ding ZK, 2016, WASTE MANAG 1:00201                                                         0.0                                       0.0                               0.000                                1.938                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    Ding ZK, 2018, J CLEAN PROD 1:00178                                                        0.0                                       0.0                               1.938                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    Wang JY/1, 2015, J CLEAN PROD 1:00143                                                      0.0                                       0.0                               0.000                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    Wu YZ, 2011, CITIES 1:00130                                                                0.0                                       0.0                               0.000                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    Orji IJ, 2015, COMPUT IND ENG 1:00125                                                      0.0                                       0.0                               0.000                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    Yuan HP/1, 2012, WASTE MANAG 1:00109                                                       0.0                                       0.0                               0.000                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    Wei SK, 2012, EUR J OPER RES 1:00105                                                       0.0                                       0.0                               0.000                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0
    He L, 2022, WASTE MANAG 1:00091                                                            0.0                                       0.0                               0.000                                0.000                                    0.0                          0.0                                    0.0                                   0.0                                   0.0                              0.0


"""

import numpy as np  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix
from tm2p.enum import GapComputation  # type: ignore
from tm2p.portfolio.intellect_struct.coupling.direct import DirectMatrix
from tm2p.portfolio.intellect_struct.coupling.latent import LatentMatrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        observed = DirectMatrix().update(**self.params.__dict__).run()
        latent = LatentMatrix().update(**self.params.__dict__).run()

        mask = (latent >= self.params.wh_minimum_latent_similarity) & (
            observed <= self.params.wh_maximum_observed_similarity
        )

        if self.params.wh_gap_computation == GapComputation.LATENT_MINUS_OBSERVED:
            white_space = latent.sub(observed).clip(lower=0.0)
        elif self.params.wh_gap_computation == GapComputation.RELATIVE_LATENT_GAP:
            white_space = latent.sub(observed).div(latent + 1e-12).clip(lower=0.0)
        elif self.params.wh_gap_computation == GapComputation.STRUCTURAL_HOLE_SOFT:
            white_space = latent.mul(1.0 - observed)
        else:
            raise ValueError(
                f"Unknown white space computation method: {self.params.wh_gap_computation}"
            )

        white_space = white_space.where(mask, 0)
        white_space.values[np.diag_indices_from(white_space)] = 0.0

        return white_space
