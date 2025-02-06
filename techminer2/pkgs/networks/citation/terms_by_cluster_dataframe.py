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


## >>> from techminer2.pkgs.citation_network  import TermsByClusterDataFrame
## >>> (
## ...     TermsByClusterDataFrame()
## ...     .set_analysis_params(
## ...         unit_of_analysis="article",
## ...         top_n=30, 
## ...         citations_threshold=0,
## ...     .using_clustering_algorithm_or_dict("louvain")
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... ).head()
                                                   0  ...                                                  3
0  Ryu H.-S., 2018, IND MANAGE DATA SYS, V118, P5...  ...  Anagnostopoulos I., 2018, J ECON BUS, V100, P7...
1  Gracia D.B., 2019, IND MANAGE DATA SYS, V119, ...  ...     Zavolokina L., 2016, FINANCIAL INNOV, V2 1:106
2                   Hu Z., 2019, SYMMETRY, V11 1:176  ...                                                   
3    Gabor D., 2017, NEW POLIT ECON, V22, P423 1:314  ...                                                   
4  Gai K., 2018, J NETWORK COMPUT APPL, V103, P26...  ...                                                   
<BLANKLINE>
[5 rows x 4 columns]


## >>> # abbr_source_title, authors, organizations, countries:
## >>> from techminer2.pkgs.citation_network  import TermsByClusterDataFrame
## >>> (
## ...     TermsByClusterDataFrame()
## ...     .set_analysis_params(
## ...         unit_of_analysis="abbr_source_title",
## ...         top_n=30, 
## ...         citations_threshold=0,
## ...         occurrence_threshold=2,
## ...         custom_terms=None,
## ...        algorithm_or_dict="louvain",
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... ).head()
                         0                       1                          2
0    Electron. Mark. 2:287   Financ. Manage. 2:161  Ind Manage Data Sys 2:386
1  J Manage Inf Syst 2:696     J. Econ. Bus. 3:422                           
2     Sustainability 2:150  Financial Innov. 2:190                           




"""
from .articles.terms_by_cluster_dataframe import (
    _terms_by_cluster_frame as _terms_by_cluster_frame_from_docs,
)
from .others.terms_by_cluster_dataframe import _terms_by_cluster_frame


def terms_by_cluster_dataframe(
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

        return _terms_by_cluster_frame_from_docs(
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

    return _terms_by_cluster_frame(
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
