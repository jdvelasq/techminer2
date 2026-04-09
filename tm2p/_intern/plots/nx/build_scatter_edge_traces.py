import networkx as nx  # type: ignore
import plotly.graph_objects as go  # type: ignore


def build_scatter_edge_traces(
    nx_graph: nx.Graph,
) -> list[go.Scatter]:

    edge_traces = []

    data = []

    for edge in nx_graph.edges():

        pos_x0 = nx_graph.nodes[edge[0]]["x"]
        pos_y0 = nx_graph.nodes[edge[0]]["y"]

        pos_x1 = nx_graph.nodes[edge[1]]["x"]
        pos_y1 = nx_graph.nodes[edge[1]]["y"]

        color = nx_graph.edges[edge]["color"]
        dash = nx_graph.edges[edge]["dash"]
        width = nx_graph.edges[edge]["width"]

        edge_trace = go.Scatter(
            x=(pos_x0, pos_x1),
            y=(pos_y0, pos_y1),
            line={
                "color": color,
                "dash": dash,
                "width": width,
            },
            hoverinfo="none",
            mode="lines",
        )

        data.append((edge_trace, width))

    data = sorted(data, key=lambda x: x[1])
    edge_traces = [x[0] for x in data]

    return edge_traces
