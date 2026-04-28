"""
SimilarityBetweenThemes
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
    >>> from tm2p.portfolio.thematic_struct.topic_modeling import SimilarityBetweenThemes
    >>> df = (
    ...     SimilarityBetweenThemes()
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
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.round(3).head()
    THEME      0      1      2      3      4      5      6      7      8      9
    THEME
    0      1.000  0.538  0.525  0.506  0.621  0.408  0.569  0.410  0.447  0.506
    1      0.538  1.000  0.427  0.443  0.546  0.521  0.518  0.413  0.403  0.463
    2      0.525  0.427  1.000  0.439  0.389  0.318  0.421  0.417  0.344  0.354
    3      0.506  0.443  0.439  1.000  0.433  0.339  0.417  0.329  0.326  0.448
    4      0.621  0.546  0.389  0.433  1.000  0.439  0.546  0.408  0.339  0.387



"""

import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from tm2p._intern import ParamsMixin

from .normalized_components_by_item import NormalizedComponentsByItem


class SimilarityBetweenThemes(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        components_by_theme = (
            NormalizedComponentsByItem().update(**self.params.__dict__).run()
        )

        similarity = cosine_similarity(components_by_theme)

        df = pd.DataFrame(
            similarity,
            index=components_by_theme.index,
            columns=components_by_theme.index,
        )
        df.index.name = "THEME"
        df.columns.name = "THEME"

        return df
