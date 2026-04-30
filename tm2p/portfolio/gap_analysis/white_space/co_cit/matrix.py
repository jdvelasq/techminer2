"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.gap_analysis.white_space.co_cit import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # WHITESPACE ANALYSIS:
    ...     .using_wh_gap_computation(GapComputation.LATENT_MINUS_OBSERVED)
    ...     .using_wh_minimum_latent_similarity(0.4)
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
    
    COLUMNS                                               Forrester JayWright., 2013, Industrial dynamics 74:0  Sterman J.D., 2000, BUSINESS DYNAMICS 70:0  Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0  Barlas Y, 1996, SYST DYNAM REV 27:0  FORRESTER JW, 1958, HARVARD BUS REV 25:0
    ROWS                                                                                                                                                                                                                                                                                      
    Forrester JayWright., 2013, Industrial dynamics 74:0                                                   0.0                                         0.0                                                  0.0                                  0.0                                       0.0
    Sterman J.D., 2000, BUSINESS DYNAMICS 70:0                                                             0.0                                         0.0                                                  0.0                                  0.0                                       0.0
    Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0                                                    0.0                                         0.0                                                  0.0                                  0.0                                       0.0
    Barlas Y, 1996, SYST DYNAM REV 27:0                                                                    0.0                                         0.0                                                  0.0                                  0.0                                       0.0
    FORRESTER JW, 1958, HARVARD BUS REV 25:0                                                               0.0                                         0.0                                                  0.0                                  0.0                                       0.0

    

"""

import numpy as np  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix
from tm2p.enum import GapComputation  # type: ignore
from tm2p.portfolio.intellect_struct.co_cit_netw.direct import DirectMatrix
from tm2p.portfolio.intellect_struct.co_cit_netw.latent import LatentMatrix


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
                f"Unknown gap computation method: {self.params.wh_gap_computation}"
            )

        white_space = white_space.where(mask, 0)
        white_space.values[np.diag_indices_from(white_space)] = 0.0

        return white_space
