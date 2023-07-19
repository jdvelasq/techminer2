# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx

from .._read_records import read_records
from ..vantagepoint.discover.list_items import list_items
from ..vantagepoint.discover.matrix import co_occurrence_matrix
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
    # Explodes local_references field. Each row in the dataframe is equivalent
    # to a link between two documents. This step obtains the data when the
    # unit_of_analysis == 'documents'.
    records["local_references"] = records.local_references.str.split(";")
    records = records.explode("local_references")
    records["local_references"] = records.local_references.str.strip()
    records.index = records.article.copy()

    if unit_of_analysis == "article":
        records["citing_unit"] = records.article
        records["cited_unit"] = records.local_references
    else:
        records["citing_unit"] = records[unit_of_analysis].copy()
        records["cited_unit"] = records.local_references

        ref_to_unit_of_analysis = dict(
            zip(
                records.local_references.dropna().to_list(),
                records.loc[records.local_references.dropna(), unit_of_analysis],
            )
        )
        records["cited_unit"] = records.cited_unit.map(
            lambda x: ref_to_unit_of_analysis[x] if x in ref_to_unit_of_analysis else x
        )

        records["citing_unit"] = records.citing_unit.str.split(";")
        records = records.explode("citing_unit")
        records["citing_unit"] = records.citing_unit.str.strip()

        records["cited_unit"] = records.cited_unit.str.split(";")
        records = records.explode("cited_unit")
        records["cited_unit"] = records.cited_unit.str.strip()

    #
    # Computes the number of citations per citing_unit-cited_unit pair
    records = records[["citing_unit", "cited_unit"]]

    records = records.groupby(
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

    if unit_of_analysis != "article":
        #
        # Filters the records.
        metrics = list_items(
            #
            # ITEMS PARAMS:
            field=unit_of_analysis,
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

        records = records.loc[
            (records.citing_unit.isin(metrics.index.to_list()))
            & (records.cited_unit.isin(metrics.index.to_list())),
            :,
        ]

    #
    #
    for _, row in records.iterrows():
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
