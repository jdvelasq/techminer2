"""
Clustering by coupling.
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix__coupling_network
>>> nnet = bibliometrix__coupling_network(
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
                                               CL_00  ...                                              CL_19
0       Das SR, 2019, FINANC MANAGE, V48, P981 1:024  ...  Thilakarathne DJ, 2020, LECT NOTES COMPUT SCI,...
1  Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 ...  ...                                                   
2     Buckley RP, 2020, J BANK REGUL, V21, P26 1:017  ...                                                   
3  Kavassalis P, 2018, J RISK FINANC, V19, P39 1:014  ...                                                   
4  Micheler E, 2020, EUR BUS ORG LAW REV, V21, P3...  ...                                                   
<BLANKLINE>
[5 rows x 20 columns]



>>> file_name = "sphinx/_static/bibliometrix_coupling_network_plot_by_references_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix_coupling_network_plot_by_references_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                                    group  ...  pagerank
Birch DGW, 2017, HANDB OF BLOCKCHAIN, DIGIT FIN...      7  ...  0.003851
Golubic G, 2019, INTEREULAWEAST, V6, P83 1:001          8  ...  0.003851
Khabrieva TY, 2018, RUS J OF CRIM, V12, P459 1:002      9  ...  0.003851
Scholz FJB, 2018, REV CHIL DERECHO TECNOL, V7, ...     10  ...  0.003851
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...      2  ...  0.044610
<BLANKLINE>
[5 rows x 4 columns]


"""
from dataclasses import dataclass

from .._association_index import association_index
from .._get_network_graph_communities import get_network_graph_communities
from .._get_network_graph_degree_plot import get_network_graph_degree_plot
from .._get_network_graph_indicators import get_network_graph_indicators
from .._get_network_graph_plot import get_network_graph_plot
from .._matrix_2_matrix_list import matrix_2_matrix_list
from .._matrix_list_2_network_graph import matrix_list_2_network_graph
from .._network_community_detection import network_community_detection
from .clustering.coupling_matrix_list import bibliometrix__coupling_matrix_list


@dataclass(init=False)
class _Results:
    communities_: None
    indicators_: None
    plot_: None
    degree_plot_: None


def bibliometrix__coupling_network(
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

    matrix_list = bibliometrix__coupling_matrix_list(
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
