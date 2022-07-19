"""
Co-citation Network
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import co_citation_network
>>> nnet = co_citation_network(
...     top_n=50,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iteratons=10,
...     delta=1.0,    
... )

>>> file_name = "sphinx/_static/co_citation_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/co_citation_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                                               CL_00  ...                                   CL_05
0       Gomber P, 2017, J BUS ECON, V87, P537 06:140  ...  Szabo N, 1997, FIRST MONDAY, V2 02:007
1            Lee I, 2018, BUS HORIZ, V61, P35 06:027  ...                                        
2  Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 ...  ...                                        
3   Tsai C-H, 2017, ASIAN J LAW SOC, V4, P109 04:028  ...                                        
4       Adhami S, 2018, J ECON BUS, V100, P64 04:027  ...                                        
<BLANKLINE>
[5 rows x 6 columns]

>>> file_name = "sphinx/_static/co_citation_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/co_citation_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


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
from ...co_occ_network import co_occ_network
from ...network_communities import network_communities
from ...network_community_detection import network_community_detection
from ...network_degree_plot import network_degree_plot
from ...network_indicators import network_indicators
from ...network_plot import network_plot
from .co_citation_matrix_list import co_citation_matrix_list


class _Result:
    """Results"""

    def __init__(self):
        self.communities_ = None
        self.indicators_ = None
        self.plot_ = None
        self.degree_plot_ = None


def co_citation_network(
    top_n=50,
    directory="./",
    method="louvain",
    nx_k=0.5,
    nx_iteratons=10,
    delta=1.0,
):
    """Co-citation Network."""

    matrix_list = co_citation_matrix_list(
        top_n=top_n,
        directory=directory,
    )

    graph = co_occ_network(matrix_list)
    graph = network_community_detection(graph, method=method)

    result = _Result()

    result.communities_ = network_communities(graph)
    result.indicators_ = network_indicators(graph)
    result.plot_ = network_plot(
        graph,
        nx_k=nx_k,
        nx_iteratons=nx_iteratons,
        delta=delta,
    )
    result.degree_plot_ = network_degree_plot(graph)

    return result
