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

## >>> from techminer2.pkgs.co_citation_network import NodeDegreePlot
## >>> plot = (
## ...     NodeDegreePlot()
## ...     .set_analysis_params(
## ...         unit_of_analysis="cited_sources", # "cited_sources", 
## ...                                           # "cited_references",
## ...                                           # "cited_authors"
## ...         top_n=30, 
## ...         citations_threshold=None,
## ...         custom_terms=None,
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
## >>> plot.write_html("sphinx/_static/co_citation_network/node_degree_plot.html")

.. raw:: html

    <iframe src="../_static/co_citation_network/node_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""

# from ...internals.nx_mixin.nx_degree import nx_degree_plot
from .internals.create_co_citation_nx_graph import _create_co_citation_nx_graph


def node_degree_plot(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
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

    nx_graph = _create_co_citation_nx_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        custom_terms=custom_terms,
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
