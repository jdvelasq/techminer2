def add_weighted_edges_from_matrix_list(
    nx_graph,
    matrix_list,
):
    matrix_list = matrix_list.copy()
    col_name = matrix_list.columns[-1]

    for _, row in matrix_list.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row["rows"], row["columns"], row[col_name])],
        )

    return nx_graph
