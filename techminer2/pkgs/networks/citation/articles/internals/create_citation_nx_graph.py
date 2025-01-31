# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx  # type: ignore
import numpy as np

from ......database.load.load__database import load__filtered_database


def _create_citation_nx_graph(
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
    records = load__filtered_database(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        record_years_range=year_filter,
        record_citations_range=cited_by_filter,
        records_order_by=None,
        **filters,
    )

    #
    # Filter the data using the specified parameters
    records = records.sort_values(
        ["global_citations", "local_citations", "year", "article"],
        ascending=[False, False, False, True],
    )
    #
    # Same order of selection of VOSviewer
    if citations_threshold is not None:
        records = records.loc[records.global_citations >= citations_threshold, :]
    if top_n is not None:
        records = records.head(top_n)

    #
    # data_frame contains the citing and cited articles.
    data_frame = records[["article", "local_references", "global_citations"]]

    #
    # Continues the processing
    data_frame.loc[:, "local_references"] = data_frame.local_references.str.split(";")
    data_frame = data_frame.explode("local_references")
    data_frame["local_references"] = data_frame["local_references"].str.strip()

    #
    # Local references must be in article column
    data_frame_with_links = data_frame[
        data_frame["local_references"].map(lambda x: x in data_frame.article.to_list())
    ]

    #
    # Adds citations to the article
    max_citations = records.global_citations.max()
    n_zeros = int(np.log10(max_citations - 1)) + 1
    fmt = " 1:{:0" + str(n_zeros) + "d}"
    #
    rename_dict = {
        key: value
        for key, value in zip(
            data_frame["article"].to_list(),
            (
                data_frame["article"] + data_frame["global_citations"].map(fmt.format)
            ).to_list(),
        )
    }
    #
    data_frame_with_links.loc[:, "article"] = data_frame_with_links["article"].map(
        rename_dict
    )
    data_frame_with_links.loc[:, "local_references"] = data_frame_with_links[
        "local_references"
    ].map(rename_dict)

    #
    # Removes documents without local citations in references
    data_frame = data_frame.dropna()

    #
    # Adds the links to the network:
    for _, row in data_frame_with_links.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row.local_references, row.article, 1)],
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
