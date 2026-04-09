import networkx as nx  # type: ignore
import plotly.graph_objects as go  # type: ignore


def build_scatter_node_trace(
    nx_graph: nx.Graph,
) -> go.Scatter:

    node_x = [data["x"] for _, data in nx_graph.nodes(data=True)]
    node_y = [data["y"] for _, data in nx_graph.nodes(data=True)]

    node_color = [data["node_color"] for _, data in nx_graph.nodes(data=True)]
    node_size = [data["node_size"] for _, data in nx_graph.nodes(data=True)]
    node_text = [data["text"] for _, data in nx_graph.nodes(data=True)]

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        text=node_text,
        hoverinfo="text",
        marker={
            "color": node_color,
            "size": node_size,
            "line": {"width": 1.5, "color": "white"},
            "opacity": 1.0,
        },
    )

    return node_trace
