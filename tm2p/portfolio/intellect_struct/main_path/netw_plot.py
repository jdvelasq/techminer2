"""
Network Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.intellect_struct.main_path.network_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.enum import NodeSizeMetric  # type: ignore
    >>> from tm2p.enum import Scaling  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.main_path import NetworkPlot  # type: ignore
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_top_n_units(None)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    ...     .using_min_node_degree(1)
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_metric(NodeSizeMetric.GCS)
    ...     .using_node_size_range(12, 80)
    ...     .using_top_n_nodes(1000)
    ...     .using_uniform_node_opacity(0.75)
    ...     #
    ...     .using_max_node_labels(15)
    ...     .using_node_label_max_length(20)
    ...     #
    ...     .using_textfont_opacity_range(0.55, 1.00)
    ...     .using_textfont_size_range(10, 24)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_edge_opacity_range(0.35, 0.75)
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_edge_width_range(1.5, 5.0)
    ...     .using_global_top_edges(1000)
    ...     .using_top_edges_per_node(1000)
    ...     .using_uniform_edge_color("#BFC5CC")
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
    >>> fig.write_html("docsrc/_generated/px.portfolio.intellect_struct.main_path.network_plot.html")



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.adv.co_occ_overlay_plot import build_co_occ_overlay_plot
from tm2p.portfolio.intellect_struct.main_path.matrix import Matrix


class NetworkPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        matrix = Matrix().update(**self.params.__dict__).run()

        units = sorted(set(matrix.index.to_list() + matrix.columns.to_list()))
        u2c = {unit: 0 for unit in units}
        units = [" ".join(u.split(" ")[:-1]) for u in units]
        u2y = {unit: float(unit.split(", ")[1]) for unit in units}

        self.using_counters(False)

        fig = build_co_occ_overlay_plot(
            params=self.params,
            similarity_matrix=matrix,
            co_occurrence_matrix=matrix,
            i2c=u2c,
            i2y=u2y,
        )

        return fig
