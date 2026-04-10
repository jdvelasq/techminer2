import networkx as nx  # type: ignore
import plotly.graph_objects as go  # type: ignore


def add_node_labels(
    fig: go.Figure,
    nx_graph: nx.Graph,
) -> go.Figure:

    nodes = sorted(nx_graph.nodes(data=True), reverse=True)

    for _, data in reversed(nodes):

        if not data["labeled"]:
            continue

        xanchor, yanchor, xshift, yshift = _map_text_position(data["textposition"])

        fig.add_annotation(
            x=data["x"],
            y=data["y"],
            text=f" {data['text']} ",
            showarrow=False,
            font={"size": data["textfont_size"]},
            bordercolor="grey",
            bgcolor="white",
            xanchor=xanchor,
            yanchor=yanchor,
            xshift=xshift,
            yshift=yshift,
            opacity=data["textfont_opacity"],
        )

    return fig


def _map_text_position(textpos):

    if textpos == "top right":
        return "left", "bottom", 4, 4

    if textpos == "top left":
        return "right", "bottom", -4, 4

    if textpos == "bottom right":
        return "left", "top", 4, -4

    if textpos == "bottom left":
        return "right", "top", -4, -4

    return "center", "center", 0, 0
