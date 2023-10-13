# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx
import numpy as np

from ._read_records import read_records
from .nx_apply_cdlib_algorithm import nx_apply_cdlib_algorithm
from .nx_compute_edge_width_from_edge_weight import (
    nx_compute_edge_width_from_edge_weight,
)
from .nx_compute_node_size_from_item_citations import (
    nx_compute_node_size_from_item_citations,
)
from .nx_compute_spring_layout import nx_compute_spring_layout
from .nx_compute_textfont_opacity_from_item_citations import (
    nx_compute_textfont_opacity_from_item_citations,
)
from .nx_compute_textfont_size_from_item_citations import (
    nx_compute_textfont_size_from_item_citations,
)
from .nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from .nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from .nx_set_node_color_from_group_attr import nx_set_node_color_from_group_attr


def nx_create_citation_graph_documents(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # NETWORK CLUSTERING:
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_range=(0.8, 3.0),
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

    #
    # Cluster the networkx graph
    if isinstance(algorithm_or_dict, str):
        nx_graph = nx_apply_cdlib_algorithm(nx_graph, algorithm_or_dict)
    if isinstance(algorithm_or_dict, dict):
        nx_graph = __assign_group_from_dict(nx_graph, algorithm_or_dict)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = nx_set_node_color_from_group_attr(nx_graph)
    #
    nx_graph = nx_compute_node_size_from_item_citations(nx_graph, node_size_range)
    nx_graph = nx_compute_textfont_size_from_item_citations(
        nx_graph, textfont_size_range
    )
    nx_graph = nx_compute_textfont_opacity_from_item_citations(
        nx_graph, textfont_opacity_range
    )

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_range)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)
    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)

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
    records = read_records(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
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
    # Removes documents without local citations in references
    data_frame = data_frame.dropna()

    #
    # Continues the processing
    data_frame["local_references"] = data_frame.local_references.str.split(";")
    data_frame = data_frame.explode("local_references")
    data_frame["local_references"] = data_frame["local_references"].str.strip()

    #
    # Local references must be in article column
    data_frame_with_links = data_frame[
        data_frame["local_references"].map(lambda x: x in data_frame.article.to_list())
    ]

    # data_frame_without_links = data_frame[
    #     data_frame["local_references"].map(
    #         lambda x: x not in data_frame.article.to_list()
    #     )
    # ]

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
    data_frame_with_links["article"] = data_frame_with_links["article"].map(rename_dict)
    data_frame_with_links["local_references"] = data_frame_with_links[
        "local_references"
    ].map(rename_dict)

    # data_frame_without_links["article"] = data_frame_without_links["article"].map(
    #     rename_dict
    # )
    # data_frame_without_links["local_references"] = data_frame_without_links[
    #     "local_references"
    # ].map(rename_dict)

    #
    # # Removes self-citations (this case not exists)
    # data_frame_with_links = data_frame_with_links[
    #     data_frame_with_links.apply(
    #         lambda row: row.article != row.local_references, axis=1
    #     )
    # ]

    # #
    # # Adds isolated nodes to the network:
    # nodes = data_frame_without_links["article"].drop_duplicates().to_list()
    # nx_graph.add_nodes_from(nodes, group=0)

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
