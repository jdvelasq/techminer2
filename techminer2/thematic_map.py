"""
Thematic Map
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

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

    <iframe src="_static/thematic_map_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()

>>> file_name = "sphinx/_static/thematic_map_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/thematic_map_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()

"""

from .association_index import association_index
from .co_occ_matrix import co_occ_matrix
from .co_occ_network import co_occ_network
from .network_communities import network_communities
from .network_community_detection import network_community_detection
from .network_degree_plot import network_degree_plot
from .network_indicators import network_indicators
from .network_plot import network_plot


class Result:
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

    matrix = co_occ_matrix(
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
    matrix_list = matrix_list.reset_index(drop=True)
    # end TODO

    graph = co_occ_network(matrix_list)
    graph = network_community_detection(graph, method=method)

    result = Result(
        communities=network_communities(graph),
        indicators=network_indicators(graph),
        plot=network_plot(
            graph,
            nx_k=nx_k,
            nx_iteratons=nx_iteratons,
            delta=delta,
        ),
        degree_plot=network_degree_plot(graph),
    )

    return result
