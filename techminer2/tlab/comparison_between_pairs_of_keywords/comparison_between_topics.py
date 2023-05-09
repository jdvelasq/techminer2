"""
Compararison between topics
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import tlab
>>> cbt = tlab.comparison_between_pairs_of_keywords.comparison_between_topics(
...     criterion="author_keywords",
...     topic_a="artificial intelligence",
...     topic_b="regtech",
...     topics_length=None,
...     topic_min_occ=None,
...     topic_min_citations=None,
...     custom_topics=[
...         "fintech",
...         "blockchain",
...         "machine learning",
...     ],
...     directory=directory,
... )

>>> file_name = "sphinx/_static/tlab__co_occurrence_analysis__comparison_between_topics_bar_chart-1.html"
>>> cbt.bar_chart_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/tlab__co_occurrence_analysis__comparison_between_topics_bar_chart-1.html" height="600px" width="100%" frameBorder="0"></iframe>




>>> directory = "data/regtech/"

>>> from techminer2 import tlab
>>> cbt = tlab.comparison_between_pairs_of_keywords.comparison_between_topics(
...     criterion="author_keywords",
...     topic_a="artificial intelligence",
...     topic_b="regtech",
...     topics_length=20,
...     topic_min_occ=None,
...     topic_min_citations=None,
...     directory=directory,
... )

>>> cbt.table_.head(10)
                                 row                     column  OCC
0            artificial intelligence             fintech 12:249    0
1  artificial intelligence & regtech             fintech 12:249    1
2                            regtech             fintech 12:249   11
3            artificial intelligence          compliance 07:030    0
4                            regtech          compliance 07:030    6
5  artificial intelligence & regtech          compliance 07:030    1
6            artificial intelligence          regulation 05:164    0
7  artificial intelligence & regtech          regulation 05:164    0
8                            regtech          regulation 05:164    4
9                            regtech  financial services 04:168    3


>>> file_name = "sphinx/_static/tlab__co_occurrence_analysis__comparison_between_topics_bar_chart.html"
>>> cbt.bar_chart_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/tlab__co_occurrence_analysis__comparison_between_topics_bar_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/tlab__co_occurrence_analysis__comparison_between_topics_radial_diagram.html"
>>> cbt.radial_diagram_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/tlab__co_occurrence_analysis__comparison_between_topics_radial_diagram.html" height="600px" width="100%" frameBorder="0"></iframe>



"""
from dataclasses import dataclass

import networkx as nx
import plotly.express as px

from ..._items2counters import items2counters
from ..._load_stopwords import load_stopwords
from ..._read_records import read_records
from ...techminer.indicators.indicators_by_topic import indicators_by_topic
from ...vantagepoint.report.matrix_viewer import (
    _color_node_points,
    _create_network_graph,
    _create_traces,
    _make_layout,
)


@dataclass(init=False)
class _Results:
    table_: None
    bar_chart_: None
    radial_diagram_: None


def comparison_between_topics(
    criterion,
    topic_a,
    topic_b,
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    nx_k=0.5,
    nx_iterations=10,
    delta=0.2,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Comparison between topics."""

    matrix_list = _create_comparison_matrix_list(
        topic_a=topic_a,
        topic_b=topic_b,
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = _remove_stopwords(
        directory,
        matrix_list,
    )

    matrix_list = _select_topics(
        matrix_list=matrix_list,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        topics_length=topics_length,
        custom_topics=custom_topics,
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = _add_counters_to_items(
        matrix_list=matrix_list,
        column_name="column",
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = _sort_matrix_list(matrix_list)
    matrix_list = matrix_list.reset_index(drop=True)

    results = _Results()
    results.table_ = matrix_list
    results.bar_chart_ = _create_bart_chart(matrix_list, topic_a, topic_b)
    results.radial_diagram_ = _create_radial_diagram(
        matrix_list, topic_a, topic_b, nx_k, nx_iterations, delta
    )

    return results


def _create_radial_diagram(matrix_list, topic_a, topic_b, nx_k, nx_iterations, delta):
    graph = nx.Graph()
    graph = _create_nodes(graph, matrix_list, topic_a, topic_b)
    graph = _create_edges(graph, matrix_list, topic_a, topic_b)
    graph = _make_layout(graph, nx_k, nx_iterations)
    edge_trace, node_trace = _create_traces(graph)
    node_trace = _color_node_points(graph, node_trace)
    fig = _create_network_graph(edge_trace, node_trace, delta)
    return fig


def _create_edges(graph, matrix_list, topic_a, topic_b):
    edges_dict = {}
    for _, row in matrix_list.iterrows():
        if row[0] == topic_a or row[0] == topic_b:
            if (row[0], row[1]) not in edges_dict:
                edges_dict[(row[0], row[1])] = row[2]
            else:
                edges_dict[(row[0], row[1])] += row[2]
        else:
            keys = row[0].split("&")
            keys = [key.strip() for key in keys]
            if (keys[0], row[1]) not in edges_dict:
                edges_dict[(keys[0], row[1])] = row[2]
            else:
                edges_dict[(keys[0], row[1])] += row[2]

            if (keys[1], row[1]) not in edges_dict:
                edges_dict[(keys[1], row[1])] = row[2]
            else:
                edges_dict[(keys[1], row[1])] += row[2]

    edges = []
    for key1, key2 in edges_dict:
        edges += [(key1, key2, edges_dict[(key1, key2)])]

    graph.add_weighted_edges_from(edges)
    return graph


def _create_nodes(graph, matrix_list, topic_a, topic_b):
    nodes = []

    indicators = matrix_list.copy()
    indicators = indicators[["column", "OCC"]]
    indicators = indicators.groupby("column", as_index=True).aggregate("sum")
    topic_size = indicators.sort_values(by=["OCC"], ascending=False)

    nodes += [
        (topic, dict(size=topic_size.loc[topic], group=0)) for topic in topic_size.index
    ]

    indicators = matrix_list.copy()
    indicators = indicators[["row", "OCC"]]
    indicators = indicators.groupby("row", as_index=True).aggregate("sum")
    topic_size = indicators.sort_values(by=["OCC"], ascending=False)

    group_a = (
        0 if topic_size.loc[topic_a]["OCC"] > topic_size.loc[topic_b]["OCC"] else 1
    )
    group_b = 0 if group_a == 1 else 1

    join_terms = " & ".join([topic_a, topic_b])
    if join_terms in topic_size.index:
        nodes += [
            (
                topic_a,
                dict(
                    size=topic_size.loc[topic_a]["OCC"]
                    + topic_size.loc[" & ".join([topic_a, topic_b])]["OCC"],
                    group=group_a,
                ),
            )
        ]

        nodes += [
            (
                topic_b,
                dict(
                    size=topic_size.loc[topic_b]["OCC"]
                    + topic_size.loc[" & ".join([topic_a, topic_b])]["OCC"],
                    group=group_b,
                ),
            )
        ]

    else:
        nodes += [
            (
                topic_a,
                dict(
                    size=topic_size.loc[topic_a]["OCC"],
                    group=group_a,
                ),
            )
        ]

        nodes += [
            (
                topic_b,
                dict(
                    size=topic_size.loc[topic_b]["OCC"],
                    group=group_b,
                ),
            )
        ]

    graph.add_nodes_from(nodes)
    return graph


def _create_bart_chart(matrix_list, topic_a, topic_b):
    matrix_list = matrix_list.copy()

    fig = px.bar(
        matrix_list,
        x="OCC",
        y="column",
        color="row",
        title="Co-occurrences between topics",
        hover_data=["OCC"],
        orientation="h",
        color_discrete_map={
            topic_a: "#CCD3D9",
            topic_b: "#99A8B3",
            " & ".join(sorted([topic_a, topic_b])): "#556f81",
        },
    )
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    fig.update_layout(
        yaxis_title=None,
    )

    return fig


def _select_topics(
    matrix_list,
    topic_min_occ,
    topic_min_citations,
    topics_length,
    custom_topics,
    criterion,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    indicators = indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if custom_topics is None:
        if topic_min_occ is not None:
            indicators = indicators[indicators.OCC >= topic_min_occ]
        if topic_min_citations is not None:
            indicators = indicators[indicators.global_citations >= topic_min_citations]

        indicators = indicators.sort_values(
            ["OCC", "global_citations", "local_citations"],
            ascending=[False, False, False],
        )

        if topics_length is not None:
            indicators = indicators.head(topics_length)

        custom_topics = indicators.index.to_list()

    matrix_list = matrix_list.loc[matrix_list.column.isin(custom_topics), :]

    return matrix_list


def _remove_stopwords(directory, matrix_list):
    stopwords = load_stopwords(directory)
    matrix_list = matrix_list[~matrix_list["column"].isin(stopwords)]
    return matrix_list


def _create_comparison_matrix_list(
    topic_a,
    topic_b,
    criterion,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = records[[criterion]].copy()
    matrix_list = matrix_list.dropna()
    matrix_list = matrix_list.rename(columns={criterion: "column"})
    matrix_list = matrix_list.assign(row=records[[criterion]])

    # Explode 'row' for topic_a and topic_b
    matrix_list["row"] = matrix_list["row"].str.split(";")
    matrix_list["row"] = matrix_list["row"].map(lambda x: [y.strip() for y in x])
    matrix_list = matrix_list[
        matrix_list["row"].map(lambda x: any([y in [topic_a, topic_b] for y in x]))
    ]

    matrix_list["row"] = matrix_list["row"].map(
        lambda x: sorted([y for y in x if y in [topic_a, topic_b]])
    )
    matrix_list["row"] = matrix_list["row"].str.join(" & ")
    matrix_list = matrix_list.explode("row")
    matrix_list["row"] = matrix_list["row"].str.strip()

    # Explode 'column' for all topics
    matrix_list["column"] = matrix_list["column"].str.split(";")
    matrix_list = matrix_list.explode("column")
    matrix_list["column"] = matrix_list["column"].str.strip()
    matrix_list = matrix_list[
        matrix_list["column"].map(lambda x: x not in [topic_a, topic_b])
    ]

    # count
    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
        "sum"
    )

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)
    if " & ".join([topic_a, topic_b]) not in matrix.index.to_list():
        matrix.loc[" & ".join(sorted([topic_a, topic_b]))] = 0

    matrix_list = matrix.melt(value_name="OCC", var_name="column", ignore_index=False)

    matrix_list = matrix_list.reset_index()
    matrix_list["OCC"] = matrix_list["OCC"].astype(int)

    return matrix_list


def _sort_matrix_list(matrix_list):
    indicators = matrix_list.copy()
    indicators = indicators[["column", "OCC"]]
    indicators = indicators.groupby("column", as_index=False).aggregate("sum")
    indicators = indicators.sort_values(by=["OCC"], ascending=False)
    sorted_topics = indicators["column"]
    topics2rank = {topic: i for i, topic in enumerate(sorted_topics)}

    matrix_list["rank"] = matrix_list["column"].map(topics2rank)
    matrix_list = matrix_list.sort_values(by=["rank"], ascending=True)
    matrix_list = matrix_list.drop(columns=["rank"])

    return matrix_list


def _add_counters_to_items(
    matrix_list,
    column_name,
    criterion,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    new_column_names = items2counters(
        column=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    matrix_list[column_name] = matrix_list[column_name].map(new_column_names)
    return matrix_list
