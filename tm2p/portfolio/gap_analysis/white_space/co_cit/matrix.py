"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.gap_analysis.white_space.co_occur import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
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
    ...     .using_wh_minimum_latent_similarity(0.8)
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
    >>> print(df.iloc[:5, :5].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                            tinyml 1031:010091  machine learning 0766:008244  tiny machine learning 0388:003654  internet of things 0346:005415  learning systems 0343:003524
    ROWS                                                                                                                                                                                
    tinyml 1031:010091                                0.0                           0.0                                0.0                             0.0                           0.0
    machine learning 0766:008244                      0.0                           0.0                                0.0                             0.0                           0.0
    tiny machine learning 0388:003654                 0.0                           0.0                                0.0                             0.0                           0.0
    internet of things 0346:005415                    0.0                           0.0                                0.0                             0.0                           0.0
    learning systems 0343:003524                      0.0                           0.0                                0.0                             0.0                           0.0

    

"""

import numpy as np  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix
from tm2p.enum import GapComputation  # type: ignore
from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import DirectMatrix
from tm2p.portfolio.thematic_struct.co_occur.latent_simil_netw import LatentMatrix


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
            gap = latent.sub(observed).clip(lower=0.0)
        elif self.params.wh_gap_computation == GapComputation.RELATIVE_LATENT_GAP:
            white_space = latent.sub(observed).div(latent + 1e-12).clip(lower=0.0)
        elif self.params.wh_gap_computation == GapComputation.STRUCTURAL_HOLE_SOFT:
            white_space = latent.mul(1.0 - observed)
        else:
            raise ValueError(
                f"Unknown gap computation method: {self.params.wh_gap_computation}"
            )

        white_space = gap.where(mask, 0)
        white_space.values[np.diag_indices_from(white_space)] = 0.0

        return white_space
