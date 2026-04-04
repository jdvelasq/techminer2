"""
FactorMap
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_structure.factorial_analysis.second_order.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke test:
    >>> from sklearn.decomposition import PCA
    >>> pca = PCA(
    ...     n_components=5,
    ...     whiten=False,
    ...     svd_solver="auto",
    ...     tol=0.0,
    ...     iterated_power="auto",
    ...     n_oversamples=10,
    ...     power_iteration_normalizer="auto",
    ...     random_state=0,
    ... )
    >>> from sklearn.cluster import KMeans
    >>> kmeans = KMeans(
    ...     n_clusters=6,
    ...     init="k-means++",
    ...     n_init=10,
    ...     max_iter=300,
    ...     tol=0.0001,
    ...     algorithm="elkan",
    ...     random_state=0,
    ... )
    >>> from tm2p import Field, ItemOrderBy, NodeScaling
    >>> from tm2p.portfolio.thematic_structure.factorial_analysis.second_order import FactorMap
    >>> plot = (
    ...     FactorMap()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(50)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(pca)
    ...     #
    ...     # MAP:
    ...     .using_edge_colors(("#7793a5", "#7793a5", "#7793a5", "#7793a5"))
    ...     .using_edge_widths((1.0, 1.0, 2.0, 3.5))
    ...     .using_edge_similarity_threshold(0.00001)
    ...     .using_edge_top_n(1000)
    ...     .using_top_edges_per_node(10)
    ...     .using_min_edges_per_node(2)
    ...     #
    ...     .using_node_colors(("#7793a5",))
    ...     .using_node_size_range(18, 90)
    ...     .using_node_scaling(NodeScaling.SQRT)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.portfolio.thematic_structure.factorial_analysis.second_order.html")



"""

import numpy as np
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_structure.correlation._intern.plot_correl_map import (
    plot_correl_map,
)

from .cluster_centers import ClusterCenters


class FactorMap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = ClusterCenters().update(**self.params.__dict__).run()
        matrix = pd.DataFrame(
            np.abs(cosine_similarity(matrix)),
            index=matrix.index,
            columns=matrix.index,
        )
        return plot_correl_map(self.params, matrix)
