import networkx as nx  # type: ignore
import pandas as pd  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params

from ..nx import (
    add_node_colorscale,
    add_node_labels,
    build_network_plot,
    build_scatter_edge_traces,
    build_scatter_node_trace,
    configure_figure_axes,
    keep_top_k_edges_per_node,
    keep_top_n_edges,
    keep_top_n_nodes,
    remove_isolated_nodes,
    remove_selfloop_edges,
    remove_weak_nodes,
    scale_edge_opacity,
    scale_edge_weight,
    scale_edge_width,
    scale_node_size,
    scale_textfont_opacity,
    scale_textfont_size,
    set_edge_color_by_group,
    set_edge_width_from_pandas_adjacency,
    set_node_color_by_year,
    set_node_opacity,
    set_node_size_properties,
    set_node_textposition,
    set_node_year,
    set_top_n_node_labels,
    set_uniform_edge_line_style,
)


def build_historiograph_plot(
    params: Params,
    matrix: pd.DataFrame,
    i2y: dict[str, float],
) -> go.Figure:

    nx_graph = nx.from_pandas_adjacency(matrix)
    nx_graph = remove_selfloop_edges(nx_graph)
    nx_graph = set_node_size_properties(params, nx_graph, matrix)
    nx_graph = set_node_year(nx_graph, i2y)

    nx_graph = keep_top_k_edges_per_node(params, nx_graph)
    nx_graph = keep_top_n_edges(params, nx_graph)
    nx_graph = remove_weak_nodes(params, nx_graph)
    nx_graph = keep_top_n_nodes(params, nx_graph)
    nx_graph = remove_isolated_nodes(nx_graph)

    nx_graph = set_top_n_node_labels(
        params=params,
        nx_graph=nx_graph,
    )

    nx_graph = scale_edge_weight(params, nx_graph)
    #
    nx_graph = historiogr_layout(matrix, nx_graph)

    #
    nx_graph = scale_node_size(params, nx_graph)
    nx_graph = scale_textfont_size(params, nx_graph)
    nx_graph = scale_textfont_opacity(params, nx_graph)

    nx_graph = set_node_color_by_year(params, nx_graph)
    nx_graph = set_edge_color_by_group(params, nx_graph)

    nx_graph = set_node_opacity(params, nx_graph)

    nx_graph = set_edge_width_from_pandas_adjacency(nx_graph, matrix)
    nx_graph = scale_edge_width(params, nx_graph)
    nx_graph = scale_edge_opacity(params, nx_graph)

    nx_graph = set_node_textposition(nx_graph)

    nx_graph = set_uniform_edge_line_style(nx_graph, "solid")

    node_trace = build_scatter_node_trace(nx_graph)
    edge_traces = build_scatter_edge_traces(nx_graph)

    fig = build_network_plot(edge_traces, node_trace)
    fig = configure_figure_axes(params, fig)
    fig = add_node_labels(fig, nx_graph)
    fig = add_node_colorscale(params, fig, nx_graph)

    return fig


def historiogr_layout(
    matrix: pd.DataFrame,
    nx_graph: nx.Graph,
) -> nx.Graph:

    x_gap: float = 1.0
    y_gap: float = 1.0
    n_sweeps: int = 4

    # --- 1. Build directed graph from matrix -----------------------------------
    nx_digraph: nx.DiGraph = nx.from_pandas_adjacency(
        matrix,
        create_using=nx.DiGraph,
    )

    # --- 2. Parse years -------------------------------------------------------
    years: dict[str, float] = {col: float(col.split(", ")[1]) for col in matrix.columns}

    years_sorted: list[float] = sorted({years[n] for n in nx_digraph.nodes})
    year_to_x: dict[float, float] = {yr: i * x_gap for i, yr in enumerate(years_sorted)}

    # layers[year] = ordered list of nodes; order is mutated during sweeps
    layers: dict[float, list] = {
        yr: sorted(
            [n for n in nx_digraph.nodes if years[n] == yr],
            key=lambda n: (
                -nx_digraph.in_degree(n),
                -nx_digraph.out_degree(n),
                str(n),
            ),
        )
        for yr in years_sorted
    }

    # --- 3. Sugiyama barycenter sweeps ----------------------------------------

    def _rank(layer_nodes: list) -> dict:
        """Map each node in a layer to its current rank (0-based)."""
        return {n: i for i, n in enumerate(layer_nodes)}

    def _barycenter(node, ref_rank: dict) -> float:
        """
        Average rank of all neighbours (predecessors + successors) that appear
        in ref_rank.  Returns inf if the node has no ranked neighbours,
        so unconnected nodes sink to the bottom.
        """
        neighbours = [
            n
            for n in (*nx_digraph.predecessors(node), *nx_digraph.successors(node))
            if n in ref_rank
        ]
        if not neighbours:
            return float("inf")
        return sum(ref_rank[n] for n in neighbours) / len(neighbours)

    def _sort_layer(nodes: list, ref_rank: dict) -> list:
        """Sort a layer's nodes by barycenter, tie-break by in-degree desc."""
        return sorted(
            nodes,
            key=lambda n: (
                _barycenter(n, ref_rank),
                -nx_digraph.in_degree(n),
                -nx_digraph.out_degree(n),
                str(n),
            ),
        )

    def _forward_sweep() -> None:
        """Left → right: each layer sorted against the layer to its left."""
        for i in range(1, len(years_sorted)):
            yr = years_sorted[i]
            prev_yr = years_sorted[i - 1]
            ref_rank = _rank(layers[prev_yr])
            layers[yr] = _sort_layer(layers[yr], ref_rank)

    def _backward_sweep() -> None:
        """Right → left: each layer sorted against the layer to its right."""
        for i in range(len(years_sorted) - 2, -1, -1):
            yr = years_sorted[i]
            next_yr = years_sorted[i + 1]
            ref_rank = _rank(layers[next_yr])
            layers[yr] = _sort_layer(layers[yr], ref_rank)

    for _ in range(n_sweeps):
        _forward_sweep()
        _backward_sweep()

    # --- 4. Assign positions --------------------------------------------------
    positions: dict = {}
    for yr, nodes in layers.items():
        x = year_to_x[yr]
        center = (len(nodes) - 1) / 2.0
        for i, node in enumerate(nodes):
            positions[node] = (x, (center - i) * y_gap)

    # --- 5. Write to target graph, guard missing nodes -----------------------
    missing = [n for n in nx_graph.nodes if n not in positions]
    if missing:
        raise KeyError(
            f"historiogr_layout: {len(missing)} node(s) in nx_graph are absent "
            f"from the adjacency matrix: {missing[:5]}{'...' if len(missing) > 5 else ''}"
        )

    for node in nx_graph.nodes:
        x, y = positions[node]
        nx_graph.nodes[node]["x"] = x
        nx_graph.nodes[node]["y"] = y

    return nx_graph
