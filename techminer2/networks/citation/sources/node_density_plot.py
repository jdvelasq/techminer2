# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Density Plot
===============================================================================


Example:
    >>> from techminer2.packages.networks.citation.sources  import NodeDensityPlot
    >>> plot = (
    ...     NodeDensityPlot()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
    ...     .using_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     # DENSITY:
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_colormap("Aggrnyl")
    ...     .using_contour_opacity(0.6)
    ...     .using_textfont_size_range(10, 20)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.packages.networks.citation.sources.node_density_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.citation.sources.node_density_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>



"""
from techminer2._internals import ParamsMixin
from techminer2.networks.citation._internals.from_others.node_density_plot import (
    NodeDensityPlot as OtherNodeDensityPlot,
)


class NodeDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            OtherNodeDensityPlot()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .unit_of_analysis("source_title_abbr")
            .run()
        )
