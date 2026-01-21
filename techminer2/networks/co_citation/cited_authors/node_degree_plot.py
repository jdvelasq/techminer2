# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Plot
===============================================================================


Example:
    >>> from techminer2.packages.networks.co_citation.cited_authors import NodeDegreePlot
    >>> plot = (
    ...     NodeDegreePlot()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
    ...     .using_citation_threshold(0)
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
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.packages.networks.co_citation.cited_authors.node_degree_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.co_citation.cited_authors.node_degree_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.co_citation._internals.node_degree_plot import (
    NodeDegreePlot as InternalNodeDegreePlot,
)


class NodeDegreePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNodeDegreePlot()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_authors")
            .run()
        )
