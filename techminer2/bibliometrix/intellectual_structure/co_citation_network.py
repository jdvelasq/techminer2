"""
Co-citation Network
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix__co_citation_network
>>> nnet = bibliometrix__co_citation_network(
...     topics_length=50,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iterations=10,
...     delta=1.0,    
... )

>>> file_name = "sphinx/_static/bibliometrix__co_citation_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__co_citation_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                                               CL_00  ...                                   CL_05
0       Gomber P, 2017, J BUS ECON, V87, P537 06:140  ...  Szabo N, 1997, FIRST MONDAY, V2 02:007
1            Lee I, 2018, BUS HORIZ, V61, P35 06:027  ...                                        
2  Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 ...  ...                                        
3   Tsai C-H, 2017, ASIAN J LAW SOC, V4, P109 04:028  ...                                        
4       Adhami S, 2018, J ECON BUS, V100, P64 04:027  ...                                        
<BLANKLINE>
[5 rows x 6 columns]

>>> file_name = "sphinx/_static/bibliometrix__co_citation_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__co_citation_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                                    group  ...  pagerank
Adhami S, 2018, J ECON BUS, V100, P64 04:027            0  ...  0.035582
Anagnostopoulos I, 2018, J ECON BUS, V100, P7 1...      1  ...  0.044167
Antweiler W, 2004, J FINANC, V59, P1259 02:028          3  ...  0.017492
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...      2  ...  0.046950
Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 0...      0  ...  0.027119
<BLANKLINE>
[5 rows x 4 columns]

"""
from ..._check_references_csv import check_references_csv
from ..._get_network_graph_communities import get_network_graph_communities
from ..._get_network_graph_degree_plot import get_network_graph_degree_plot
from ..._get_network_graph_indicators import get_network_graph_indicators
from ..._get_network_graph_plot import get_network_graph_plot
from ..._matrix_list_2_network_graph import matrix_list_2_network_graph
from ..._network_community_detection import network_community_detection
from .co_citation_matrix_list import bibliometrix__co_citation_matrix_list


class _Result:
    """Results"""

    def __init__(self):
        self.communities_ = None
        self.indicators_ = None
        self.plot_ = None
        self.degree_plot_ = None


def bibliometrix__co_citation_network(
    topics_length=50,
    directory="./",
    method="louvain",
    nx_k=0.5,
    nx_iterations=10,
    delta=1.0,
    start_year=None,
    end_year=None,
    **filters,
):
    """Co-citation Network."""

    if not check_references_csv(directory):
        return

    matrix_list = bibliometrix__co_citation_matrix_list(
        topics_length=topics_length,
        directory=directory,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    graph = matrix_list_2_network_graph(matrix_list)
    graph = network_community_detection(graph, method=method)

    result = _Result()

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
