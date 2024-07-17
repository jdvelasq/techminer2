# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Communities
===============================================================================


>>> from techminer2.science_mapping.bibliographic_coupling.documents import communities
>>> communities(
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
                                     CL_0  ...                                        CL_3
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
from ....core.nx.nx_create_coupling_graph_from_documents import nx_create_coupling_graph_from_documents
from ....core.nx.nx_extract_communities_to_frame import nx_extract_communities_to_frame


def generate_communities_from_documents_coupling_network(
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
    """
    :meta private:
    """
    # --------------------------------------------------------------------------
    # TODO: REMOVE DEPENDENCES:
    #
    # NODES:
    node_size_range = (30, 70)
    textfont_size_range = (10, 20)
    textfont_opacity_range = (0.35, 1.00)
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_range = (0.8, 3.0)
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    #
    # --------------------------------------------------------------------------

    nx_graph = nx_create_coupling_graph_from_documents(
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        textfont_opacity_range=textfont_opacity_range,
        #
        # EDGES:
        edge_color=edge_color,
        edge_width_range=edge_width_range,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return nx_extract_communities_to_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
