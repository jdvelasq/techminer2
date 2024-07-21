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

>>> from techminer2.coupling_network import terms_by_cluster_frame
>>> terms_by_cluster_frame(
...     unit_of_analysis='authors', # article
...                                 # authors 
...                                 # countries
...                                 # organizations 
...                                 # sources
...     #
...     # FILTERS:
...     top_n=20, 
...     citations_threshold=0,
...     #
...     # FILTERS NOT VALID FOR 'article' UNIT OF ANALYSIS:
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
... )
                    0                     1                2
0    Gomber P. 2:1065      Dolata M. 2:0181    Gai K. 2:0323
1    Hornuf L. 2:0358     Schwabe G. 2:0181    Qiu M. 2:0323
2  Jagtiani J. 3:0317  Zavolokina L. 2:0181  Sun X./3 2:0323
3   Lemieux C. 2:0253                                       


>>> # article:
>>> from techminer2.coupling_network import terms_by_cluster_frame
>>> terms_by_cluster_frame(
...     unit_of_analysis='article', # article
...                                 # authors 
...                                 # countries, 
...                                 # organizations 
...                                 # sources
...     #
...     # FILTERS:
...     top_n=30, 
...     citations_threshold=0,
...     #
...     # NOT VALID FOR 'article' UNIT OF ANALYSIS:
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
from ._core.docs.terms_by_cluster_frame import _terms_by_cluster_frame as docs_terms_by_cluster_frame
from ._core.others.terms_by_cluster_frame import _terms_by_cluster_frame as others_terms_by_cluster_frame


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
