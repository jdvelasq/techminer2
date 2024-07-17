# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Degree Plot
===============================================================================


>>> from techminer2.network.co_occurrence import plot_node_degree_from_co_occurrence_network
>>> plot = plot_node_degree_from_co_occurrence_network(
...     #
...     # PARAMS:
...     field='author_keywords',
...     #
...     # COLUMN PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     association_index="association",
...     #
...     # DEGREE PLOT:
...     textfont_size=10,
...     marker_size=7,
...     line_color="black",
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> plot.fig_.write_html("sphinx/_static/network/co_occurrence/plot_node_degree_from_co_occurrence_network.html")

.. raw:: html

    <iframe src="../../_static/network/co_occurrence/plot_node_degree_from_co_occurrence_network.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                        Name  Degree
0     0             FINTECH 31:5168      18
1     1  FINANCIAL_SERVICES 04:0667       7
2     2          INNOVATION 07:0911       6
3     3          TECHNOLOGY 02:0310       5
4     4             FINANCE 02:0309       5

>>> print(plot.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
from ...core.nx.nx_assign_degree_to_nodes import nx_assign_degree_to_nodes
from ...core.nx.nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ...core.nx.nx_generate_node_degree_distribution_chart import nx_generate_node_degree_distribution_chart


def plot_node_degree_from_co_occurrence_network(
    #
    # PARAMS:
    field,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK PARAMS:
    association_index="association",
    #
    # DEGREE PLOT:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=field,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # NETWORK PARAMS:
        association_index=association_index,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = nx_assign_degree_to_nodes(nx_graph)

    return nx_generate_node_degree_distribution_chart(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # DEGREE PLOT PARAMS:
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
