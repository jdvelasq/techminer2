# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx  # type: ignore
import numpy as np

from ...._core.read_filtered_database import read_filtered_database


def _create_coupling_nx_graph(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
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
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = " ".join(node.split(" ")[:-1])

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    top_n=None,
    citations_threshold=0,
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
        sort_by=None,
        **filters,
    )

    records = records.sort_values(
        ["global_citations", "local_citations", "year", "article"],
        ascending=[False, False, False, True],
    )
    records = records.dropna(subset=["global_references"])
    #
    # Same order of selection of VOSviewer
    if citations_threshold is not None:
        records = records.loc[records.global_citations >= citations_threshold, :]
    if top_n is not None:
        records = records.head(top_n)
    #
    #
    # Adds citations to the article id
    max_citations = records.global_citations.max()
    n_zeros = int(np.log10(max_citations - 1)) + 1
    fmt = " 1:{:0" + str(n_zeros) + "d}"
    records["article"] = records["article"] + records["global_citations"].map(fmt.format)

    data_frame = records[["article", "global_references"]]
    data_frame = data_frame.dropna()
    data_frame["article"] = data_frame["article"].str.split("; ").map(lambda x: [y.strip() for y in x])
    data_frame["global_references"] = data_frame["global_references"].str.split(";").map(lambda x: [y.strip() for y in x])

    data_frame = data_frame.explode("article")
    data_frame = data_frame.explode("global_references")

    data_frame = data_frame.groupby(["global_references"], as_index=True).agg({"article": list})

    data_frame.columns = ["row"]
    data_frame["column"] = data_frame.row.copy()

    data_frame = data_frame.explode("row")
    data_frame = data_frame.explode("column")
    data_frame = data_frame.loc[data_frame.row != data_frame.column, :]
    data_frame = data_frame.groupby(["row", "column"], as_index=False).size()

    #
    # Formats only articles
    data_frame["row"] = data_frame["row"].str.split(", ").map(lambda x: x[:2] + [x[2] + " " + x[-1].split(" ")[-1]]).str.join(", ")
    #
    data_frame["column"] = data_frame["column"].str.split(", ").map(lambda x: x[:2] + [x[2] + " " + x[-1].split(" ")[-1]]).str.join(", ")

    #
    # Adds the data to the network:
    for _, row in data_frame.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row.row, row.column, row["size"])],
            dash="solid",
        )

    return nx_graph


def __assign_group_from_dict(nx_graph, group_dict):
    #
    # The group is assigned using and external algorithm. It is designed
    # to provide analysis capabilities to the system when other types of
    # analysis are conducted, for example, factor analysis.
    for node, group in group_dict.items():
        nx_graph.nodes[node]["group"] = group
    return nx_graph
