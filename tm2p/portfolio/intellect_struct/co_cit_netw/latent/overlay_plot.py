"""
OverlayPlot
===============================================================================

* **CITED_REF** / **CITED_AUTH** / **CITED_SRC**

.. raw:: html

    <iframe src="../_static/px.portfolio.intellect_struct.co_cit_netw.latent.overlay_plot_cited_auth.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import NodeSizeMetric, Scaling  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw.latent import OverlayPlot  # type: ignore
    >>> plot = (
    ...     OverlayPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(40)
    ...     .having_minimum_cited_unit_occurrences(3)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)    
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(0.30)
    ...     .using_spring_layout_iterations(50)
    ...     .using_spring_layout_seed(5)
    ...     #
    ...     .using_colorscale(
    ...         [
    ...             [0.00, "#2C7BB6"],
    ...             [0.35, "#00A6CA"],
    ...             [0.65, "#4EBA6F"],
    ...             [1.00, "#F28E2B"],
    ...         ]
    ...     )
    ...     .using_uniform_node_opacity(0.75)
    ...     .using_node_size_metric(NodeSizeMetric.OCC)
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_range(12, 80)
    ...     .using_top_n_nodes(50)
    ...     .using_min_node_degree(2)
    ...     #
    ...     .using_max_node_labels(20)
    ...     .using_node_label_max_length(40)
    ...     #
    ...     .using_textfont_opacity_range(0.55, 1.00)
    ...     .using_textfont_size_range(10, 24)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_uniform_edge_color("#d8d8d8")
    ...     .using_edge_opacity_range(0.25, 0.65)
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_global_top_edges(100)
    ...     .using_edge_width_range(1.5, 5.0)
    ...     .using_top_edges_per_node(5)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.portfolio.intellect_struct.co_cit_netw.latent.overlay_plot_cited_auth.html")

"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.adv.co_occ_overlay_plot import build_co_occ_overlay_plot
from tm2p.enum import AnalysisUnit

from ..direct.matrix import Matrix as CoOccurrenceMatrix
from .item_to_cluster import ItemToCluster
from .latent_matrix import LatentMatrix


class OverlayPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        similarity_matrix = (
            LatentMatrix().update(**self.params.__dict__).using_counters(True).run()
        )
        co_occ_matrix = (
            CoOccurrenceMatrix()
            .update(**self.params.__dict__)
            .using_counters(True)
            .run()
        )

        analysis_unit = self.params.analysis_unit
        units = co_occ_matrix.index.tolist()
        i2y = {}
        if analysis_unit == AnalysisUnit.CITED_REF:
            i2y = {
                " ".join(unit.split(" ")[:-1]): float(unit.split(",")[1].strip())
                for unit in units
            }
        elif analysis_unit in (
            AnalysisUnit.CITED_AUTH,
            AnalysisUnit.CITED_SRC,
        ):
            units = co_occ_matrix.index.tolist()

            df = pd.DataFrame(
                {"year": [float(unit.split(",")[1].strip()) for unit in units]}
            )

            if analysis_unit == AnalysisUnit.CITED_AUTH:
                pos = 0
            else:
                pos = 2
            df["unit"] = ([unit.split(",")[pos] for unit in units],)
            df = df.groupby("unit")["year"].mean()
            i2y = dict(zip(df.index, df["year"]))

        i2c = ItemToCluster().update(**self.params.__dict__).using_counters(True).run()

        fig = build_co_occ_overlay_plot(  # type: ignore
            params=self.params,
            similarity_matrix=similarity_matrix,
            co_occurrence_matrix=co_occ_matrix,
            i2c=i2c,
            i2y=i2y,  # type: ignore
        )

        return fig
