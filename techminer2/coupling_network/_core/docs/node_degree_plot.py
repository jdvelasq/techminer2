# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

>>> from techminer2.coupling_network._core.docs.node_degree_plot import _node_degree_plot
>>> plot = _node_degree_plot(
...     #
...     # ARTICLE PARAMS:
...     top_n=20, 
...     citations_threshold=0,
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
>>> plot.fig_.write_html("sphinx/_static/coupling_network/_core/docs/node_degree_plot.html")

.. raw:: html

    <iframe src="../../_static/coupling_network/_core/docs/node_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> plot.df_.head()
   Node                                        Name  Degree
0     0  Anagnostopoulos I., 2018, J ECON BUS 1:202       7
1     1           Gomber P., 2017, J BUS ECON 1:489       7
2     2    Gomber P., 2018, J MANAGE INF SYST 1:576       5
3     3                 Hu Z., 2019, SYMMETRY 1:176       4
4     4  Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161       4


>>> print(plot.prompt_) # doctest: +ELLIPSIS                                        
Your task is ...


"""
from ...._core.nx.nx_assign_degree_to_nodes import nx_assign_degree_to_nodes
from ...._core.nx.nx_degree_plot import nx_degree_plot
from ._create_coupling_nx_graph import _create_coupling_nx_graph


def _node_degree_plot(
    #
    # ARTICLE PARAMS:
    top_n=None,
    citations_threshold=0,
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

    nx_graph = _create_coupling_nx_graph(
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = nx_assign_degree_to_nodes(nx_graph)

    return nx_degree_plot(
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
