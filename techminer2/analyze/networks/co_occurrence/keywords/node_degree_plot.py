"""
Node Degree Plot
===============================================================================


Smoke tests:
    >>> from techminer2.co_occurrence_network.keywords import NodeDegreePlot
    >>> plot = (
    ...     NodeDegreePlot()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index("association")
    ...     #
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.packages.networks.co_occurrence.keywords.node_degree_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.co_occurrence.keywords.node_degree_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>



"""

"""Node Degree Plot"""
from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.node_degree_plot import (
    NodeDegreePlot as UserNodeDegreePlot,
)


class NodeDegreePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNodeDegreePlot()
            .update(**self.params.__dict__)
            .with_field("keywords")
            .run()
        )
