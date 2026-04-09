import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params


def configure_figure_axes(
    params: Params,
    fig: go.Figure,
) -> go.Figure:

    if params.axes_visible is False:
        fig.update_layout(
            xaxis={
                "showgrid": False,
                "zeroline": False,
                "showticklabels": False,
            },
            yaxis={
                "showgrid": False,
                "zeroline": False,
                "showticklabels": False,
            },
        )

    if params.xaxes_range is not None:
        fig.update_xaxes(range=params.xaxes_range)

    if params.yaxes_range is not None:
        fig.update_yaxes(range=params.yaxes_range)

    fig.update_layout(
        hoverlabel={
            "bgcolor": "white",
            "font_family": "monospace",
        },
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    return fig
