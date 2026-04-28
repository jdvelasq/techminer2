"""
LatentMatrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.co_occur.latent_simil_netw import LatentMatrix
    >>> df = (
    ...     LatentMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
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
    >>> print(df.round(3).head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                            fintech 119:26148  finance 029:07137  innovation 020:03916  china 018:03596  financial inclusion 017:03823  financial technology 016:02809  sustainable development 015:02158  banking 013:03043  sustainability 013:02308  blockchain 012:03450  green finance 011:02844  financial services 011:02399  covid-19 009:01743  economic growth 009:01654  artificial intelligence 008:01915  financial service 007:02627  technology 007:01409  crowdfunding 007:01245  commerce 006:02013  technology adoption 006:01500
    ROWS
    fintech 119:26148                              1.000              0.853                 0.824            0.696                          0.680                           0.696                              0.733              0.759                     0.708                 0.642                    0.640                         0.663               0.648                      0.580                              0.587                        0.528                 0.640                   0.481               0.582                          0.705
    finance 029:07137                              0.853              1.000                 0.740            0.630                          0.715                           0.660                              0.641              0.634                     0.725                 0.611                    0.523                         0.529               0.581                      0.608                              0.478                        0.443                 0.606                   0.544               0.525                          0.561
    innovation 020:03916                           0.824              0.740                 1.000            0.692                          0.593                           0.762                              0.767              0.623                     0.784                 0.428                    0.680                         0.540               0.699                      0.623                              0.534                        0.365                 0.616                   0.424               0.426                          0.693
    china 018:03596                                0.696              0.630                 0.692            1.000                          0.436                           0.640                              0.725              0.588                     0.769                 0.196                    0.805                         0.523               0.670                      0.687                              0.487                        0.243                 0.765                   0.337               0.338                          0.640
    financial inclusion 017:03823                  0.680              0.715                 0.593            0.436                          1.000                           0.289                              0.433              0.513                     0.341                 0.520                    0.296                         0.674               0.352                      0.324                              0.301                        0.385                 0.234                   0.434               0.440                          0.633
    financial technology 016:02809                 0.696              0.660                 0.762            0.640                          0.289                           1.000                              0.514              0.677                     0.733                 0.228                    0.604                         0.286               0.713                      0.609                              0.613                        0.361                 0.760                   0.339               0.357                          0.474
    sustainable development 015:02158              0.733              0.641                 0.767            0.725                          0.433                           0.514                              1.000              0.515                     0.627                 0.338                    0.820                         0.510               0.546                      0.643                              0.426                        0.279                 0.540                   0.375               0.381                          0.637
    banking 013:03043                              0.759              0.634                 0.623            0.588                          0.513                           0.677                              0.515              1.000                     0.555                 0.355                    0.473                         0.462               0.513                      0.437                              0.478                        0.403                 0.556                   0.219               0.340                          0.587
    sustainability 013:02308                       0.708              0.725                 0.784            0.769                          0.341                           0.733                              0.627              0.555                     1.000                 0.369                    0.749                         0.356               0.585                      0.611                              0.417                        0.284                 0.654                   0.292               0.302                          0.551
    blockchain 012:03450                           0.642              0.611                 0.428            0.196                          0.520                           0.228                              0.338              0.355                     0.369                 1.000                    0.147                         0.421               0.180                      0.248                              0.150                        0.470                 0.197                   0.367               0.533                          0.423



"""

import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from tm2p._intern import ParamsMixin

from ..dir_simil_netw import DirectMatrix


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
