# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Chart
===============================================================================

# >>> from techminer2.visualize.specialized_plots.bradford_law import chart
# >>> plot = chart(
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/",
# ...     database="main",
# ...     year_filter=(None, None),
# ...     cited_by_filter=(None, None),
# ... )
# >>> plot.write_html("docs_src/_generated/px.visualize/specialized_charts/bradford_law/chart.html")

.. raw:: html

    <iframe src="../../../_generated/visualize/specialized_charts/bradford_law/chart.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""

import plotly.express as px  # type: ignore

from .zones import zones as bradford_law_zones


def chart(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    zones = bradford_law_zones(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    fig = px.line(
        zones,
        x="no",
        y="OCC",
        title="Source Clustering through Bradford's Law",
        markers=True,
        hover_data=[zones.index, "OCC"],
        log_x=True,
    )
    fig.update_traces(
        marker=dict(size=5, line=dict(color="darkslategray", width=1)),
        marker_color="rgb(171,171,171)",
        line=dict(color="darkslategray"),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis_title=None,
        xaxis_showticklabels=False,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
    )

    core = len(zones.loc[zones.zone == 1])

    fig.add_shape(
        type="rect",
        x0=1,
        y0=0,
        x1=core,
        y1=zones.OCC.max(),
        line=dict(
            color="lightgrey",
            width=2,
        ),
        fillcolor="lightgrey",
        opacity=0.2,
    )

    fig.data = fig.data[::-1]

    return fig
