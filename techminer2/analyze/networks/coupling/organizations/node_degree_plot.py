# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Degree Plot
===============================================================================


Smoke tests:
    >>> from techminer2.packages.networks.coupling.organizations import NodeDegreePlot
    >>> plot = (
    ...     NodeDegreePlot()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .using_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.packages.networks.coupling.organizations.node_degree_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.coupling.organizations.node_degree_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""
from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.coupling._internals.from_others.node_degree_plot import (
    InternalNodeDegreePlot,
)


class NodeDegreePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNodeDegreePlot()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .unit_of_analysis("organizations")
            .run()
        )
