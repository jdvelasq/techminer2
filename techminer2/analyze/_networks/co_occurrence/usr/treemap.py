"""
Treemap
===============================================================================


Smoke tests:
    >>> from techminer2.co_occurrence_network.user import Treemap
    >>> plot = (
    ...     Treemap()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords")
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
    ...     .using_title_text(None)
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
    >>> plot.write_html("docsrc/_generated/px.packages.networks.co_occurrence.user.treemap.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.co_occurrence.user.treemap.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.nx import (
    internal__assign_node_colors_based_on_group_attribute,
    internal__cluster_nx_graph,
    internal__plot_node_treemap,
)
from techminer2.analyze._networks.co_occurrence._internals.create_nx_graph import (
    internal__create_nx_graph,
)


class Treemap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        nx_graph = internal__assign_node_colors_based_on_group_attribute(nx_graph)
        return internal__plot_node_treemap(self.params, nx_graph)
        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        nx_graph = internal__assign_node_colors_based_on_group_attribute(nx_graph)
        return internal__plot_node_treemap(self.params, nx_graph)
