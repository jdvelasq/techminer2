"""
StrengthPlot
===============================================================================

* **CitationUnit.DOC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.node_degree_plot_auth.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CitationUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import StrengthPlot
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # PLOT:
    ...     .using_textfont_size(10)
    ...     .using_marker_size(7)
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
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
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.node_degree_plot_doc.html")


* **CitationUnit.AUTH**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.node_degree_plot_auth.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.AUTH)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # PLOT:
    ...     .using_textfont_size(10)
    ...     .using_marker_size(7)
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
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
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.node_degree_plot_auth.html")


* **CitationUnit.CTRY**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.node_degree_plot_ctry.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # PLOT:
    ...     .using_textfont_size(10)
    ...     .using_marker_size(7)
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
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
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.node_degree_plot_ctry.html")



* **CitationUnit.ORG**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.node_degree_plot_org.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.ORG)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # PLOT:
    ...     .using_textfont_size(10)
    ...     .using_marker_size(7)
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
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
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.node_degree_plot_org.html")



* **CitationUnit.SRC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.node_degree_plot_src.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.SRC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # PLOT:
    ...     .using_textfont_size(10)
    ...     .using_marker_size(7)
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
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
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.node_degree_plot_src.html")


"""

from tm2p._intern.networks import BaseStrengthPlot

from ._node_metrics import NodeMetrics


class StrengthPlot(
    BaseStrengthPlot,
):
    """:meta private:"""

    def get_node_metrics(self):
        return NodeMetrics()
