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

>>> from techminer2.analyze.coupling_network import terms_by_cluster_frame
>>> terms_by_cluster_frame(

...         algorithm_or_dict="louvain",
...         unit_of_analysis='authors', # article
...                                     # authors 
...                                     # countries
...                                     # organizations 
...                                     # sources
...         top_n=20, 
...         citations_threshold=0,
...         #
...         # FILTERS NOT VALID FOR 'article' UNIT OF ANALYSIS:
...         occurrence_threshold=2,
...         custom_terms=None,
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... )
                    0                     1                2
0    Gomber P. 2:1065      Dolata M. 2:0181    Gai K. 2:0323
1    Hornuf L. 2:0358     Schwabe G. 2:0181    Qiu M. 2:0323
2  Jagtiani J. 3:0317  Zavolokina L. 2:0181  Sun X./3 2:0323
3   Lemieux C. 2:0253                                       


>>> # article:
>>> from techminer2.analyze.coupling_network import terms_by_cluster_frame
>>> terms_by_cluster_frame(
...     .set_analysis_params(
...         algorithm_or_dict="louvain",
...         unit_of_analysis='article', # article
...                                     # authors 
...                                     # countries, 
...                                     # organizations 
...                                     # sources
...         top_n=30, 
...         citations_threshold=0,
...     #
...     # NOT VALID FOR 'article' UNIT OF ANALYSIS:
...     occurrence_threshold=2,
...     custom_terms=None,
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... )
                                                0  ...                                           3
0    Gracia D.B., 2019, IND MANAGE DATA SYS 1:225  ...           Alt R., 2018, ELECTRON MARK 1:150
1                     Hu Z., 2019, SYMMETRY 1:176  ...    Gomber P., 2018, J MANAGE INF SYST 1:576
2       Gai K., 2018, J NETWORK COMPUT APPL 1:238  ...    Gozman D., 2018, J MANAGE INF SYST 1:120
3      Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161  ...  Iman N., 2018, ELECT COMMER RES APPL 1:102
4          Kim Y., 2016, INT J APPL ENG RES 1:125  ...                                            
5  Lim S.H., 2019, INT J HUMCOMPUT INTERACT 1:121  ...                                            
6     Stewart H., 2018, INF COMPUT SECURITY 1:104  ...                                            
<BLANKLINE>
[7 rows x 4 columns]


"""
from .docs.terms_by_cluster_dataframe import (
    _terms_by_cluster_frame as docs_terms_by_cluster_frame,
)
from .others.terms_by_cluster_dataframe import (
    _terms_by_cluster_frame as others_terms_by_cluster_frame,
)


def terms_by_cluster_frame(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
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

        return docs_terms_by_cluster_frame(
            #
            # ARTICLE PARAMS:
            top_n=top_n,
            citations_threshold=citations_threshold,
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

    return others_terms_by_cluster_frame(
        unit_of_analysis,
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
