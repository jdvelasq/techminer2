"""
Co-citation Network
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.intellectual_structure.co_citation_network(
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
                                               CL_00  ...                                              CL_02
0  Barrell R, 2011, NATL INST ECON REV, V216, PF4...  ...  Williams JW, 2013, ACCOUNT ORGAN SOC, V38, P54...
1  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...   Currie WL, 2018, J INF TECHNOL, V33, P304 03:005
2  Butler T/1, 2019, PALGRAVE STUD DIGIT BUS ENAB...  ...  Singh C, 2020, J MONEY LAUND CONTROL, V24, P46...
3  Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3...  ...       Bellamy RKE, 2019, IBM J RES DEV, V63 02:017
4  Kavassalis P, 2018, J RISK FINANC, V19, P39 08...  ...   Smith KT, 2010, J STRATEG MARK, V18, P201 02:017
<BLANKLINE>
[5 rows x 3 columns]

>>> file_name = "sphinx/_static/bibliometrix__co_citation_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__co_citation_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                                    group  ...  pagerank
Anagnostopoulos I, 2018, J ECON BUS, V100, P7 1...      0  ...  0.050024
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...      1  ...  0.018383
Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 0...      1  ...  0.021444
Bamberger KA, 2010, TEX LAW REV, V88, P669 03:008       0  ...  0.005976
Barrell R, 2011, NATL INST ECON REV, V216, PF4 ...      0  ...  0.150584
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
from .co_citation_matrix_list import co_citation_matrix_list


class _Result:
    """Results"""

    def __init__(self):
        self.communities_ = None
        self.indicators_ = None
        self.plot_ = None
        self.degree_plot_ = None


def co_citation_network(
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

    matrix_list = co_citation_matrix_list(
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
