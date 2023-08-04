# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""Metrics by Year Chart"""

import plotly.express as px

from .metrics_per_year import metrics_per_year

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def metrics_by_year_chart(
    indicator_to_plot: str,
    auxiliary_indicator: str,
    #
    # CHART PARAMS:
    title: str,
    year_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Makes a time line plot for indicators."""

    df = metrics_per_year(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    column_names = {
        column: column.replace("_", " ").title()
        for column in df.columns
        if column not in ["OCC", "cum_OCC"]
    }
    column_names["OCC"] = "OCC"
    column_names["cum_OCC"] = "cum OCC"
    df = df.rename(columns=column_names)

    if indicator_to_plot == "OCC":
        pass
    elif indicator_to_plot == "cum_OCC":
        indicator_to_plot = "cum OCC"
    else:
        indicator_to_plot = indicator_to_plot.replace("_", " ").title()

    if auxiliary_indicator == "OCC":
        pass
    elif auxiliary_indicator == "cum_OCC":
        auxiliary_indicator = "cum OCC"
    else:
        auxiliary_indicator = auxiliary_indicator.replace("_", " ").title()

    fig = px.line(
        df,
        x=df.index,
        y=indicator_to_plot,
        title=title,
        markers=True,
        hover_data=["OCC", "Global Citations", "Local Citations"],
    )
    fig.update_traces(
        marker={
            "size": marker_size,
            "line": {"color": MARKER_LINE_COLOR, "width": 2},
        },
        marker_color=MARKER_COLOR,
        line={"color": MARKER_LINE_COLOR, "width": line_width},
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title=indicator_to_plot if metric_label is None else metric_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
        title="Year" if year_label is None else year_label,
    )

    for index, row in df.iterrows():
        fig.add_annotation(
            x=index,
            y=indicator_to_plot,
            text=str(int(row[auxiliary_indicator])),
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return fig
