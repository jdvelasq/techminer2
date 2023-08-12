# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx

from ._read_records import read_records
from .co_occurrence_matrix import co_occurrence_matrix
from .normalize_co_occurrence_matrix import normalize_co_occurrence_matrix
from .nx_apply_cdlib_algorithm import nx_apply_cdlib_algorithm
from .nx_compute_edge_width_from_edge_weight import nx_compute_edge_width_from_edge_weight
from .nx_compute_node_size_from_item_occ import nx_compute_node_size_from_item_occ
from .nx_compute_spring_layout import nx_compute_spring_layout
from .nx_compute_textfont_opacity_from_item_occ import nx_compute_textfont_opacity_from_item_occ
from .nx_compute_textfont_size_from_item_occ import nx_compute_textfont_size_from_item_occ
from .nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from .nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from .nx_set_node_color_from_group_attr import nx_set_node_color_from_group_attr
from .nx_set_node_size_to_constant import nx_set_node_size_to_constant
from .nx_set_textfont_opacity_to_constant import nx_set_textfont_opacity_to_constant
from .nx_set_textfont_size_to_constant import nx_set_textfont_size_to_constant
from .performance.performance_metrics import performance_metrics


def nx_create_citation_graph(
    #
    # FUNCTION PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK CLUSTERING:
    association_index="association",
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size=30,
    textfont_size=10,
    textfont_opacity=1.00,
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_min=0.8,
    edge_width_max=3.0,
    #
    # AXES:
    # xaxes_range=None,
    # yaxes_range=None,
    # show_axes=False,
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
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

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
    nx_graph = nx_set_node_size_to_constant(nx_graph, node_size)
    nx_graph = nx_set_textfont_size_to_constant(nx_graph, textfont_size)
    nx_graph = nx_set_textfont_opacity_to_constant(nx_graph, textfont_opacity)

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_min, edge_width_max)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)
    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
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
    # data_frame contains the citing and cited articles.
    data_frame = records[["article", "local_references"]]
    data_frame = data_frame.dropna()
    data_frame["local_references"] = data_frame.local_references.str.split(";")
    data_frame = data_frame.explode("local_references")
    data_frame["local_references"] = data_frame["local_references"].str.strip()
    data_frame.columns = ["citing_unit", "cited_unit"]

    records.index = records.article.copy()

    if unit_of_analysis == "authors":
        article2authors = {
            row.article: row.authors for _, row in records[["article", "authors"]].iterrows()
        }
        data_frame["citing_unit"] = data_frame["citing_unit"].map(article2authors)
        data_frame["cited_unit"] = data_frame["cited_unit"].map(article2authors)

    elif unit_of_analysis == "countries":
        article2countries = {
            row.article: row.countries for _, row in records[["article", "countries"]].iterrows()
        }
        data_frame["citing_unit"] = data_frame["citing_unit"].map(article2countries)
        data_frame["cited_unit"] = data_frame["cited_unit"].map(article2countries)

    elif unit_of_analysis == "article":
        data_frame["citing_unit"] = (
            data_frame["citing_unit"].str.split(", ").map(lambda x: x[:3]).str.join(", ")
        )
        data_frame["cited_unit"] = (
            data_frame["cited_unit"].str.split(", ").map(lambda x: x[:3]).str.join(", ")
        )

    elif unit_of_analysis == "organizations":
        article2organizations = {
            row.article: row.organizations
            for _, row in records[["article", "organizations"]].iterrows()
        }
        data_frame["citing_unit"] = data_frame["citing_unit"].map(article2organizations)
        data_frame["cited_unit"] = data_frame["cited_unit"].map(article2organizations)

    elif unit_of_analysis == "source_abbr":
        article2source_abbr = {
            row.article: row.source_abbr
            for _, row in records[["article", "source_abbr"]].iterrows()
        }
        data_frame["citing_unit"] = data_frame["citing_unit"].map(article2source_abbr)
        data_frame["cited_unit"] = data_frame["cited_unit"].map(article2source_abbr)

    else:
        raise ValueError("Bad unit_of_analysis")

    #
    # Explode columns to find the relationships
    data_frame["citing_unit"] = data_frame["citing_unit"].str.split(";")
    data_frame = data_frame.explode("citing_unit")
    data_frame["citing_unit"] = data_frame["citing_unit"].str.strip()

    data_frame["cited_unit"] = data_frame["cited_unit"].str.split(";")
    data_frame = data_frame.explode("cited_unit")
    data_frame["cited_unit"] = data_frame["cited_unit"].str.strip()

    data_frame = data_frame.loc[
        data_frame.apply(lambda row: row.citing_unit != row.cited_unit, axis=1), :
    ]

    #
    # Filter the data
    if unit_of_analysis != "article":
        metrics = performance_metrics(
            #
            # ITEMS PARAMS:
            field=unit_of_analysis,
            metric="OCC",
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        ).df_

        data_frame = data_frame.loc[data_frame.citing_unit.isin(metrics.index), :]
        data_frame = data_frame.loc[data_frame.cited_unit.isin(metrics.index), :]

    #
    # Computes the number of citations per citing_unit-cited_unit pair
    data_frame = data_frame.groupby(
        #
        # Generates:
        #      citing_unit           cited_unit  size
        # 0      Anasweh M    Anagnostopoulos I     1
        # 1       Arman AA    Anagnostopoulos I     4
        # 2       Arman AA            Anasweh M     3
        # 3       Arman AA             Arner DW     2
        # 4       Arman AA             Becker M     4
        # ..           ...                  ...   ...
        ["citing_unit", "cited_unit"],
        as_index=False,
    ).size()

    #
    # Adds the data to the network:
    for _, row in data_frame.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row.citing_unit, row.cited_unit, row["size"])],
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
