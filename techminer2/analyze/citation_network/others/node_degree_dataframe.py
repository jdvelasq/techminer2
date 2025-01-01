# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Frame
===============================================================================




>>> # abbr_source_title, authors, organizations, countries:
>>> from techminer2.analyze.citation_network  import NodeDegreeDataFrame
>>> node_degree_frame(
...     .set_analysis_params(
...         # unit_of_analysis="abbr_source_title",
...         top_n=30,
...         citations_threshold=0,
...         occurrence_threshold=2,
...         custom_terms=None,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... ).head()
   Node                       Name  Degree
0     0    J Manage Inf Syst 2:696       3
1     1        J. Econ. Bus. 3:422       3
2     2      Electron. Mark. 2:287       1
3     3      Financ. Manage. 2:161       1
4     4  Ind Manage Data Sys 2:386       1






"""
from ....internals.nx.nx_degree_frame import nx_degree_frame
from .internals.create_citation_nx_graph import _create_citation_nx_graph


def _node_degree_frame(
    #
    # FIELD PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    occurrence_threshold=None,
    custom_terms=None,
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
        # FUNCTION PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
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
