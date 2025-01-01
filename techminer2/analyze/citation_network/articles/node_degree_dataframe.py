# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Dataframe
===============================================================================

>>> from techminer2.analyze.citation_network.articles  import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     .set_analysis_params(
...         #cunit_of_analysis="article",
...         top_n=30, 
...         citations_threshold=0,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... ).head()
   Node                                               Name  Degree
0     0                   Hu Z., 2019, SYMMETRY, V11 1:176       7
1     1       Gomber P., 2017, J BUS ECON, V87, P537 1:489       4
2     2  Gomber P., 2018, J MANAGE INF SYST, V35, P220 ...       4
3     3       Alt R., 2018, ELECTRON MARK, V28, P235 1:150       4
4     4  Gozman D., 2018, J MANAGE INF SYST, V35, P145 ...       2


"""
from ....internals.nx.nx_degree_frame import nx_degree_frame
from .internals.create_citation_nx_graph import _create_citation_nx_graph

UNIT_OF_ANALYSIS = "article"


def _node_degree_frame(
    #
    # COLUMN PARAMS:
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
    """:meta private:"""

    nx_graph = _create_citation_nx_graph(
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
