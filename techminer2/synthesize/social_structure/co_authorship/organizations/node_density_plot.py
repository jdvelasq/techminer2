"""
Node Density Plot
===============================================================================


Smoke tests:
    >>> from techminer2.packages.networks.co_authorship.organizations import NodeDensityPlot
    >>> plot = (
    ...     NodeDensityPlot()
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
    ...     #
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_textfont_size_range(10, 20)
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_colormap("Aggrnyl")
    ...     .using_contour_opacity(0.6)
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
    >>> plot.write_html("docsrc/_generated/px.packages.networks.co_authorship.organizations.node_density_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.co_authorship.organizations.node_density_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""

from techminer2._internals import ParamsMixin
from techminer2.synthesize.conceptual_structure.co_occurrence.usr.node_density_plot import (
    NodeDensityPlot as UserNodeDensityPlot,
)


class NodeDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNodeDensityPlot()
            .update(**self.params.__dict__)
            .with_field("organizations")
            .run()
        )
