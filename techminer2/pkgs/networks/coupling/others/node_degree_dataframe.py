# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

## >>> from techminer2.coupling_network._core.others.node_degree_frame import _node_degree_frame
## >>> _node_degree_frame(
## ...     unit_of_analysis='authors', # authors, countries, organizations, sources
## ...     #
## ...     # COLUMN PARAMS:
## ...     top_n=20, 
## ...     citations_threshold=0,
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build()
## ... ).head()
   Node                Name  Degree
0     0    Gomber P. 2:1065       3
1     1    Hornuf L. 2:0358       3
2     2  Jagtiani J. 3:0317       3
3     3   Lemieux C. 2:0253       3
4     4    Dolata M. 2:0181       2





"""
# from ....internals.nx.nx_degree_frame import nx_degree_frame
from .internals.create_coupling_nx_graph import _create_coupling_nx_graph


def _node_degree_frame(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
    custom_terms=None,
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
