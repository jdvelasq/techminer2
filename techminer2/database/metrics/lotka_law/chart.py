# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Chart
===============================================================================


# >>> from techminer2.visualize.specialized_plots.lotka_law import chart
# >>> plot = chart(
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/",
# ...     database="main",
# ...     year_filter=None,
# ...     cited_by_filter=None,
# ... )
# >>> # plot.write_html("docs_src/_generated/visualize/specialized_charts/lotka_law/chart.html")

.. raw:: html

    <iframe src="../../../_generated/visualize/specialized_charts/lotka_law/chart.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import plotly.graph_objects as go  # type: ignore

from .dataframe import dataframe


def chart(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """:meta private:"""

    data_frame = dataframe(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data_frame["Documents Written"],
            y=data_frame["Proportion of Authors"],
            fill="tozeroy",
            name="Real",
            opacity=0.5,
            marker_color="darkslategray",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data_frame["Documents Written"],
            y=data_frame["Prop Theoretical Authors"],
            fill="tozeroy",
            name="Theoretical",
            opacity=0.5,
            marker_color="lightgrey",
        )
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title="Author Productivity through Lotka's Law",
    )

    fig.update_traces(
        marker=dict(
            size=7,
            line=dict(color="darkslategray", width=2),
        ),
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title="Documents Written",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title="Proportion of Authors",
    )

    return fig
