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


>>> from techminer2.science_mapping.citation.network.documents import communities
>>> x = communities(
...     #
...     # COLUMN PARAMS:
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
>>> print(x.to_markdown())
|    | CL_0                                                 | CL_1                                                      | CL_2                                                  | CL_3                                                   | CL_4                                                 | CL_5                                               |
|---:|:-----------------------------------------------------|:----------------------------------------------------------|:------------------------------------------------------|:-------------------------------------------------------|:-----------------------------------------------------|:---------------------------------------------------|
|  0 | Gomber P., 2017, J BUS ECON, V87, P537 1:489         | Ryu H.-S., 2018, IND MANAGE DATA SYS, V118, P541 1:161    | Shim Y., 2016, TELECOMMUN POLICY, V40, P168 1:146     | Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69 1:253 | Anagnostopoulos I., 2018, J ECON BUS, V100, P7 1:202 | Kim Y., 2016, INT J APPL ENG RES, V11, P1058 1:125 |
|  1 | Gomber P., 2018, J MANAGE INF SYST, V35, P220 1:576  | Gracia D.B., 2019, IND MANAGE DATA SYS, V119, P1411 1:225 | Gai K., 2018, J NETWORK COMPUT APPL, V103, P262 1:238 | Haddad C., 2019, SMALL BUS ECON, V53, P81 1:258        | Zavolokina L., 2016, FINANCIAL INNOV, V2 1:106       | Gimpel H., 2018, ELECTRON MARK, V28, P245 1:137    |
|  2 | Gozman D., 2018, J MANAGE INF SYST, V35, P145 1:120  | Hu Z., 2019, SYMMETRY, V11 1:176                          | Schueffel P., 2016, J INNOV MANAG, V4, P32 1:226      |                                                        |                                                      |                                                    |
|  3 | Alt R., 2018, ELECTRON MARK, V28, P235 1:150         | Gabor D., 2017, NEW POLIT ECON, V22, P423 1:314           |                                                       |                                                        |                                                      |                                                    |
|  4 | Lee I., 2018, BUS HORIZ, V61, P35 1:557              | Leong C., 2017, INT J INF MANAGE, V37, P92 1:180          |                                                       |                                                        |                                                      |                                                    |
|  5 | Iman N., 2018, ELECT COMMER RES APPL, V30, P72 1:102 | Stewart H., 2018, INF COMPUT SECURITY, V26, P109 1:104    |                                                       |                                                        |                                                      |                                                    |


"""
from ..._core.nx.nx_create_citation_graph_from_documents import nx_create_citation_graph_from_documents
from ..._core.nx.nx_extract_communities_to_frame import nx_extract_communities_to_frame


def generate_communities_from_documents_citation_network(
    #
    # COLUMN PARAMS:
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

    nx_graph = nx_create_citation_graph_from_documents(
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
