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

## >>> from techminer2.pkgs.networks.coupling.articles import NodeDegreePlot
## >>> plot = (
## ...     NodeDegreePlot()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .having_terms_in_top(20)
## ...     .having_citation_threshold(0)
## ...     #
## ...     # PLOT:
## ...     .using_line_color("black")
## ...     .using_line_width(1.5)
## ...     .using_marker_size(7)
## ...     .using_textfont_size(10)
## ...     .using_yshift(4)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> # plot.write_html("sphinx/_generated/pkgs/networks/coupling/articles/node_degree_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/networks/coupling/articles/node_degree_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>




"""
from .....internals.mixins import InputFunctionsMixin

# from ....internals.nx_mixin.nx_degree import nx_degree_plot
from ..internals.from_articles.create_nx_graph import internal__create_nx_graph


class NodeDegreePlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        pass


def _node_degree_plot(
    #
    # ARTICLE PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # DEGREE PLOT:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):

    nx_graph = internal__create_nx_graph(
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return nx_degree_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # DEGREE PLOT PARAMS:
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
