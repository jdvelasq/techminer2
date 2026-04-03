import networkx as nx  # type: ignore
import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.nx import (
    assign_node_sizes_based_on_occurrences,
    assign_text_positions_based_on_quadrants,
    assign_textfont_opacity_based_on_occurrences,
    assign_textfont_sizes_based_on_occurrences,
    compute_spring_layout_positions,
    plot_nx_graph,
)


def plot_correl_map(
    params: Params,
    matrix: pd.DataFrame,
):

    nx_graph = nx.Graph()

    matrix_list = _matrix_to_matrix_list(matrix)
    matrix_list = _remove_isolated_nodes(matrix_list)
    matrix_list = _apply_similarity_threshold(
        matrix_list, params.edge_similarity_threshold
    )
    matrix_list = _select_top_links(matrix_list, params.edge_top_n)
    matrix_list = _select_top_links_per_node(matrix_list, params.max_edges_per_node)
    nx_graph = _add_weighted_edges_from(nx_graph, matrix_list)
    nx_graph = _set_node_properties(params, nx_graph, matrix_list)

    nx_graph = compute_spring_layout_positions(params, nx_graph)
    nx_graph = assign_node_sizes_based_on_occurrences(params, nx_graph)
    nx_graph = assign_textfont_sizes_based_on_occurrences(params, nx_graph)
    nx_graph = assign_textfont_opacity_based_on_occurrences(params, nx_graph)
    nx_graph = assign_text_positions_based_on_quadrants(nx_graph)

    nx_graph = _set_edge_properties(params, nx_graph)

    return plot_nx_graph(params=params, nx_graph=nx_graph)


def _add_weighted_edges_from(
    nx_graph,
    matrix_list,
):
    matrix_list = matrix_list.copy()

    for _, row in matrix_list.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row["rows"], row["columns"], row["CORR"])],
        )

    return nx_graph


def _set_node_properties(params, nx_graph, matrix_list):

    matrix_list = matrix_list.copy()
    nodes = set(matrix_list["rows"]).union(set(matrix_list["columns"]))

    nodes_df = pd.DataFrame({"node": list(nodes)})
    nodes_df["OCC"] = nodes_df["node"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[0])
    )
    nodes_df["GCS"] = nodes_df["node"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[1])
    )
    nodes_df = nodes_df.sort_values(
        by=["OCC", "GCS", "node"],
        ascending=[False, False, True],
    ).reset_index(drop=True)

    labeld_nodes = nodes_df["node"].tolist()
    labeld_nodes = labeld_nodes[: params.node_n_labels]

    for node in nx_graph.nodes():

        nx_graph.nodes[node]["group"] = 0
        nx_graph.nodes[node]["node_color"] = params.node_colors[0]

        if params.counters:
            nx_graph.nodes[node]["text"] = node
        else:
            nx_graph.nodes[node]["text"] = " ".join(node.split(" ")[:-1])

        if node in labeld_nodes:
            nx_graph.nodes[node]["labeled"] = True
        else:
            nx_graph.nodes[node]["labeled"] = False

    return nx_graph


def _apply_similarity_threshold(
    matrix_list: pd.DataFrame, threshold: float
) -> pd.DataFrame:
    matrix_list = matrix_list.copy()
    matrix_list = matrix_list.loc[matrix_list["CORR"] >= threshold, :]
    return matrix_list


def _select_top_links_per_node(
    matrix_list: pd.DataFrame, max_edges_per_node: int
) -> pd.DataFrame:

    matrix_list = matrix_list.copy()
    matrix_list["selected"] = False

    nodes = set(matrix_list["rows"]).union(set(matrix_list["columns"]))

    for node in nodes:

        selected_rows = matrix_list["rows"] == node
        selected_columns = matrix_list["columns"] == node

        selected_edges = matrix_list[selected_rows | selected_columns]
        selected_edges = selected_edges.head(max_edges_per_node)

        matrix_list.loc[selected_edges.index, "selected"] = True

    matrix_list = matrix_list.loc[matrix_list["selected"], :]

    return matrix_list


def _select_top_links(matrix_list: pd.DataFrame, top_n: int) -> pd.DataFrame:
    matrix_list = matrix_list.head(top_n)
    return matrix_list


def _remove_isolated_nodes(matrix_list: pd.DataFrame) -> pd.DataFrame:
    matrix_list = matrix_list.copy()
    selected = [row["rows"] != row["columns"] for _, row in matrix_list.iterrows()]
    matrix_list = matrix_list.loc[selected, :]
    return matrix_list


def _matrix_to_matrix_list(matrix):

    matrix_list = matrix.melt(
        ignore_index=False, var_name="col", value_name="CORR"
    ).reset_index()

    matrix_list = matrix_list.rename({"index": "rows", "col": "columns"}, axis=1)
    matrix_list["row_OCC"] = matrix_list["rows"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[0])
    )
    matrix_list["row_GCS"] = matrix_list["rows"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[1])
    )
    matrix_list["col_OCC"] = matrix_list["columns"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[0])
    )
    matrix_list["col_GCS"] = matrix_list["columns"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[1])
    )

    matrix_list = matrix_list.sort_values(
        by=["CORR", "row_OCC", "col_OCC", "row_GCS", "col_GCS", "rows", "columns"],
        ascending=[False, False, False, False, False, True, True],
    ).reset_index(drop=True)

    matrix_list = matrix_list[["rows", "columns", "CORR"]]

    return matrix_list


def _set_edge_properties(params, nx_graph):

    for edge in nx_graph.edges():

        weight = nx_graph.edges[edge]["weight"]

        if weight < 0.25:
            width, dash = params.edge_widths[0], "dot"
            edge_color = params.edge_colors[0]

        elif weight < 0.5:
            width, dash = params.edge_widths[1], "dash"
            edge_color = params.edge_colors[1]

        elif weight < 0.75:
            width, dash = params.edge_widths[2], "solid"
            edge_color = params.edge_colors[2]

        else:
            width, dash = params.edge_widths[3], "solid"
            edge_color = params.edge_colors[3]

        nx_graph.edges[edge]["width"] = width
        nx_graph.edges[edge]["dash"] = dash
        nx_graph.edges[edge]["color"] = edge_color

    return nx_graph
