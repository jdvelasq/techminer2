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


>>> from techminer2.pkgs.networks.citation.organizations  import NodeDegreePlot
>>> plot = (
...     NodeDegreePlot()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_occurrence_threshold(2)
...     .having_terms_in(None)
...     #
...     # PLOT:
...     .using_textfont_size(10)
...     .using_marker_size(7)
...     .using_line_color("black")
...     .using_line_width(1.5)
...     .using_yshift(4)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> # plot.write_html("sphinx/_generated/pkgs/networks/citation/organizations/network_degree_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/networks/citation/organizations/network_degree_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>






"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.node_degree_plot import (
    NodeDegreePlot as OtherNodeDegreePlot,
)


class NodeDegreePlot(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            OtherNodeDegreePlot()
            .update(**self.params.__dict__)
            .unit_of_analysis("organizations")
            .build()
        )
