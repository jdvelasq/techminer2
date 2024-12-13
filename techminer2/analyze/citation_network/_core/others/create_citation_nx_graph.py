# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx  # type: ignore
import numpy as np

from ....._core.read_filtered_database import read_filtered_database
from .....metrics.performance_metrics_frame import performance_metrics_frame


def _create_citation_nx_graph(
    #
    # FUNCTION PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=(None, None),
    occurrence_threshold=(None, None),
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
        nx_graph.nodes[node]["text"] = " ".join(node.split(" ")[:-1])

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=(None, None),
    occurrence_threshold=(None, None),
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
        sort_by=None,
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

    article2unit = {
        row.article: row[unit_of_analysis]
        for _, row in records[["article", unit_of_analysis]].iterrows()
    }
    data_frame["citing_unit"] = data_frame["citing_unit"].map(article2unit)
    data_frame["cited_unit"] = data_frame["cited_unit"].map(article2unit)

    #
    # Explode columns to find the relationships
    data_frame["citing_unit"] = data_frame["citing_unit"].str.split(";")
    data_frame = data_frame.explode("citing_unit")
    data_frame["citing_unit"] = data_frame["citing_unit"].str.strip()

    data_frame["cited_unit"] = data_frame["cited_unit"].str.split(";")
    data_frame = data_frame.explode("cited_unit")
    data_frame["cited_unit"] = data_frame["cited_unit"].str.strip()

    #
    # Compute citations and occurrences
    metrics = performance_metrics_frame(
        #
        # ITEMS PARAMS:
        field=unit_of_analysis,
        metric="OCCGC",
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
    data_frame = data_frame.loc[data_frame.citing_unit.isin(metrics.index.to_list()), :]
    data_frame = data_frame.loc[data_frame.cited_unit.isin(metrics.index.to_list()), :]

    #
    # Adds citations and occurrences to items
    max_occ = metrics.OCC.max()
    n_zeros = int(np.log10(max_occ - 1)) + 1
    fmt_occ = "{:0" + str(n_zeros) + "d}"

    max_citations = metrics.global_citations.max()
    n_zeros = int(np.log10(max_citations - 1)) + 1
    fmt_citations = "{:0" + str(n_zeros) + "d}"

    rename_dict = {
        key: value
        for key, value in zip(
            metrics.index.to_list(),
            (
                metrics.index
                + " "
                + metrics["OCC"].map(fmt_occ.format)
                + ":"
                + metrics["global_citations"].map(fmt_citations.format)
            ).to_list(),
        )
    }

    data_frame["citing_unit"] = data_frame["citing_unit"].map(rename_dict)
    data_frame["cited_unit"] = data_frame["cited_unit"].map(rename_dict)

    #
    # Computes the number of citations per citing_unit-cited_unit pair
    data_frame = data_frame.groupby(
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
