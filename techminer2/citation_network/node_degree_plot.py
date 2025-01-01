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

## >>> # article:
## >>> from techminer2.citation_network import node_degree_plot
## >>> plot = node_degree_plot(
## ...     unit_of_analysis="article",
## ...     #
## ...     # COLUMN PARAMS:
## ...     top_n=30, 
## ...     citations_threshold=0,
## ...     #
## ...     # DEGREE PLOT:
## ...     textfont_size=10,
## ...     marker_size=7,
## ...     line_color="black",
## ...     line_width=1.5,
## ...     yshift=4,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # plot.write_html("sphinx/_static/citation_network/article_degree_plot.html")

.. raw:: html

    <iframe src="../_static/citation_network/article_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

## >>> # abbr_source_title, authors, organizations, countries:
## >>> from techminer2.citation_network import node_degree_plot
## >>> plot = node_degree_plot(
## ...     unit_of_analysis="abbr_source_title",
## ...     #
## ...     # COLUMN PARAMS:
## ...     top_n=30,
## ...     citations_threshold=0,
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     #
## ...     # DEGREE PLOT:
## ...     textfont_size=10,
## ...     marker_size=7,
## ...     line_color="black",
## ...     line_width=1.5,
## ...     yshift=4,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # plot.write_html("sphinx/_static/citation_network/others_degree_plot.html")

.. raw:: html

    <iframe src="../_static/citation_network/others_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>




"""
from ._core.docs.node_degree_plot import _node_degree_plot as _node_degree_plot_from_docs
from ._core.others.node_degree_plot import _node_degree_plot as _node_degree_plot_from_others


def node_degree_plot(
    #
    # COLUMN PARAMS:
    unit_of_analysis,
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
    """:meta private:"""

    if unit_of_analysis == "article":

        return _node_degree_plot_from_docs(
            #
            # COLUMN PARAMS:
            top_n=top_n,
            citations_threshold=citations_threshold,
            #
            # DEGREE PLOT PARAMS:
            textfont_size=textfont_size,
            marker_size=marker_size,
            line_color=line_color,
            line_width=line_width,
            yshift=yshift,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return _node_degree_plot_from_others(
        #
        # FIELD PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DEGREE PLOT PARAMS:
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
