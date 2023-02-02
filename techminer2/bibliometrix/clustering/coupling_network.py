"""
Clustering by coupling.
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.clustering.coupling_network(
...     criterion="article",
...     coupling_measured_by='local_references',
...     topics_length=50,
...     metric="local_citations",
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iterations=10,
...     delta=1.0,    
... )

>>> file_name = "sphinx/_static/bibliometrix_coupling_network_plot_by_references.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix_coupling_network_plot_by_references.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                                               CL_00  ...                                       CL_07
0         Muganyi T, 2022, FINANCIAL INNOV, V8 1:013  ...  Lan G, 2023, RES INT BUS FINANC, V64 1:000
1  Ryan P, 2020, ICEIS - PROC INT CONF ENTERP INF...  ...                                            
2                   Turki M, 2020, HELIYON, V6 1:011  ...                                            
3   von Solms J, 2021, J BANK REGUL, V22, P152 1:011  ...                                            
4                Kurum E, 2020, J FINANC CRIME 1:010  ...                                            
<BLANKLINE>
[5 rows x 8 columns]


>>> file_name = "sphinx/_static/bibliometrix_coupling_network_plot_by_references_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix_coupling_network_plot_by_references_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                                    group  ...  pagerank
Hee Jung JH, 2019, FINTECH: LAW AND REGULATION,...      1  ...  0.125258
Mohamed H, 2021, STUD COMPUT INTELL, V935, P153...      1  ...  0.125258
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...      2  ...  0.004481
Huang GKJ, 2017, PROC INT CONF ELECTRON BUS (IC...      4  ...  0.003521
Waye V, 2020, ADELAIDE LAW REV, V40, P363 1:005         0  ...  0.006029
<BLANKLINE>
[5 rows x 4 columns]

"""
from dataclasses import dataclass

from ..._association_index import association_index
from ..._get_network_graph_communities import get_network_graph_communities
from ..._get_network_graph_degree_plot import get_network_graph_degree_plot
from ..._get_network_graph_indicators import get_network_graph_indicators
from ..._get_network_graph_plot import get_network_graph_plot
from ..._matrix_2_matrix_list import matrix_2_matrix_list
from ..._matrix_list_2_network_graph import matrix_list_2_network_graph
from ..._network_community_detection import network_community_detection
from .coupling_matrix_list import coupling_matrix_list


@dataclass(init=False)
class _Results:
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
    nx_k=0.5,
    nx_iterations=10,
    delta=1.0,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Clustering by coupling."""

    matrix_list = coupling_matrix_list(
        criterion=criterion,
        coupling_measured_by=coupling_measured_by,
        topics_length=topics_length,
        metric=metric,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    # matrix list ---> matrix
    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)
    matrix = matrix.astype(int)

    columns = sorted(
        matrix.columns.tolist(), key=lambda x: x.split()[-1].split(":")[0], reverse=True
    )
    indexes = sorted(
        matrix.index.tolist(), key=lambda x: x.split()[-1].split(":")[0], reverse=True
    )
    matrix = matrix.loc[indexes, columns]

    # continue ...
    matrix = association_index(matrix, association=normalization)
    matrix_list = matrix_2_matrix_list(matrix)

    graph = matrix_list_2_network_graph(matrix_list)
    graph = network_community_detection(graph, method=method)

    result = _Results()

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
