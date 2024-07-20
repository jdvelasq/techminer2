# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================


>>> from techminer2.citation_network import terms_by_cluster_frame
>>> terms_by_cluster_frame(
...     #
...     # FUNCTION PARAMS:
...     unit_of_analysis="article",
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
... ).head()
                                                   0  ...                                                  4
0       Gomber P., 2017, J BUS ECON, V87, P537 1:489  ...  Anagnostopoulos I., 2018, J ECON BUS, V100, P7...
1  Gomber P., 2018, J MANAGE INF SYST, V35, P220 ...  ...     Zavolokina L., 2016, FINANCIAL INNOV, V2 1:106
2  Gozman D., 2018, J MANAGE INF SYST, V35, P145 ...  ...                                                   
3       Alt R., 2018, ELECTRON MARK, V28, P235 1:150  ...                                                   
4            Lee I., 2018, BUS HORIZ, V61, P35 1:557  ...                                                   
<BLANKLINE>
[5 rows x 5 columns]


>>> # abbr_source_title, authors, organizations, countries:
>>> from techminer2.citation_network import terms_by_cluster_frame
>>> terms_by_cluster_frame(
...     #
...     # FUNCTION PARAMS:
...     unit_of_analysis="abbr_source_title",
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_threshold=0,
...     occurrence_threshold=2,
...     custom_terms=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                         0                       1                          2
0    Electron. Mark. 2:287   Financ. Manage. 2:161  Ind Manage Data Sys 2:386
1  J Manage Inf Syst 2:696     J. Econ. Bus. 3:422                           
2     Sustainability 2:150  Financial Innov. 2:190                           




"""
from ._core._terms_by_cluster_frame_from_documents import _terms_by_cluster_frame_from_documents
from ._core._terms_by_cluster_frame_from_others import _terms_by_cluster_frame_from_others


def terms_by_cluster_frame(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    #
    occurrence_threshold=None,
    custom_terms=None,
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
    """:meta private:"""

    if unit_of_analysis == "article":

        return _terms_by_cluster_frame_from_documents(
            #
            # COLUMN PARAMS:
            top_n=top_n,
            citations_threshold=citations_threshold,
            #
            # NETWORK CLUSTERING:
            algorithm_or_dict=algorithm_or_dict,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return _terms_by_cluster_frame_from_others(
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
        #
        # NETWORK PARAMS:
        algorithm_or_dict=algorithm_or_dict,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
