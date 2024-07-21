# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

>>> from techminer2.coupling_network._core.docs.terms_by_cluster_frame import _terms_by_cluster_frame
>>> _terms_by_cluster_frame(
...     #
...     # ARTICLE PARAMS:
...     top_n=30, 
...     citations_threshold=0,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
                                        0  ...                                           3
0     Jagtiani J., 2018, J ECON BUS 1:156  ...           Alt R., 2018, ELECTRON MARK 1:150
1      Jakšič M., 2019, RISK MANAGE 1:102  ...    Gomber P., 2018, J MANAGE INF SYST 1:576
2    Cai C.W., 2018, ACCOUNT FINANC 1:145  ...    Gozman D., 2018, J MANAGE INF SYST 1:120
3       Gomber P., 2017, J BUS ECON 1:489  ...  Iman N., 2018, ELECT COMMER RES APPL 1:102
4   Haddad C., 2019, SMALL BUS ECON 1:258  ...                                            
5           Lee I., 2018, BUS HORIZ 1:557  ...                                            
6  Chen M.A., 2019, REV FINANC STUD 1:235  ...                                            
7  Leong C., 2017, INT J INF MANAGE 1:180  ...                                            
<BLANKLINE>
[8 rows x 4 columns]



"""
from ...._core.nx.nx_cluster_graph import nx_cluster_graph
from ...._core.nx.nx_extract_communities_to_frame import nx_extract_communities_to_frame
from ._create_coupling_nx_graph import _create_coupling_nx_graph


def _terms_by_cluster_frame(
    #
    # ARTICLE PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
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

    nx_graph = nx_cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    return nx_extract_communities_to_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
