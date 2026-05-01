"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.gap_analysis.white_space.cross_occur.matrix import Matrix  # type: ignore
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COLUMNS:
    ...     .with_column_analysis_unit(AnalysisUnit.KW)
    ...     .having_column_units_in_top(100)
    ...     .having_column_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_column_unit_occurrence_between(None, None)
    ...     .having_column_unit_citation_between(None, None)
    ...     .having_column_units_in(None)
    ...     #
    ...     # ROWS:
    ...     .with_index_analysis_unit(AnalysisUnit.CTRY)
    ...     .having_index_units_in_top(100)
    ...     .having_index_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_index_unit_occurrence_between(2, None)
    ...     .having_index_unit_citation_between(None, None)
    ...     .having_index_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.INCLUSION)    
    ...     #
    ...     # WHITESPACE ANALYSIS:
    ...     .using_wh_gap_computation(GapComputation.LATENT_MINUS_OBSERVED)
    ...     .using_wh_minimum_latent_similarity(0.02)
    ...     .using_wh_maximum_observed_similarity(0.1)    
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     #
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
    columns          tinyml 1031:010091  machine learning 0766:008244  tiny machine learning 0388:003654  internet of things 0346:005415  learning systems 0343:003524
    rows                                                                                                                                                              
    ITA 0257:002515                 0.0                           0.0                                0.0                             0.0                           0.0
    IND 0257:002182                 0.0                           0.0                                0.0                             0.0                           0.0
    USA 0169:001828                 0.0                           0.0                                0.0                             0.0                           0.0
    CHN 0128:001388                 0.0                           0.0                                0.0                             0.0                           0.0
    DEU 0089:000811                 0.0                           0.0                                0.0                             0.0                           0.0





"""

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import GapComputation  # type: ignore
from tm2p.enum import AssociationIndex
from tm2p.portfolio.perform_metr.unit import Metrics
from tm2p.portfolio.thematic_struct.cross_occur.matrix import CountMatrix
from tm2p.portfolio.thematic_struct.tfidf import Matrix as TfIdfMatrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def _compute_observed_cross_occurrence_matrix(self):
        return CountMatrix().update(**self.params.__dict__).run()

    def _compute_column_tf_matrix(self):
        return (
            TfIdfMatrix()
            #
            .update(**self.params.__dict__)
            #
            .with_analysis_unit(self.params.column_analysis_unit)
            #
            .having_top_n_units(self.params.top_n_column_units)
            .having_units_ordered_by(self.params.column_unit_order_by)
            .having_unit_occurrence_between(
                self.params.column_unit_occurrence_range[0],
                self.params.column_unit_occurrence_range[1],
            )
            .having_unit_global_citation_between(
                self.params.column_unit_citation_range[0],
                self.params.column_unit_citation_range[1],
            )
            .having_units_in(self.params.column_units_in)
            #
            # COUNTERS:
            .using_counters(True)
            #
            # TFIDF:
            .using_tfidf_binary_frequencies(True)
            .using_tfidf_norm(None)
            .using_tfidf_smooth_idf(False)
            .using_tfidf_sublinear_tf(False)
            .using_tfidf_use_idf(False)
            #
            .run()
        )

    def _compute_index_tf_matrix(self):
        return (
            TfIdfMatrix()
            #
            .update(**self.params.__dict__)
            #
            .with_analysis_unit(self.params.index_analysis_unit)
            #
            .having_top_n_units(self.params.top_n_index_units)
            .having_units_ordered_by(self.params.index_item_order_by)
            .having_unit_occurrence_between(
                self.params.index_unit_occurrence_range[0],
                self.params.index_unit_occurrence_range[1],
            )
            .having_unit_global_citation_between(
                self.params.index_unit_citation_range[0],
                self.params.index_unit_citation_range[1],
            )
            .having_units_in(self.params.index_units_in)
            #
            # COUNTERS:
            .using_counters(True)
            #
            # TFIDF:
            .using_tfidf_binary_frequencies(True)
            .using_tfidf_norm(None)
            .using_tfidf_smooth_idf(False)
            .using_tfidf_sublinear_tf(False)
            .using_tfidf_use_idf(False)
            #
            .run()
        )

    def _normalize_matrix(self, observed, idx_tf_matrix, col_tf_matrix):

        idx_tf_matrix, col_tf_matrix = idx_tf_matrix.align(
            col_tf_matrix,
            axis=0,
            fill_value=0,
        )

        idx_occ = idx_tf_matrix.loc[:, observed.index].sum(axis=0).to_numpy()

        col_occ = col_tf_matrix.loc[:, observed.columns].sum(axis=0).to_numpy()
        values = observed.to_numpy(dtype=float)

        if self.params.association_index == AssociationIndex.JACCARD:
            den = idx_occ[:, None] + col_occ[None, :] - values
            normalized = values / (den + 1e-12)

        elif self.params.association_index in {
            AssociationIndex.COSINE,
            AssociationIndex.SALTON,
        }:
            den = np.sqrt(idx_occ[:, None] * col_occ[None, :])
            normalized = values / (den + 1e-12)

        elif self.params.association_index == AssociationIndex.DICE:
            den = idx_occ[:, None] + col_occ[None, :]
            normalized = 2.0 * values / (den + 1e-12)

        elif self.params.association_index == AssociationIndex.INCLUSION:
            den = np.minimum(idx_occ[:, None], col_occ[None, :])
            normalized = values / (den + 1e-12)

        elif self.params.association_index == AssociationIndex.EQUIVALENCE:
            den = idx_occ[:, None] * col_occ[None, :]
            normalized = values**2 / (den + 1e-12)

        elif self.params.association_index == AssociationIndex.ASSOCIATION_STRENGTH:
            den = idx_occ[:, None] * col_occ[None, :]
            normalized = values / (den + 1e-12)

        else:
            raise ValueError(
                f"Invalid association index: {self.params.association_index}"
            )

        return pd.DataFrame(
            normalized,
            index=observed.index,
            columns=observed.columns,
        )

    def _compute_latent_matrix(self, observed, idx_tf_matrix, col_tf_matrix):

        idx_tf_matrix, col_tf_matrix = idx_tf_matrix.align(
            col_tf_matrix,
            axis=0,
            fill_value=0,
        )

        idx_items = observed.index
        col_items = observed.columns

        A = idx_tf_matrix.loc[:, idx_items].to_numpy(dtype=float)
        B = col_tf_matrix.loc[:, col_items].to_numpy(dtype=float)

        A = (A > 0).astype(int)
        B = (B > 0).astype(int)

        latent = cosine_similarity(A.T, B.T)

        return pd.DataFrame(
            latent,
            index=idx_items,
            columns=col_items,
        )

    def _compute_white_space(self, observed, latent):

        mask = (latent >= self.params.wh_minimum_latent_similarity) & (
            observed <= self.params.wh_maximum_observed_similarity
        )

        if self.params.wh_gap_computation == GapComputation.LATENT_MINUS_OBSERVED:
            white_space = (latent - observed).clip(lower=0.0)

        elif self.params.wh_gap_computation == GapComputation.RELATIVE_LATENT_GAP:
            white_space = (latent - observed) / (latent + 1e-12)
            white_space = white_space.clip(lower=0.0)

        elif self.params.wh_gap_computation == GapComputation.STRUCTURAL_HOLE_SOFT:
            white_space = latent * (1.0 - observed)

        else:
            raise ValueError(
                f"Unknown gap computation method: {self.params.wh_gap_computation}"
            )

        white_space = white_space.where(mask, 0.0)

        return white_space

    def run(self):

        observed = self._compute_observed_cross_occurrence_matrix()
        idx_tf_matrix = self._compute_index_tf_matrix()
        col_tf_matrix = self._compute_column_tf_matrix()
        observed = self._normalize_matrix(observed, idx_tf_matrix, col_tf_matrix)
        latent = self._compute_latent_matrix(observed, idx_tf_matrix, col_tf_matrix)
        white_space = self._compute_white_space(observed, latent)

        return white_space
