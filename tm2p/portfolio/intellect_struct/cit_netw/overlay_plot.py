"""
OverlayPlot
===============================================================================

* **AnalysisUnit.DOC**

.. raw:: html

    <iframe src="../_generated/px.portfolio.intellect_struct.cit_netw.overlay_plot_doc.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import Scaling  # type: ignore
    >>> from tm2p.enum import NodeSizeMetric  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.cit_netw import OverlayPlot  # type: ignore
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     OverlayPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(0.27)
    ...     .using_spring_layout_iterations(100)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_colorscale(
    ...         [
    ...             [0.00, "#2C7BB6"],
    ...             [0.35, "#00A6CA"],
    ...             [0.65, "#4EBA6F"],
    ...             [1.00, "#F28E2B"],
    ...         ]
    ...     )
    ...     .using_min_node_degree(2)
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_metric(NodeSizeMetric.TLS)
    ...     .using_node_size_range(12, 80)
    ...     .using_top_n_nodes(50)
    ...     .using_uniform_node_opacity(0.75)
    ...     #
    ...     .using_max_node_labels(15)
    ...     .using_node_label_max_length(20)
    ...     #
    ...     .using_textfont_opacity_range(0.55, 1.00)
    ...     .using_textfont_size_range(10, 24)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_edge_opacity_range(0.25, 0.65)
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_edge_width_range(1.5, 5.0)
    ...     .using_global_top_edges(200)
    ...     .using_top_edges_per_node(5)
    ...     .using_uniform_edge_color("#d8d8d8")
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
    >>> fig.write_html("docsrc/_generated/px.portfolio.intellect_struct.cit_netw.overlay_plot_doc.html")



* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

.. raw:: html

    <iframe src="../_generated/px.portfolio.intellect_struct.cit_netw.overlay_plot_auth.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # OTHER
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     OverlayPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(30)
    ...     .having_units_in(None)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(0.27)
    ...     .using_spring_layout_iterations(100)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_colorscale(
    ...         [
    ...             [0.00, "#2C7BB6"],
    ...             [0.35, "#00A6CA"],
    ...             [0.65, "#4EBA6F"],
    ...             [1.00, "#F28E2B"],
    ...         ]
    ...     )
    ...     .using_min_node_degree(2)
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_metric(NodeSizeMetric.TLS)
    ...     .using_node_size_range(12, 80)
    ...     .using_top_n_nodes(50)
    ...     .using_uniform_node_opacity(0.75)
    ...     #
    ...     .using_max_node_labels(15)
    ...     .using_node_label_max_length(20)
    ...     #
    ...     .using_textfont_opacity_range(0.55, 1.00)
    ...     .using_textfont_size_range(10, 24)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_edge_opacity_range(0.25, 0.65)
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_edge_width_range(1.5, 5.0)
    ...     .using_global_top_edges(200)
    ...     .using_top_edges_per_node(5)
    ...     .using_uniform_edge_color("#d8d8d8")
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
    >>> fig.write_html("docsrc/_generated/px.portfolio.intellect_struct.cit_netw.overlay_plot_auth.html")




"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.adv.co_occ_overlay_plot import build_co_occ_overlay_plot
from tm2p.enum import AnalysisUnit, UnitOrderBy
from tm2p.portfolio.perform_metr.trend.trend import Trends

from .dir_matrix import DirectMatrix
from .item_to_clust import ItemToCluster
from .matrix import Matrix as CoOccurrenceMatrix


class OverlayPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        similarity_matrix = (
            DirectMatrix().update(**self.params.__dict__).using_counters(True).run()
        )
        co_occ_matrix = (
            CoOccurrenceMatrix()
            .update(**self.params.__dict__)
            .using_counters(True)
            .run()
        )

        if self.params.analysis_unit == AnalysisUnit.DOC:
            docs = similarity_matrix.index.to_list()
            docs = [" ".join(d.split(" ")[:-1]) for d in docs]
            years = [int(d.split(", ")[1]) for d in docs]
            i2y = dict(zip(docs, years))

        else:
            trends = (
                Trends()
                .update(**self.params.__dict__)
                .having_top_n_units(None)
                .having_unit_global_citation_between(None, None)
                .having_unit_occurrence_between(None, None)
                .having_units_in(None)
                .having_units_ordered_by(UnitOrderBy.OCC)
                .run()
            )
            years = trends.columns.astype(int)
            avg_year = (trends * years).sum(axis=1) / trends.sum(axis=1)
            avg_year = avg_year.round(1)
            i2y = dict(zip(trends.index, avg_year))

        i2c = ItemToCluster().update(**self.params.__dict__).using_counters(True).run()

        fig = build_co_occ_overlay_plot(
            params=self.params,
            similarity_matrix=similarity_matrix,
            co_occurrence_matrix=co_occ_matrix,
            i2c=i2c,
            i2y=i2y,
        )

        return fig
