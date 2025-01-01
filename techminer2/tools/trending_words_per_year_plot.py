# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trending Words per Year Plot
===============================================================================

## >>> from techminer2.tools import trending_words_per_year_plot
## >>> plot = trending_words_per_year_plot(
## ...     #
## ...     # PARAMS:
## ...     field="author_keywords",
## ...     n_words_per_year=5,
## ...     custom_terms=None,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=None,
## ...     cited_by_filter=None,
## ... )
## >>> # plot.write_html("sphinx/tools/trending_words_per_year_plot.html")

.. raw:: html

    <iframe src="../_static/tools/trending_words_per_year_plot.html" 
    height="900px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go  # type: ignore

from .trending_words_per_year_frame import trending_words_per_year_frame


def trending_words_per_year_plot(
    #
    # PARAMS:
    field,
    #
    # ITEM FILTERS:
    n_words_per_year=5,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """:meta private:"""

    words_by_year = trending_words_per_year_frame(
        #
        # PARAMS:
        field=field,
        #
        # ITEM FILTERS:
        n_words_per_year=n_words_per_year,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    fig = go.Figure(
        go.Bar(
            x=words_by_year.width,
            y=words_by_year.index,
            base=words_by_year.year_q1,
            width=words_by_year.height,
            orientation="h",
            marker_color="lightslategrey",
        ),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
        dtick=1.0,
    )

    return fig
