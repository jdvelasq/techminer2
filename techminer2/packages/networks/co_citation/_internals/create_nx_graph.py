# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx  # type: ignore
import numpy as np

from .....database._internals.io import internal__load_filtered_records_from_database


# -------------------------------------------------------------------------
def _step_01_load_records(params):
    return internal__load_filtered_records_from_database(params=params)


# -------------------------------------------------------------------------
def _step_02_compute_co_occurrences_between_references(params, records):

    matrix_list = records[["global_references"]].dropna().copy()
    matrix_list = matrix_list.rename(columns={"global_references": "column"})
    matrix_list = matrix_list.assign(row=records[["global_references"]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    if params.unit_of_analysis == "cited_authors":
        matrix_list["row"] = matrix_list["row"].str.split(", ").map(lambda x: x[0])
        matrix_list["column"] = (
            matrix_list["column"].str.split(", ").map(lambda x: x[0])
        )
    elif params.unit_of_analysis == "cited_sources":
        matrix_list["row"] = matrix_list["row"].str.split(", ").map(lambda x: x[2])
        matrix_list["column"] = (
            matrix_list["column"].str.split(", ").map(lambda x: x[2])
        )
    elif params.unit_of_analysis == "cited_references":
        matrix_list["row"] = (
            matrix_list["row"].str.split(", ").map(lambda x: x[:3]).str.join(", ")
        )
        matrix_list["column"] = (
            matrix_list["column"].str.split(", ").map(lambda x: x[:3]).str.join(", ")
        )
    else:
        raise ValueError("Bad unit_of_analysis")

    matrix_list = matrix_list.loc[
        matrix_list.apply(lambda x: x.row != x.column, axis=1), :
    ]

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
        "sum"
    )

    matrix_list = matrix_list.sort_values(
        ["OCC", "row", "column"], ascending=[False, True, True]
    )
    return matrix_list


# -------------------------------------------------------------------------
def _step_03_compute_terms(params, records):

    if params.terms_in is not None:
        return params.terms_in

    #
    # Creates a list with global references
    global_references = records["global_references"].dropna().copy()
    global_references = global_references.str.split(";")
    global_references = global_references.explode()
    global_references = global_references.str.strip()

    #
    # Transforms each reference into the element of interest
    if params.unit_of_analysis == "cited_authors":
        global_references = global_references.str.split(", ").map(lambda x: x[0])
    elif params.unit_of_analysis == "cited_sources":
        global_references = global_references.str.split(", ").map(lambda x: x[2])
    elif params.unit_of_analysis == "cited_references":
        global_references = (
            global_references.str.split(", ").map(lambda x: x[:3]).str.join(", ")
        )
    else:
        raise ValueError("Bad unit_of_analysis")

    #
    # Counts the number of appareances of each element of interest
    valid_items = global_references.value_counts().to_frame()
    valid_items.columns = ["citations"]
    valid_items = valid_items.rename_axis("index")
    valid_items = valid_items.reset_index()
    valid_items = valid_items.sort_values(
        ["citations", "index"], ascending=[False, True]
    )

    #
    # Applies the filters
    if params.top_n is not None:
        valid_items = valid_items.head(params.top_n)
    if params.citation_threshold is not None:
        valid_items = valid_items.loc[
            valid_items.citations >= params.citation_threshold
        ]

    #
    # Returns the selected elements as a list
    return valid_items


# -------------------------------------------------------------------------
def _step_04_filter_matrix_list(matrix_list, valid_items):
    matrix_list = matrix_list.loc[
        matrix_list.row.isin(valid_items["index"].to_list()), :
    ]
    matrix_list = matrix_list.loc[
        matrix_list.column.isin(valid_items["index"].to_list()), :
    ]
    return matrix_list


# -------------------------------------------------------------------------
def _step_05_adds_citations_to_terms(valid_items, matrix_list):

    max_citations = valid_items.citations.max()
    n_zeros = int(np.log10(max_citations - 1)) + 1
    fmt = " 1:{:0" + str(n_zeros) + "d}"

    #
    # Rename the items adding the citations
    rename_dict = {
        key: value
        for key, value in zip(
            valid_items["index"].to_list(),
            (valid_items["index"] + valid_items["citations"].map(fmt.format)).to_list(),
        )
    }
    matrix_list["row"] = matrix_list["row"].map(rename_dict)
    matrix_list["column"] = matrix_list["column"].map(rename_dict)

    return matrix_list


# -------------------------------------------------------------------------
def _step_06_create_a_nx_graph(matrix_list):
    nx_graph = nx.Graph()
    for _, x in matrix_list.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(x.row, x.column, x.size)],
            dash="solid",
        )
    return nx_graph


# -------------------------------------------------------------------------
def _step_07_set_text_property_of_nodes(nx_graph, params):

    if params.unit_of_analysis == "cited_references":
        for node in nx_graph.nodes():
            nx_graph.nodes[node]["text"] = ", ".join(node.split(", ")[:2])

    else:
        for node in nx_graph.nodes():
            nx_graph.nodes[node]["text"] = node

    return nx_graph


# -------------------------------------------------------------------------
def internal__create_nx_graph(params):

    records = _step_01_load_records(params)
    matrix_list = _step_02_compute_co_occurrences_between_references(params, records)
    valid_terms = _step_03_compute_terms(params, records)
    matrix_list = _step_04_filter_matrix_list(matrix_list, valid_terms)
    matrix_list = _step_05_adds_citations_to_terms(valid_terms, matrix_list)
    nx_graph = _step_06_create_a_nx_graph(matrix_list)
    nx_graph = _step_07_set_text_property_of_nodes(nx_graph, params)

    return nx_graph
