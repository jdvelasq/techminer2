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

>>> from techminer2.pkgs.networks.citation.sources  import node_density_plot
>>> plot = (
...     NodeDensityPlot()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
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
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citattions_range_is(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> # plot.write_html("sphinx/_generated/pkgs/networks/citation/sources/node_density_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/networks/citation/sources/node_density_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>



"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.node_density_plot import (
    NodeDensityPlot as OtherNodeDensityPlot,
)


class NodeDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            OtherNodeDensityPlot()
            .update(**self.params.__dict__)
            .unit_of_analysis("source_title")
            .build()
        )
