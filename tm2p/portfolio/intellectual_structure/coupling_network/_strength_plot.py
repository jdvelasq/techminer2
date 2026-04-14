"""
Network Degree Plot
===============================================================================

* **CouplingUnit.AUTH**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.coupl.node_degree_plot_auth.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreePlot
    >>> fig = (
    ...     NodeDegreePlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.AUTH)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.coupl.node_degree_plot_auth.html")


* **CouplingUnit.CTRY**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.coupl.node_degree_plot_ctry.html"
    height="800px" w

    idth="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreePlot
    >>> fig = (
    ...     NodeDegreePlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.coupl.node_degree_plot_ctry.html")


* **CouplingUnit.DOC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.coupl.node_degree_plot_doc.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreePlot
    >>> fig = (
    ...     NodeDegreePlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.coupl.node_degree_plot_doc.html")


* **CouplingUnit.ORG**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.coupl.node_degree_plot_org.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreePlot
    >>> fig = (
    ...     NodeDegreePlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.ORG)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.coupl.node_degree_plot_org.html")


* **CouplingUnit.SRC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.coupl.node_degree_plot_src.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreePlot
    >>> fig = (
    ...     NodeDegreePlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.SRC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.coupl.node_degree_plot_src.html")


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
# from tm2p._intern.nx import create_node_degree_plot

# from .node_metrics import NodeMetrics


# class StrengthPlot(
#     ParamsMixin,
# ):
#     """:meta private:"""

#     def run(self):

#         use_counters = self.params.counters

#         self.params.counters = True
#         metrics = NodeMetrics().update(**self.params.__dict__).run()
#         metrics = metrics.reset_index().rename(columns={"index": "NODE"})
#         if use_counters is False:
#             self.params.counters = False
#             metrics["NODE"] = metrics["NODE"].str.split(" ").str[:-1].str.join(" ")
#         plot = create_node_degree_plot(self.params, metrics)

#         return plot
