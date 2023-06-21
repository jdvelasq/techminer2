# flake8: noqa
"""
Clustering by coupling.
===============================================================================


>>> directory = "data/regtech/"

>>> import techminer2plus
>>> obj = techminer2plus.examples.clustering.coupling_network(
...     criterion="article",
...     coupling_measured_by='local_references',
...     topics_length=50,
...     metric="local_citations",
...     directory=directory,
...     method="louvain",
...     nx_k=0.1,
...     nx_iterations=10,
...     delta=1.0,    
... )

>>> file_name = "sphinx/_static/bibliometrix_coupling_network_plot_by_references.html"
>>> obj.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix_coupling_network_plot_by_references.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> # obj.communities_.head()
                                               CL_00  ...                                       CL_07
0         Muganyi T, 2022, FINANCIAL INNOV, V8 1:013  ...  Lan G, 2023, RES INT BUS FINANC, V64 1:000
1  Ryan P, 2020, ICEIS - PROC INT CONF ENTERP INF...  ...                                            
2                   Turki M, 2020, HELIYON, V6 1:011  ...                                            
3   von Solms J, 2021, J BANK REGUL, V22, P152 1:011  ...                                            
4                Kurum E, 2020, J FINANC CRIME 1:010  ...                                            
<BLANKLINE>
[5 rows x 8 columns]


>>> file_name = "sphinx/_static/bibliometrix_coupling_network_plot_by_references_degree_plot.html"
>>> obj.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix_coupling_network_plot_by_references_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> obj.indicators_.head()
                                                    group  ...  pagerank
Hee Jung JH, 2019, FINTECH: LAW AND REGULATION,...      1  ...  0.125258
Mohamed H, 2021, STUD COMPUT INTELL, V935, P153...      1  ...  0.125258
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...      2  ...  0.004481
Huang GKJ, 2017, PROC INT CONF ELECTRON BUS (IC...      4  ...  0.003521
Waye V, 2020, ADELAIDE LAW REV, V40, P363 1:005         0  ...  0.006029
<BLANKLINE>
[5 rows x 4 columns]


# pylint: disable=too-many-arguments
"""
from dataclasses import dataclass

import networkx as nx

# from ... import network_utils

# # from ..._get_network_graph_communities import get_network_graph_communities
# from ..._get_network_graph_degree_plot import get_network_graph_degree_plot

# # from ..._get_network_graph_indicators import get_network_graph_indicators
# from ..._get_network_graph_plot import get_network_graph_plot
# from ..._matrix_2_matrix_list import matrix_2_matrix_list

# # from ..._matrix_list_2_network_graph import matrix_list_2_network_graph
# from ...vantagepoint.analyze.matrix_normalization import matrix_normalization
# from .coupling_matrix_list import coupling_matrix_list


@dataclass(init=False)
class _CouplingNetwork:
    communities_: None
    indicators_: None
    plot_: None
    degree_plot_: None


def coupling_network(
    criterion,
    coupling_measured_by,
    topics_length=250,
    metric="local_citations",
    normalization="association",
    method="louvain",
    nx_k=0.1,
    nx_iterations=10,
    delta=1.0,
    node_min_size=30,
    node_max_size=70,
    textfont_size_min=10,
    textfont_size_max=20,
    seed=0,
    directory="./",
    database="main",
    start_year=None,
    end_year=None,
    **filters,
):
    """Clustering by coupling."""

    def apply_association_index(normalization, matrix_list):
        matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
        matrix = matrix.fillna(0)
        matrix = matrix.astype(int)

        columns = sorted(
            matrix.columns.tolist(),
            key=lambda x: x.split()[-1].split(":")[0],
            reverse=True,
        )
        indexes = sorted(
            matrix.index.tolist(),
            key=lambda x: x.split()[-1].split(":")[0],
            reverse=True,
        )
        matrix = matrix.loc[indexes, columns]

        # continue ...
        matrix = matrix_normalization(matrix, association=normalization)
        matrix_list = matrix_2_matrix_list(matrix)
        return matrix_list

    #
    #
    #  Main
    #
    #

    matrix_list = coupling_matrix_list(
        unit_of_analysis=criterion,
        coupling_measured_by=coupling_measured_by,
        topics_length=topics_length,
        metric=metric,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list.matrix_list_ = apply_association_index(
        normalization, matrix_list.matrix_list_
    )

    graph = nx.Graph()
    graph = network_utils.nx_add_nodes__to_graph_from_matrix_list(
        graph, matrix_list
    )
    graph = network_utils.nx_create_node_occ_property_from_node_name(graph)
    graph = network_utils.nx_compute_node_property_from_occ(
        graph, "node_size", node_min_size, node_max_size
    )
    graph = network_utils.nx_compute_node_property_from_occ(
        graph, "textfont_size", textfont_size_min, textfont_size_max
    )
    graph = network_utils.nx_add_edges_to_graph_from_matrix_list(
        graph, matrix_list
    )
    graph = network_utils.nx_compute_spring_layout(
        graph, nx_k, nx_iterations, seed
    )

    graph = network_utils.nx_apply_community_detection_method(
        graph, method=method
    )

    node_trace = network_utils.px_create_node_trace(graph)
    text_trace = network_utils.create_text_trace(graph)
    edge_traces = network_utils.px_create_edge_traces(graph)

    fig = network_utils.px_create_network_fig(
        edge_traces, node_trace, text_trace, delta
    )

    chart = _CouplingNetwork()
    chart.plot_ = fig

    return chart

    ###
    graph = matrix_list_2_network_graph(matrix_list)

    result = _CouplingNetwork()

    result.communities_ = get_network_graph_communities(graph)
    result.indicators_ = get_network_graph_indicators(graph)
    result.plot_ = get_network_graph_plot(
        graph,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        delta=delta,
    )
    result.degree_plot_ = get_network_graph_degree_plot(graph)

    return result
