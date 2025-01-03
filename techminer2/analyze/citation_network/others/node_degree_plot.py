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
## >>> from techminer2.analyze.citation_network  import NodeDegreePlot
## >>> plot = (
## ...     NodeDegreePlot()
## ...     .set_analysis_params(
## ...         unit_of_analysis="abbr_source_title",
## ...         citations_threshold=0,
## ...         occurrence_threshold=2,
## ...         custom_terms=None,
## ...     #
## ...     ).set_plot_params(
## ...         textfont_size=10,
## ...         marker_size=7,
## ...         line_color="black",
## ...         line_width=1.5,
## ...         yshift=4,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> plot.write_html("sphinx/_static/citation_network/others_degree_plot.html")

.. raw:: html

    <iframe src="../_static/citation_network/others_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>





"""
from ....internals.nx.nx_assign_degree_to_nodes import nx_assign_degree_to_nodes

# from ....internals.nx_mixin.nx_degree import nx_degree_plot
from .internals.create_citation_nx_graph import _create_citation_nx_graph


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

    nx_graph = _create_citation_nx_graph(
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

    nx_graph = nx_assign_degree_to_nodes(nx_graph)

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
