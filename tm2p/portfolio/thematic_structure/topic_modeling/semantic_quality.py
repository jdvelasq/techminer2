"""
SemanticQuality
===============================================================================

Smoke tests:
    >>> from sklearn.decomposition import LatentDirichletAllocation
    >>> lda = LatentDirichletAllocation(
    ...     n_components=10,
    ...     learning_decay=0.7,
    ...     learning_offset=50.0,
    ...     max_iter=10,
    ...     batch_size=128,
    ...     evaluate_every=-1,
    ...     perp_tol=0.1,
    ...     mean_change_tol=0.001,
    ...     max_doc_update_iter=100,
    ...     random_state=0,
    ... )
    >>> from tm2p.enum import UnitOrderBy, Field
    >>> from tm2p.portfolio.thematic_stucture.topic_modeling import SemanticQuality
    >>> df = (
    ...     SemanticQuality()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(lda)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_item_frequencies(False)
    ...     .using_tfidf_norm(None)
    ...     .using_tfidf_smooth_idf(False)
    ...     .using_tfidf_sublinear_tf(False)
    ...     .using_tfidf_use_idf(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df
       THEME  MEAN SIMILARITY  MIN SIMILARITY  MAX SIMILARITY
    0      5         0.829983        0.500000             1.0
    1      7         0.733855        0.288675             1.0
    2      4         0.717160        0.353553             1.0
    3      3         0.647684        0.333333             1.0
    4      9         0.606759        0.258199             1.0
    5      8         0.598507        0.267261             1.0
    6      1         0.593264        0.353553             1.0
    7      2         0.585529        0.288675             1.0
    8      0         0.565874        0.250000             1.0
    9      6         0.555846        0.223607             1.0




"""

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_structure.tfidf.matrix import Matrix as TfIdf

from .theme_to_items import ThemeToItems


class SemanticQuality(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        tf_matrix = TfIdf().update(**self.params.__dict__).run()
        theme_to_items = ThemeToItems().update(**self.params.__dict__).run()
        top_items = {k: v[:10] for k, v in theme_to_items.items()}

        def coherence(items, tf_matrix):

            tf_subset = tf_matrix[items]
            n_cols = tf_subset.shape[1]

            similarity = cosine_similarity(tf_subset)

            sims = []
            for i in range(n_cols - 1):
                for j in range(i + 1, n_cols):
                    s = similarity[i, j]
                    sims.append(s)
            return (np.mean(sims), np.min(sims), np.max(sims))

        scores = [
            coherence(top_items[theme], tf_matrix) for theme in sorted(top_items.keys())
        ]

        df = pd.DataFrame(
            scores,
            columns=[
                "MEAN SIMILARITY",
                "MIN SIMILARITY",
                "MAX SIMILARITY",
            ],
            index=sorted(top_items.keys()),
        )

        df.index.name = "THEME"
        df = df.sort_values("MEAN SIMILARITY", ascending=False)
        df = df.reset_index(drop=False)

        return df
