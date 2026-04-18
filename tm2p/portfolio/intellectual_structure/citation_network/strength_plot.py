"""
StrengthPlot
===============================================================================

* **AnalysisUnit.DOC**


.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.node_degree_plot_auth.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import StrengthPlot
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
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
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.node_degree_plot_doc.html")

* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**


"""

from tm2p._intern.networks import BaseStrengthPlot

from .node_metrics import NodeMetrics


class StrengthPlot(
    BaseStrengthPlot,
):
    """:meta private:"""

    def get_node_metrics(self):
        return NodeMetrics()
