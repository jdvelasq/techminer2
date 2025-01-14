# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx  # type: ignore
import numpy as np

from .....database.load.load__filtered_database import load__filtered_database
from .....internals.utils.utils_append_occurrences_and_citations_to_axis import (
    _utils_append_occurrences_and_citations_to_axis,
)
from ....metrics.performance_metrics_dataframe import performance_metrics_frame


def _create_coupling_nx_graph(
    #
    # FUNCTION PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
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
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
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

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
    custom_terms=None,
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
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=None,
        **filters,
    )

    #
    data_frame = records[[unit_of_analysis, "global_references"]]
    data_frame = data_frame.dropna()
    data_frame[unit_of_analysis] = (
        data_frame[unit_of_analysis]
        .str.split("; ")
        .map(lambda x: [y.strip() for y in x])
    )
    data_frame["global_references"] = (
        data_frame["global_references"]
        .str.split(";")
        .map(lambda x: [y.strip() for y in x])
    )

    data_frame = data_frame.explode(unit_of_analysis)
    data_frame = data_frame.explode("global_references")

    data_frame = data_frame.groupby(["global_references"], as_index=True).agg(
        {unit_of_analysis: list}
    )

    data_frame.columns = ["row"]
    data_frame["column"] = data_frame.row.copy()

    data_frame = data_frame.explode("row")
    data_frame = data_frame.explode("column")
    data_frame = data_frame.loc[data_frame.row != data_frame.column, :]
    data_frame = data_frame.groupby(["row", "column"], as_index=False).size()

    #
    # Filter the data

    metrics = performance_metrics_frame(
        #
        # ITEMS PARAMS:
        field=unit_of_analysis,
        metric="OCC",
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=(occurrence_threshold, None),
        gc_range=(citations_threshold, None),
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = data_frame.loc[data_frame.row.isin(metrics.index), :]
    data_frame = data_frame.loc[data_frame.column.isin(metrics.index), :]

    #
    # Adds the counters to the data frame:
    data_frame.index = data_frame.row.values
    data_frame = _utils_append_occurrences_and_citations_to_axis(
        dataframe=data_frame,
        axis=0,
        field=unit_of_analysis,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    data_frame["row"] = data_frame.index.values

    #
    # Adds the counters to the data frame:
    data_frame.index = data_frame.column.values
    data_frame = _utils_append_occurrences_and_citations_to_axis(
        dataframe=data_frame,
        axis=0,
        field=unit_of_analysis,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    data_frame["column"] = data_frame.index.values

    #
    #
    data_frame.index = np.arange(len(data_frame))

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
