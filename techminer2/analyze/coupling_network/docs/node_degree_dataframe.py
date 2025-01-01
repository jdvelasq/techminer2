# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

## >>> from techminer2.coupling_network._core.docs.node_degree_frame import _node_degree_frame
## >>> _node_degree_frame(
## ...     #
## ...     # ARTICLE PARAMS:
## ...     top_n=20, 
## ...     citations_threshold=0,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... ).head()
   Node                                        Name  Degree
0     0  Anagnostopoulos I., 2018, J ECON BUS 1:202       7
1     1           Gomber P., 2017, J BUS ECON 1:489       6
2     2    Gomber P., 2018, J MANAGE INF SYST 1:576       5
3     3                 Hu Z., 2019, SYMMETRY 1:176       4
4     4  Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161       4


"""
# from ....internals.nx.nx_degree_frame import nx_degree_frame
from .internals.create_coupling_nx_graph import _create_coupling_nx_graph


def _node_degree_frame(
    #
    # ARTICLE PARAMS:
    top_n=None,
    citations_threshold=0,
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

    return nx_degree_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
