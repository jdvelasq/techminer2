"""
NodeDegreePlot
===============================================================================


* **CITED_AUTH**

.. raw:: html

    <iframe src="../_static/px.synthes.netw.co_cit.node_degree_plot_cited_auth.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NodeDegreePlot
    >>> fig = (
    ...     NodeDegreePlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_AUTH)
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.co_cit.node_degree_plot_cited_auth.html")


* **CITED_REF**

.. raw:: html

    <iframe src="../_static/px.synthes.netw.co_cit.node_degree_plot_cited_ref.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NodeDegreePlot
    >>> fig = (
    ...     NodeDegreePlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_REF)
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.co_cit.node_degree_plot_cited_ref.html")


* **CITED_SRC**

.. raw:: html

    <iframe src="../_static/px.synthes.netw.co_cit.node_degree_plot_cited_src.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NodeDegreePlot
    >>> fig = (
    ...     NodeDegreePlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_SRC)
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.co_cit.node_degree_plot_cited_src.html")


"""

from tm2p._intern.networks import BaseStrengthPlot

from ._node_metrics import NodeMetrics


class StrengthPlot(
    BaseStrengthPlot,
):
    """:meta private:"""

    def get_node_metrics(self):
        return NodeMetrics()


# from tm2p._intern import ParamsMixin
# from tm2p._intern.nx import (
#     assign_degree_to_nodes,
#     collect_node_degrees,
#     create_node_degree_dataframe,
#     create_node_degree_plot,
# )
# from tm2p.portfolio.intellectual_structure.co_citation_network._intern.create_nx_graph import (
#     create_nx_graph,
# )


# class NodeDegreePlot(
#     ParamsMixin,
# ):
#     """:meta private:"""

#     def run(self):

#         nx_graph = create_nx_graph(self.params)
#         nx_graph = assign_degree_to_nodes(nx_graph)
#         node_degrees = collect_node_degrees(nx_graph)
#         data_frame = create_node_degree_dataframe(node_degrees)
#         plot = create_node_degree_plot(self.params, data_frame)

#         return plot
