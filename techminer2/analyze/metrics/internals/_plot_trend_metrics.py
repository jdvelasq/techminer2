# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""Trend Metrics Chart"""

import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def plot_trend_metrics(
    #
    # METRICS:
    data_frame,
    metric_to_plot: str,
    auxiliary_metric_to_plot: str,
    #
    # CHART PARAMS:
    title: str,
    year_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
):
    """Makes a time line plot for indicators."""

    column_names = {column: column.replace("_", " ").title() for column in data_frame.columns if column not in ["OCC", "cum_OCC"]}
    column_names["OCC"] = "OCC"
    column_names["cum_OCC"] = "cum OCC"
    data_frame = data_frame.rename(columns=column_names)

    if metric_to_plot == "OCC":
        pass
    elif metric_to_plot == "cum_OCC":
        metric_to_plot = "cum OCC"
    else:
        metric_to_plot = metric_to_plot.replace("_", " ").title()

    if auxiliary_metric_to_plot is not None:
        if auxiliary_metric_to_plot == "OCC":
            pass
        elif auxiliary_metric_to_plot == "cum_OCC":
            auxiliary_metric_to_plot = "cum OCC"
        else:
            auxiliary_metric_to_plot = auxiliary_metric_to_plot.replace("_", " ").title()

    fig = px.line(
        data_frame,
        x=data_frame.index,
        y=metric_to_plot,
        title=title,
        markers=True,
        hover_data=data_frame.columns.to_list(),
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
        title=metric_to_plot if metric_label is None else metric_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
        title="Year" if year_label is None else year_label,
        tickmode="array",
        tickvals=data_frame.index,
    )

    if auxiliary_metric_to_plot is not None:
        for index, row in data_frame.iterrows():
            fig.add_annotation(
                x=index,
                y=row[metric_to_plot],
                text=format(int(row[auxiliary_metric_to_plot]), ","),
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={"size": textfont_size},
                yshift=yshift,
            )

    return fig
