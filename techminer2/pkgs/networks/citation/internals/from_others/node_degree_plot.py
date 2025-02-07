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

## >>> # abbr_source_title, authors, organizations, countries:
## >>> from techminer2.pkgs.citation_network  import NodeDegreePlot
## >>> plot = (
## ...     NodeDegreePlot()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .unit_of_analysis('source_title')
## ...     .having_terms_in_top(30)
## ...     .having_citation_threshold(0)
## ...     .having_occurrence_threshold(2)
## ...     .having_terms_in(None)
## ...     #
## ...     ).set_plot_params(
## ...     .using_textfont_size(10)
## ...     .using_marker_size(7)
## ...         line_color="black",
## ...     .using_line_width(1.5)
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
## >>> plot.write_html("sphinx/_static/citation_network/others_degree_plot.html")

.. raw:: html

    <iframe src="../_static/citation_network/others_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>





"""

from ......internals.mixins import InputFunctionsMixin
from ......internals.nx.assign_degree_to_nodes import internal__assign_degree_to_nodes

# from ....internals.nx_mixin.nx_degree import nx_degree_plot
from .create_nx_graph import internal__create_nx_graph


class NodeDegreePlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        pass


def _node_degree_plot(
    #
    # FIELD PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    occurrence_threshold=None,
    custom_terms=None,
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
    """:meta private:"""

    nx_graph = internal__create_nx_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = internal__assign_degree_to_nodes(nx_graph)

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
