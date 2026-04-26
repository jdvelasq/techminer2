"""
Network Degree Plot
===============================================================================

* **AnalysisUnit.DOC**


* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.coupl.node_degree_plot_auth.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm, UnitOrderBy
    >>> from tm2p.portfolio.intellect_struct.coupl_netw import StrengthPlot
    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # COUPLING UNIT:
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
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_uniform_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.coupl.node_degree_plot_auth.html")



"""

from tm2p._intern.netw import BaseStrengthPlot

from .node_metrics import NodeMetrics


class StrengthPlot(
    BaseStrengthPlot,
):
    """:meta private:"""

    def get_node_metrics(self):
        return NodeMetrics()
