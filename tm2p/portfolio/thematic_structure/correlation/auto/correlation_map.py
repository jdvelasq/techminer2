"""
NetworkMap
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_structure.correlation.auto.correlation_map.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> # grey colors: https://www.w3schools.com/colors/colors_shades.asp
    >>> from tm2p import ItemOrderBy, Field, Correlation, NodeScaling
    >>> from tm2p.portfolio.thematic_structure.correlation.auto import CorrelationMap
    >>> plot = (
    ...     CorrelationMap()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(30)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method(Correlation.PEARSON)
    ...     #
    ...     # MAP:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(100)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_edge_colors(("#7793a5", "#7793a5", "#7793a5", "#7793a5"))
    ...     .using_edge_widths((1.0, 1.0, 2.0, 3.5))
    ...     .using_edge_similarity_threshold(0.20)
    ...     .using_edge_top_n(1000)
    ...     .using_top_edges_per_node(10)
    ...     .using_min_edges_per_node(2)
    ...     #
    ...     .using_node_colors(("#7793a5",))
    ...     .using_node_size_range(18, 90)
    ...     .using_node_scaling(NodeScaling.SQRT)
    ...     #
    ...     .using_node_n_labels(4)
    ...     .using_textfont_opacity_range(0.75, 1.00)
    ...     .using_textfont_size_range(11, 16)
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
    >>> plot.write_html("docsrc/_generated/px.portfolio.thematic_structure.correlation.auto.correlation_map.html")



"""

import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from tm2p import Correlation
from tm2p._intern import ParamsMixin

from .._intern import plot_correl_map
from .matrix import Matrix


class CorrelationMap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).using_counters(True).run()

        if self.params.correlation_method != Correlation.COSINE:
            matrix = pd.DataFrame(
                cosine_similarity(matrix),
                index=matrix.index,
                columns=matrix.columns,
            )

        return plot_correl_map(self.params, matrix)
