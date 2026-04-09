import plotly.graph_objects as go  # type: ignore


def build_network_figure(
    edge_traces,
    node_trace,
):
    """Creates a network graph from traces using plotly express."""

    layout = go.Layout(
        title="",
        font={"size": 16},
        showlegend=False,
        hovermode="closest",
        margin={"b": 0, "l": 0, "r": 0, "t": 0},
        annotations=[
            {
                "text": "",
                "showarrow": False,
                "xref": "paper",
                "yref": "paper",
                "x": 0.005,
                "y": -0.002,
                "align": "left",
                "font": {"size": 10},
            }
        ],
    )

    fig = go.Figure(
        data=edge_traces + [node_trace],
        layout=layout,
    )

    fig.update_layout(
        hoverlabel={
            "bgcolor": "white",
            "font_family": "monospace",
        },
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    return fig
