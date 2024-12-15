# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx  # type: ignore
import numpy as np

from ...internals.read_filtered_database import read_filtered_database


def _create_co_citation_nx_graph(
    #
    # FUNCTION PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    #
    # Create the networkx graph
    nx_graph = nx.Graph()

    nx_graph = __add_weighted_edges_from(
        nx_graph=nx_graph,
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=None,
        **filters,
    )

    if unit_of_analysis == "cited_references":
        for node in nx_graph.nodes():
            nx_graph.nodes[node]["text"] = ", ".join(node.split(", ")[:2])

    else:
        for node in nx_graph.nodes():
            nx_graph.nodes[node]["text"] = node

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    records = read_filtered_database(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix_list = records[["global_references"]].dropna().copy()
    matrix_list = matrix_list.rename(columns={"global_references": "column"})
    matrix_list = matrix_list.assign(row=records[["global_references"]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    if unit_of_analysis == "cited_authors":
        matrix_list["row"] = matrix_list["row"].str.split(", ").map(lambda x: x[0])
        matrix_list["column"] = (
            matrix_list["column"].str.split(", ").map(lambda x: x[0])
        )
    elif unit_of_analysis == "cited_sources":
        matrix_list["row"] = matrix_list["row"].str.split(", ").map(lambda x: x[2])
        matrix_list["column"] = (
            matrix_list["column"].str.split(", ").map(lambda x: x[2])
        )
    elif unit_of_analysis == "cited_references":
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

    #
    # Computes valild items
    valid_items = __compute_valid_terms(
        unit_of_analysis=unit_of_analysis,
        records=records,
        top_n=top_n,
        citations_threshold=citations_threshold,
        custom_terms=custom_terms,
    )

    #
    # Filter data
    matrix_list = matrix_list.loc[
        matrix_list.row.isin(valid_items["index"].to_list()), :
    ]
    matrix_list = matrix_list.loc[
        matrix_list.column.isin(valid_items["index"].to_list()), :
    ]

    #
    # Adds citations
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

    #
    # Adds the data to the network:
    for _, x in matrix_list.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(x.row, x.column, x.size)],
            dash="solid",
        )

    return nx_graph


def __compute_valid_terms(
    unit_of_analysis,
    records,
    top_n,
    citations_threshold,
    custom_terms,
):
    if custom_terms is not None:
        return custom_terms

    #
    # Creates a list with global references
    global_references = records["global_references"].dropna().copy()
    global_references = global_references.str.split(";")
    global_references = global_references.explode()
    global_references = global_references.str.strip()

    #
    # Transforms each reference into the element of interest
    if unit_of_analysis == "cited_authors":
        global_references = global_references.str.split(", ").map(lambda x: x[0])
    elif unit_of_analysis == "cited_sources":
        global_references = global_references.str.split(", ").map(lambda x: x[2])
    elif unit_of_analysis == "cited_references":
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
    if top_n is not None:
        valid_items = valid_items.head(top_n)
    if citations_threshold is not None:
        valid_items = valid_items.loc[valid_items.citations >= citations_threshold]

    #
    # Returns the selected elements as a list
    return valid_items
