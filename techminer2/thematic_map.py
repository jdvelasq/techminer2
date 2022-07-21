"""
Thematic Map
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import thematic_map
>>> nnet = thematic_map(
...     "author_keywords",
...     top_n=20,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iteratons=10,
...     delta=1.0,    
... )


>>> file_name = "sphinx/_static/thematic_map_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/thematic_map_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                            CL_00  ...                    CL_02
0                  regtech 70:462  ...        regulation 06:120
1                  fintech 42:406  ...      crowdfunding 04:030
2               blockchain 18:109  ...  cryptocurrencies 04:029
3  artificial intelligence 13:065  ...        innovation 04:029
4               compliance 12:020  ...          big data 04:027
<BLANKLINE>
[5 rows x 3 columns]


>>> file_name = "sphinx/_static/thematic_map_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/thematic_map_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                group  betweenness  closeness  pagerank
regtech 70:462                      0     0.131537   1.000000  0.214240
fintech 42:406                      0     0.131537   1.000000  0.167876
blockchain 18:109                   0     0.060777   0.826087  0.077431
artificial intelligence 13:065      0     0.053314   0.791667  0.059587
compliance 12:020                   0     0.007317   0.612903  0.038065

"""

from .association_index import association_index
from .vantagepoint__co_occ_matrix import vantagepoint__co_occ_matrix
from .matrix_list_2_network_graph import matrix_list_2_network_graph
from .get_network_graph_communities import get_network_graph_communities
from .network_community_detection import network_community_detection
from .get_network_graph_degree_plot import get_network_graph_degree_plot
from .get_network_graph_indicators import get_network_graph_indicators
from .get_network_graph_plot import network_graph_plot


class _Result:
    """Results"""

    def __init__(self, communities, indicators, plot, degree_plot):
        self.communities_ = communities
        self.indicators_ = indicators
        self.plot_ = plot
        self.degree_plot_ = degree_plot


def thematic_map(
    column,
    top_n=None,
    directory="./",
    database="documents",
    method="louvain",
    nx_k=0.5,
    nx_iteratons=10,
    delta=1.0,
):
    """Thematic map network analysis"""

    matrix = vantagepoint__co_occ_matrix(
        column=column,
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        directory=directory,
        database=database,
    )

    association_index(
        matrix=matrix,
        association="association",
    )

    # TODO: refactor as a function
    matrix_list = matrix.melt(value_name="OCC", var_name="column", ignore_index=False)
    matrix_list = matrix_list.reset_index()
    matrix_list = matrix_list.rename(columns={"index": "row"})
    matrix_list = matrix_list.sort_values(
        by=["OCC", "row", "column"], ascending=[False, True, True]
    )
    matrix_list = matrix_list[matrix_list.OCC > 0]
    matrix_list = matrix_list.reset_index(drop=True)
    # end TODO

    graph = matrix_list_2_network_graph(matrix_list)
    graph = network_community_detection(graph, method=method)

    result = _Result(
        communities=get_network_graph_communities(graph),
        indicators=get_network_graph_indicators(graph),
        plot=network_graph_plot(
            graph,
            nx_k=nx_k,
            nx_iteratons=nx_iteratons,
            delta=delta,
        ),
        degree_plot=get_network_graph_degree_plot(graph),
    )

    return result
