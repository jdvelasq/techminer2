"""
Creates a SVD/MDS map used in T-LAB's comparative analysis (SVD map), 
words associations .

"""
import plotly.graph_objects as go


def map_chart(
    dataframe,
    dim_x=0,
    dim_y=1,
    delta=0.2,
):
    """Makes a map chart."""

    dataframe = dataframe.copy()

    node_x = dataframe[f"dim{dim_x}"]
    node_y = dataframe[f"dim{dim_y}"]

    x_mean = node_x.mean()
    y_mean = node_y.mean()
    textposition = []
    for x_pos, y_pos in zip(node_x, node_y):
        if x_pos >= x_mean and y_pos >= y_mean:
            textposition.append("top right")
        if x_pos <= x_mean and y_pos >= y_mean:
            textposition.append("top left")
        if x_pos <= x_mean and y_pos <= y_mean:
            textposition.append("bottom left")
        if x_pos >= x_mean and y_pos <= y_mean:
            textposition.append("bottom right")

    fig = go.Figure(
        layout=go.Layout(
            xaxis={"mirror": "allticks"},
            yaxis={"mirror": "allticks"},
        )
    )
    fig.add_trace(
        go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers+text",
            hoverinfo="text",
            textposition=textposition,
            text=dataframe.index.tolist(),
            # hovertext=dataframe.index.tolist(),
        )
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=1, r=1, t=1, b=1),
    )
    fig.update_traces(
        marker=dict(
            line=dict(color="darkslategray", width=2),
        ),
        marker_color="lightgrey",
    )

    x_max = node_x.max()
    x_min = node_x.min()
    x_range = x_max - x_min

    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        ticks="outside",
        tickwidth=2,
        ticklen=10,
        minor=dict(ticklen=5),
        range=[x_min - delta * x_range, x_max + delta * x_range],
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        ticks="outside",
        tickwidth=2,
        ticklen=10,
        minor=dict(ticklen=5),
    )
    return fig
