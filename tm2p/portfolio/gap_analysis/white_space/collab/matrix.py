"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.gap_analysis.white_space.collab import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    ...     .where_root_directory("tests/tinyml-scopus/")
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
    COLUMNS                         Luca Benini 0041:000706  Michele Magno 0035:000501  Ivanovitch Silva 0027:000442  Danilo Pau 0021:000125  Marianne Silva 0020:000255  Marco Zennaro 0018:000115  Daniel G. Costa 0016:000312  Khalid El Makkaoui 0016:000178  Manuel Roveri 0016:000160  Danilo Pietro Pau 0016:000064
    ROWS                                                                                                                                                                                                                                                                                                                  
    Luca Benini 0041:000706                             0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000
    Michele Magno 0035:000501                           0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000
    Ivanovitch Silva 0027:000442                        0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000
    Danilo Pau 0021:000125                              0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.636
    Marianne Silva 0020:000255                          0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000
    Marco Zennaro 0018:000115                           0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000
    Daniel G. Costa 0016:000312                         0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000
    Khalid El Makkaoui 0016:000178                      0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000
    Manuel Roveri 0016:000160                           0.0                        0.0                           0.0                   0.000                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000
    Danilo Pietro Pau 0016:000064                       0.0                        0.0                           0.0                   0.636                         0.0                        0.0                          0.0                             0.0                        0.0                          0.000

    

"""

import numpy as np  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix
from tm2p.enum import GapComputation  # type: ignore
from tm2p.portfolio.social_struct.collab.direct import DirectMatrix
from tm2p.portfolio.social_struct.collab.latent import LatentMatrix


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
